# Tool for tblasn search in wgs database.
import urllib3
import requests
import time
import re

from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs

import pandas as pd


class Alignment():
    '''
    Class for creation and store Alignments from tblasn Alignment output.
    '''

    def __init__(self,
                 subj_name, subj_id, subj_len, subj_range,
                 score, e_value, identity,
                 query_seq, subj_seq):
        '''
        Create Alignment object with the following attributes:
        score: alignment score (string);
        subj_range: (tuple);
        subj_name: subject sequence name (string);
        subj_id: subject sequence GenBank ID (ACCESSION, string);
        subj_len: subject sequence full length (int);
        e_value: alignment e_value (string);
        identity: identity between query seq and subject (string), identical letters/alignment length (identity %);
        query_seq: query string in pairwise alignment format (with gaps);
        subj_seq: subject in pairwise alignment format (with gaps).
        '''

        self.score = score
        self.subj_range = subj_range   # tuple
        self.subj_name = subj_name
        self.subj_id = subj_id
        self.subj_len = subj_len
        self.e_value = e_value
        self.identity = identity
        self.query_seq = query_seq
        self.subj_seq = subj_seq

    def __str__(self):
        '''
        When printing alignment object - print subj_id and score of alignment.
        '''
        return ': '.join([self.subj_id, self.score])


def taxid_search(input_taxids):
    '''
    Searches the database for an taxid (from list), returns the first match.
    If the database is searched for by taxid (i.e. only numbers were used for the search)
    and such taxid does not exist,
    then no blast is performed for this taxid (taxid will not be added to the blast).
    Return the list with taxid`s.
    '''
    TAXID_URL = 'https://blast.ncbi.nlm.nih.gov/portal/utils/autocomp.fcgi'
    taxid_list = []

    for taxid in input_taxids:

        query_str = {
            'dict': 'bdb_wgs_all_sg',
            'q': taxid
        }

        resp = requests.get(TAXID_URL, params=query_str)
        soup = BeautifulSoup(resp.content, 'lxml')

        first_taxid = re.search(r'(?<=taxid:).+(?=\)\@)', soup.text.split(', ')[1]).group(0)

        if len(first_taxid) >= len(taxid) and str.isdecimal(taxid):
            taxid_list.append(first_taxid)

    return taxid_list


def RID_request(BLAST_URL, fasta, database, taxon):
    '''
    Send search (payload) to tblasn server. Starts search.
    Input 'taxon' should be in list format (list contains strings or string).
    The search is performed with standard parameters in the wgs database when specifying an organism.
    Exclusion of an organism (taksaidi) from the search is not yet provided.
    Return status code, the time the request was sent, and RID - Request ID.
    '''

    payload = {
        'QUERY': fasta,
        'db': 'protein',
        'GENETIC_CODE': 1,
        'JOB_TITLE': 'fasta',
        'ADV_VIEW': 'true',
        'stype': 'nucleotide',
        # 'EQ_MENU' - add in range later
        'DATABASE': database,
        'DB_GROUP': 'wgsOrg',
        'NUM_ORG': len(taxon),
        'MAX_NUM_SEQ': 100,
        'EXPECT': 0.05,
        'WORD_SIZE': 6,
        'HSP_RANGE_MAX': 0,
        'MATRIX_NAME': 'BLOSUM62',
        'MATCH_SCORES': [1, -2],
        'GAPCOSTS': '11 1',
        'COMPOSITION_BASED_STATISTICS': 2,
        'FILTER': 'L',
        'REPEATS': 566037,
        'GET_SEQUENCE': 'true',
        'FORMAT_OBJECT': 'Alignment',
        'FORMAT_TYPE': 'HTML',
        'ALIGNMENT_VIEW': 'Pairwise',
        'DESCRIPTIONS': 100,
        'ALIGNMENTS': 100,
        'NCBI_GI': 'false',
        'SHOW_CDS_FEATURE': 'false',
        'CONFIG_DESCR': '2,3,4,5,8,9,10,11,12,13,14',
        'CLIENT': 'web',
        'SERVICE': 'plain',
        'CMD': 'request',
        'PAGE': 'Translations',
        'PROGRAM': 'tblastn',
        'UNGAPPED_ALIGNMENT': 'no',
        'BLAST_PROGRAMS': 'tblastn',
        'DB_DISPLAY_NAME': 'wgs',
        'ORG_DBS': 'orgDbsOnly_wgs',
        'SHOW_ORGANISMS': 'on',
        'SELECTED_PROG_TYPE': 'tblastn',
        'SAVED_SEARCH': 'true',
        'NUM_DIFFS': 1,
        'NUM_OPTS_DIFFS': 0,
        'PAGE_TYPE': 'BlastSearch'
    }

    # add taxons to payload:
    for i, tax_id in enumerate(taxon):
        if i == 0:
            payload['EQ_MENU'] = tax_id
        else:
            payload['EQ_MENU'+str(i)] = tax_id

    current_time = time.time()

    resp = requests.post(BLAST_URL, data=payload)
    soup = BeautifulSoup(resp.content, 'lxml')

    s_code = resp.status_code
    RID = soup.find('input', {'name': 'RID'}).get('value')

    return current_time, s_code, RID


