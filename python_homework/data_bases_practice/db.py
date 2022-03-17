import sqlite3
import pandas as pd
import requests
import time
from bs4 import BeautifulSoup


def get_scheme_df(df):
    '''
    Create SQL scheme from DataFrame colnames.
    Return SQL scheme and list with processed colnames.
    '''
    col_names, types = df.columns, df.dtypes
    scheme_df = ['row_id INTEGER PRIMARY KEY']
    new_names = ['row_id']

    for name, contain in zip(col_names[1:], types[1:]):
        name = name.replace("-", "").replace("  ", " ").replace(" ", "_")
        new_names.append(name)

        if 'int' in str(contain):
            scheme_df.append(' '.join([name, 'INTEGER']))

        elif 'float' in str(contain):
            scheme_df.append(' '.join([name, 'REAL']))

        else:
            scheme_df.append(' '.join([name, 'TEXT']))

    scheme_df = ', '.join(scheme_df)

    return scheme_df, new_names


def bid_DB(genstudio, metadata, scheme_genstudio, scheme_metadata, path='./data/bid_DB.db'):
    '''
    Create SQL scheme from `.scv` files
    '''

    connection = sqlite3.connect(path)

    connection.execute('''CREATE TABLE IF NOT EXISTS SNP_AG_data (
                          Sample_ID TEXT,
                          SNP_Name TEXT,
                          SNP TEXT,
                          Position TEXT,
                          Chr TEXT,
                          sex TEXT)''')

    connection.execute(f'''CREATE TABLE IF NOT EXISTS metadata ({scheme_metadata},
                           FOREIGN KEY (sex) REFERENCES SNP_data (sex))''')

    connection.execute(f'''CREATE TABLE IF NOT EXISTS genstudio ({scheme_genstudio},
                           FOREIGN KEY (Sample_ID) REFERENCES metadata (dna_chip_id),
                           FOREIGN KEY (Sample_ID) REFERENCES metadata (Sample_ID),
                           FOREIGN KEY (SNP_Name) REFERENCES metadata (SNP_Name),
                           FOREIGN KEY (SNP) REFERENCES metadata (SNP),
                           FOREIGN KEY (Position) REFERENCES metadata (Position),
                           FOREIGN KEY (Chr) REFERENCES metadata (Chr))''')

    connection.commit()

    genstudio.to_sql('genstudio', connection, if_exists='append', index=False)
    metadata.to_sql('metadata', connection, if_exists='append', index=False)

    connection.close()


def get_genes():
    '''
    Get Human Gene names from genomics.senescence.info.
    Return list with names.
    '''
    GENE_URL = 'https://genomics.senescence.info/genes/allgenes.php'

    resp = requests.get(GENE_URL)
    soup = BeautifulSoup(resp.content, 'lxml')

    genes_list = []

    table = soup.find("table", {"class": "results-table"})
    rows = table.find_all('tr')

    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]

        if cols:
            genes_list.append(cols[0])

    return genes_list


def snp_search(gene_name):
    '''
    Search first 20 SNP in ncbi snp database. Return soup object.
    '''
    SNP_URL = 'https://www.ncbi.nlm.nih.gov/snp/'
    query_str = {'term': gene_name + '[Gene Name]'}

    resp = requests.get(SNP_URL, params=query_str)
    soup = BeautifulSoup(resp.content, 'lxml')

    return soup


def parse_soup(soup):
    '''
    Extract SNP ID from soup.
    Return list with rs-id.
    '''
    rs_id = []

    for result in soup.find_all('div', {'class': 'rprt'}):
        rs_id.append(result.find('div', {'class': 'supp'}).find('a').text)

    return rs_id


def get_id_list(genes_list):
    '''
    Search first 20 SNP in ncbi snp database and extract SNP ID from soup.
    Wait 5 seconds between get requests.
    Return lists with SNP ID`s for all genes.
    '''
    id_list = []

    for gene_name in genes_list:
        time.sleep(5)

        soup = snp_search(str(gene_name))
        rs_id = parse_soup(soup)

        if rs_id:
            id_list.append(rs_id)

    return id_list


