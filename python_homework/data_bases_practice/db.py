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

    connection = sqlite3.connect(path)

    connection.execute(f'''CREATE TABLE IF NOT EXISTS SNP_AG_data (
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


if __name__ == '__main__':

    # Create sql from csv:
    genstudio = pd.read_csv('./data/genstudio.csv', dtype={'Position':str})
    metadata = pd.read_csv('./data/metadata.csv')
    #print(genstudio.shape, metadata.shape)

    # Create SQL scheme
    scheme_genstudio, new_names = get_scheme_df(genstudio)
    genstudio.columns = new_names

    scheme_metadata, new_names = get_scheme_df(metadata)
    metadata.columns = new_names

    # Create SQL DB and add data from pandas
    path='./data/bid_DB.db'
    bid_DB(genstudio, metadata, scheme_genstudio, scheme_metadata, path)

    # Select from SQL DB
    connection = sqlite3.connect('./data/bid_DB.db')

    query = '''SELECT metadata.dna_chip_id, genstudio.SNP_Name, genstudio.SNP, genstudio.Position, genstudio.Chr, 
            metadata.sex
            FROM genstudio, metadata
            WHERE metadata.dna_chip_id = genstudio.Sample_ID AND genstudio.SNP = '[A/G]'
    '''

    res = connection.execute(query)
    print(len(res.fetchall()))
    connection.close()

    # Add selection to DB
    connection = sqlite3.connect('./data/bid_DB.db')

    query = '''INSERT INTO SNP_AG_data (Sample_ID, SNP_Name, SNP, Position, Chr, sex)
    SELECT genstudio.Sample_ID, genstudio.SNP_Name, genstudio.SNP, genstudio.Position, genstudio.Chr, 
    metadata.sex 
    FROM genstudio, metadata 
    WHERE metadata.dna_chip_id = genstudio.Sample_ID AND genstudio.SNP = '[A/G]'''

    connection.execute(query)
    connection.commit()
    connection.close()