def check_results(prev_time, RID, BLAST_URL, num_query):
    '''
    Requests to the tblasn server until a result is received.
    Errors are used to check for the existence of a result.
    Also requests will continue if the server response tatus code is 500.
    When the search is complete, displays a message containing the status code value.
    Return soup object and the time whrn the last request was sent.
    '''

    payload = {
        'CMD': 'Get',
        'RID': RID,
        'FORMAT_TYPE': 'HTML',
        'QUERY_INDEX': num_query,
    }

    delay = 10
    wait = 0
    i = 0

    while True:

        current_time = time.time()
        wait = prev_time + delay - current_time

        if wait > 0:
            time.sleep(wait)

        else:
            prev_time = current_time

            try:
                resp = requests.post(BLAST_URL, data=payload)
                soup = BeautifulSoup(resp.content, 'lxml')

            except (ValueError,
                    urllib3.exceptions.InvalidChunkLength,
                    urllib3.exceptions.ProtocolError,
                    requests.exceptions.ChunkedEncodingError):

                print('Please wait. Searching.')
                i += 1
                continue

            else:
                if not soup.find('table', {'id': 'statInfo'}) and resp.status_code != 500:

                    if num_query == 0:
                        print(f'status code: {resp.status_code}, SEARCH DONE.')

                    break

                else:
                    print('Please wait. Searching.')
                    i += 1
                    continue

    return soup, current_time


def get_seq_list(soup):
    seq_list = []

    for line in soup.find_all('form', attrs={"id": "formBlastDescr"})[0].find_all('input', attrs={'type': 'checkbox'}):
        seq_list.append('gb|' + re.sub('Select seq ', '', line.next_sibling.text).split('.')[0] + '|')

    return seq_list


def get_algnmt(RID, seq_list, prev_time, num_query):

    FASTA_URL = 'https://blast.ncbi.nlm.nih.gov/t2g.cgi'
    align_seq_list = ','.join(seq_list)

    params = {
        'CMD': 'Get',
        'RID': RID,
        'GET_SEQUENCE': 'on',
        'DYNAMIC_FORMAT': 'on',
        'ALIGN_SEQ_LIST': align_seq_list,
        'SEQ_LIST_START': 1,
        'QUERY_INDEX': num_query,
        'ADV_VIEW': 'on',
        'SHOW_LINKOUT': 'on',
        'ALIGNMENT_VIEW': 'Pairwise',
        'LINE_LENGTH': 60,
        'BOBJSRVC': 'sra'
        }

    # wait 3 sec between downloading results
    wait = 1
    delay = 5

    while True:

        current_time = time.time()
        wait = prev_time + delay - current_time

        if wait > 0:
            time.sleep(wait)

        else:
            prev_time = current_time

        resp = requests.get(FASTA_URL, params=params)

        if resp.status_code == 500:
            print('Please, wait. Something with BLAST server.')
            continue

        elif resp.status_code == 200:
            break

    soup = BeautifulSoup(resp.content, 'lxml')

    return soup, prev_time