def add_to_sql(snp_name, position, chromosome, alleles, db_build, assembly_build,
               clin_sig, n_publications):
    '''
    Open connection to SNP_human DB, add some info to it and close connection.
    Return nothing.
    '''
    connection = sqlite3.connect('./data/SNP_human.db')

    query_1 = '''INSERT INTO SNP_data (SNP_Name, Alleles, Position, Chr, dbSNP_Build, Assembly_Build)
                                       VALUES (?, ?, ?, ?, ?, ?)'''

    connection.execute(query_1, [snp_name, alleles, position, chromosome, db_build, assembly_build])

    query_2 = '''INSERT INTO clin_SNP (SNP_Name, Clinical_Significance, N_Publications)
                                       VALUES (?, ?, ?)'''

    connection.execute(query_2, [snp_name, clin_sig, n_publications])

    connection.commit()
    connection.close()


def get_snp_soup(req_url):
    '''
    Get info about SNP from URL.
    Wait 10 seconds between get requests.
    '''
    time.sleep(10)
    
    with requests.Session() as s:
        resp = s.get(req_url, params={'horizontal_tab': 'true'})
        soup = BeautifulSoup(resp.content, 'lxml')
        
    return soup


def get_snp_info(red_id_list):
    '''
    Get info about SNP from soup object and add it to the SQL DB.
    Return 'DONE' when done.
    '''
    for snp_name in red_id_list:

        req_url = f'https://www.ncbi.nlm.nih.gov/snp/{snp_name}'
        soup =  get_snp_soup(req_url)

        db_build = soup.find('div', {'class': 'accession usa-width-one-third'}).text.split()[2]

        snp_info = soup.find_all('dl', {'class': 'usa-width-one-half'})
        dd_info = snp_info[0].find_all('dd')
        build_chr_pos = dd_info[1].find_all('span')

        assembly_build = build_chr_pos[1].text.strip()
        position = build_chr_pos[0].text.split(':')[1]
        chromosome = build_chr_pos[0].text.split(':')[0]

        alleles = ''.join(dd_info[2].text.split())

        clin_sig = snp_info[1].find('dd').text.strip()

        publ_info = snp_info[1].find('a', {'id': 'snp_pub_count'})

        if publ_info:
            n_publications = publ_info.text.split()[0]
        else:
            n_publications = 'no info'

        add_to_sql(snp_name,
                   position,
                   chromosome,
                   alleles,
                   db_build,
                   assembly_build,
                   clin_sig,
                   n_publications)

    return 'DONE'


def create_SNP_db():
    '''
    Create DB with two tables with info about human genes SNP.
    Gets information about the name of human genes from the "genomics.senescence.info" site.
    When searching for SNPs for each gene in SNP NCBI, returns no more than 20 SNPs.
    Write found SNPs to the SNP_ids.txt file.
    Search info about each SNP in SNP NCBI.
    Add info about found SNPs to SNP_human.db.
    Return DONE when done.
    '''

    connection = sqlite3.connect('./data/SNP_human.db')

    connection.execute('''CREATE TABLE IF NOT EXISTS SNP_data (
                           SNP_Name TEXT PRIMARY KEY,
                           Alleles TEXT,
                           Position TEXT,
                           Chr TEXT,
                           dbSNP_Build TEXT,
                           Assembly_Build TEXT)''')

    connection.execute('''CREATE TABLE IF NOT EXISTS clin_SNP (
                           SNP_Name TEXT,
                           Clinical_Significance TEXT,
                           N_Publications TEXT,
                           FOREIGN KEY (SNP_Name) REFERENCES SNP_data (SNP_Name))''')

    connection.commit()
    connection.close()

    # Done in file
    '''
    genes_list = get_genes()

    id_list = get_id_list(genes_list)
    red_id_list = list(set([j for sub in id_list for j in sub]))

    with open('./data/SNP_ids.txt', 'w') as output_file:
        for rsid in red_id_list:
            output_file.write(rsid + '\n')
    '''

    with open('./data/SNP_ids.txt') as f:
        red_id_list = f.read().splitlines()

    return get_snp_info(red_id_list)


if __name__ == '__main__':

    # Create sql from csv:
    genstudio = pd.read_csv('./data/genstudio.csv', dtype={'Position': str})
    metadata = pd.read_csv('./data/metadata.csv')
    # print(genstudio.shape, metadata.shape)

    # Create SQL scheme
    scheme_genstudio, new_names = get_scheme_df(genstudio)
    genstudio.columns = new_names

    scheme_metadata, new_names = get_scheme_df(metadata)
    metadata.columns = new_names

    # Create SQL DB and add data from pandas
    path = './data/bid_DB.db'
    bid_DB(genstudio, metadata, scheme_genstudio, scheme_metadata, path)

    # Select from SQL DB
    connection = sqlite3.connect('./data/bid_DB.db')

    query = '''SELECT Sample_ID, SNP, Chr
            FROM genstudio
            WHERE SNP = '[A/G]'
    '''

    res = connection.execute(query)
    print(len(res.fetchall()))
    connection.close()

    # Add selection to DB
    connection = sqlite3.connect('./data/bid_DB.db')

    query = '''INSERT INTO SNP_AG_data (Sample_ID, SNP_Name, SNP, Position, Chr, sex)
    SELECT DISTINCT genstudio.Sample_ID, genstudio.SNP_Name, genstudio.SNP, genstudio.Position, genstudio.Chr,
    metadata.sex
    FROM genstudio, metadata
    WHERE metadata.dna_chip_id = genstudio.Sample_ID AND genstudio.SNP = '[A/G]'''

    connection.execute(query)
    connection.commit()
    connection.close()

    # Second part
    # Create and add from web
    create_SNP_db()

    # SNP DB select

    # Select clinic with publications
    connection = sqlite3.connect('./data/SNP_human.db')

    query = '''SELECT SNP_data.SNP_Name, SNP_data.Chr, SNP_data.Position, SNP_data.Alleles
            FROM SNP_data
            LEFT JOIN clin_SNP ON SNP_data.SNP_Name = clin_SNP.SNP_Name
            WHERE clin_SNP.Clinical_Significance = 'Reported in ClinVar' AND clin_SNP.N_Publications != '0'
    '''

    res = connection.execute(query)
    result = res.fetchall()
    connection.close()

    print(f'Select Clin SNP:\n{result}')

    # count SNP for chromosome, select only counts between 2 and 20
    connection = sqlite3.connect('./data/SNP_human.db')

    query = '''SELECT Chr, COUNT(SNP_Name)
            FROM SNP_data
            GROUP BY Chr
            HAVING COUNT(SNP_Name) BETWEEN 2 AND 20
    '''

    res = connection.execute(query)
    result = res.fetchall()
    connection.close()
    print(f'ANP in Chr:\n{result}')

    # delete from tables Not Reported in ClinVar rows
    connection = sqlite3.connect('./data/SNP_human.db')

    query = '''BEGIN TRANSACTION;

               DELETE FROM SNP_data
               WHERE SNP_data.SNP_Name in (
               SELECT SNP_Name FROM clin_SNP WHERE clin_SNP.Clinical_Significance = "Not Reported in ClinVar");

               DELETE FROM clin_SNP
               WHERE clin_SNP.Clinical_Significance = "Not Reported in ClinVar";

               COMMIT'''

    connection.executescript(query)
    connection.close()

    connection = sqlite3.connect('./data/SNP_human.db')

    query = '''SELECT Chr, COUNT(SNP_Name)
            FROM SNP_data
            GROUP BY Chr
            HAVING COUNT(SNP_Name) BETWEEN 20 AND 50
    '''

    res = connection.execute(query)
    result = res.fetchall()
    connection.close()
    print(result)