def get_results_algnmnt(soup):

    result = soup.find_all('div', {'class': 'oneSeqAln'})
    alignments_list = []

    for element in result:

        id_name = element.find('div', {'class': 'dlfRow'})

        subj_name = id_name.text.strip().split('\n')[0]
        subj_len = int(element.find("label", text="Length: ").next_sibling.text)
        subj_id = id_name.find('a').text

        alignments = element.find_all('div', {'class': 'alnAll'})

        for align in alignments:

            table_params = align.find_all('table', {'class': "alnParams"})
            nember_al = len(table_params)
            urls = align.find_all('a', {'class': ""}, href=True)

            sequences = align.find_all('pre')

            for i in range(nember_al):
                parsed_url = urlparse(urls[i]['href'])

                scores_list = pd.read_html(str(table_params[i]))
                df_scores = scores_list[0]

                score = df_scores['Score'][0]
                identity = df_scores['Identities'][0]
                e_value = df_scores['Expect'][0]

                # more
                # method = df_scores['Method'][0]
                # positives = df_scores['Positives'][0]
                # gaps = df_scores['Gaps'][0]
                # frame = df_scores['Frame'][0]

                value_from = int(parse_qs(parsed_url.query)['from'][0])
                value_to = int(parse_qs(parsed_url.query)['to'][0])
                subj_range = tuple([value_from, value_to])

                query_seq = []
                subj_seq = []

                al = sequences[i].text.strip().split('\n')

                for j, line in enumerate(al):
                    line = line.split()
                    if 'Query' in line:
                        query_seq.append(line[2])

                    elif 'Sbjct' in line:
                        subj_seq.append(line[2])

                query_seq = ''.join(query_seq)
                subj_seq = ''.join(subj_seq)

                alignments_list.append(Alignment(subj_name=subj_name,
                                                 subj_id=subj_id,
                                                 subj_len=subj_len,
                                                 subj_range=subj_range,
                                                 score=score,
                                                 e_value=e_value,
                                                 identity=identity,
                                                 query_seq=query_seq,
                                                 subj_seq=subj_seq))

    return alignments_list


def taxid_prepare(taxon, search_taxid=False):

    if search_taxid:
        taxon = taxid_search([taxon])

    elif isinstance(taxon, str):
        taxon = [taxon]

    return taxon


def get_alignments(fasta, database, taxon, search_taxid=False, input_file=True):
    '''
    ...
    Several amino acid sequences can be included in one search (one file)
    if their total length is up to 1,000 amino acids.
    Otherwise, one lookup per sequence. The length of the sequence is limited by the size of the memory
    (because the file is opened and the sequence is passed as a string).

    You can pass not the path to the file, but a string - in this case set input_file=False.

    At the moment, "exclusion" of organisms is not supported.

    If input taxon not in taxid format (only numers) - search_taxid taxid=True.
    If search_taxid=False, an additional search will be performed to extract the full name of the taxon
    (only the first match will be used - as when selecting from the drop-down list in
    the web version of tblastn).
    If no significant similarity found - return the empty list.
    '''
    BLAST_URL = "https://blast.ncbi.nlm.nih.gov/Blast.cgi"

    alignments_list = []
    taxon = taxid_prepare(taxon, search_taxid)

    if input_file:
        with open(fasta, 'r') as f:
            fasta = f.read()

    seq_number = len(fasta.strip('>').split('>'))

    prev_time, s_code, RID = RID_request(BLAST_URL, fasta, database, taxon)
    print(f' RID: {RID}')

    if s_code != 200:
        print('Something wrong with request!')
        return

    for num_query in range(seq_number):

        soup, prev_time = check_results(prev_time, RID, BLAST_URL, num_query)

        seq_list = get_seq_list(soup)

        algnmt_soup, prev_time = get_algnmt(RID, seq_list, prev_time, num_query)

        if seq_number == 1:
            alignments_list = get_results_algnmnt(algnmt_soup)

        elif seq_number > 1:
            alignments_list.append(get_results_algnmnt(algnmt_soup))

    return alignments_list


def main(fasta, database, taxon):
    # get_alignments(fasta, database, taxon)
    pass


if __name__ == '__main__':

    # path to example protein sequences
    fasta = './example.fa'

    # example database - wgs (now works only with this DB)
    database = 'Whole_Genome_Shotgun_contigs'

    # example taxon - only taxid and full names (like in web tblastn form) accepted
    # if multiple - should be in list.
    taxon = '619693'    # results exists
    # taxon = ['6179', '296']   # results doesnt exists

    # run search
    alignments_list = get_alignments(fasta, database, taxon, search_taxid=True, input_file=True)
    
    # example output
    print('Example output (part):')

    if not alignments_list:
        print('No significant similarity found for all sequences.')

    else:

        for i, result in enumerate(alignments_list):

            if not result:
                print(f'No significant similarity found for {i} sequence.')

            elif len(alignments_list) == 1:
                print(result, '\t', result.identity, '\t', result.e_value)

            else:
                for j in result:
                    print(j, '\t', j.identity, '\t', j.e_value)

            print('-----')
