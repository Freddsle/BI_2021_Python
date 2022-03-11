# Tool for tblasn search in wgs database.
import urllib3
import requests
import time
import re

from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs

import pandas as pd


class Alignment():

    def __init__(self,
                 subj_name, subj_id, subj_len, subj_range,
                 score, e_value, identity,
                 query_seq, subj_seq):
        '''
        Создает объект класса Alignment со следующими атрибутами:
        self.score
        self.subj_range    # tuple
        self.subj_name
        self.subj_id
        self.subj_len
        self.e_value
        self.identity
        self.query_seq
        self.subj_seq
        '''

        self.score = score
        self.subj_range  = subj_range   # tuple
        self.subj_name = subj_name
        self.subj_id = subj_id
        self.subj_len = subj_len
        self.e_value = e_value
        self.identity = identity
        self.query_seq = query_seq
        self.subj_seq = subj_seq


    def __str__(self):
        return ': '.join([self.subj_id, self.score])


def RID_request(BLAST_URL, fasta, database, taxon, file=''):
    '''
    Send information about seqrch to tblasn server. Starts search.
    '''
    payload = {
        'QUERY': fasta,
        'db': 'protein',
        'QUERYFILE': '',  # use for binary files
        'GENETIC_CODE': 1,
        'JOB_TITLE': 'fasta',
        'ADV_VIEW': 'true',
        'stype': 'nucleotide',
        #'SUBJECTFILE': '', # use for binary files
        'DATABASE': 'Whole_Genome_Shotgun_contigs',
        'DB_GROUP': 'wgsOrg',
        #'EQ_MENU': 'Prevotella sp. oral taxon 472 str. F0295 (taxid:619693)',  # работает если передавать полное название из выпадающего списка
        'EQ_MENU': '619693',    # работает и просто при передаче самого айдишника
        #'EQ_MENU': 'Prevotella sp. oral taxon 472 str. F0295',    # а так не работает
        'NUM_ORG': 1,
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

    prev_time = time.time()

    resp = requests.post(BLAST_URL, data=payload)
    soup = BeautifulSoup(resp.content, 'lxml')

    s_code = resp.status_code
    RID = soup.find('input', {'name': 'RID'}).get('value')

    return prev_time, s_code, RID


def check_results(prev_time, RID, BLAST_URL):
    '''
    Makes requests to the tblasn server until a result is received.
    Stop when it takes more than 15 minutes and print RID for manual check on the website.
    '''

    payload = {
        'CMD': 'Get',
        'RID': RID,
        'FORMAT_TYPE': 'HTML'
    }

    delay = 10
    wait = 10
    i = 0

    while True:

        current_time = time.time()
        wait = prev_time + delay - current_time

        if wait > 0:
            time.sleep(wait)
            prev_time = current_time + wait
    
        if i * delay >= 900:
            print(f'Oops! Try to check your resalts later (or restart). RID: {RID}.')

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
            if not soup.find('table', {'id': 'statInfo'}):

                if resp.status_code != 500:
                    print(f'status code: {resp.status_code}, SEARCH DONE.')
                    break

                else:
                    continue

    return soup, current_time


def get_seq_list(soup):
    seq_list = []

    for line in soup.find_all('form', attrs={"id": "formBlastDescr"})[0].find_all('input', attrs={'type': 'checkbox'}):
        seq_list.append('gb|' + re.sub('Select seq ', '', line.next_sibling.text).split('.')[0] +'|')

    return seq_list


def get_algnmt(RID, seq_list, prev_time):

    FASTA_URL = 'https://blast.ncbi.nlm.nih.gov/t2g.cgi'
    align_seq_list = ','.join(seq_list)

    params = {
        'CMD': 'Get',
        'RID': RID,
        #'DESCRIPTIONS': 0,
        #'NUM_OVERVIEW': 0,
        'GET_SEQUENCE': 'on',
        'DYNAMIC_FORMAT': 'on',
        'ALIGN_SEQ_LIST': align_seq_list,
        #'HSP_SORT': 0,
        'SEQ_LIST_START': 1,
        'QUERY_INDEX': 0,
        'ADV_VIEW': 'on',
        'SHOW_LINKOUT': 'on',
        #'MASK_CHAR': 2,
        #'MASK_COLOR': 1,
        'ALIGNMENT_VIEW': 'Pairwise',
        'LINE_LENGTH': 60,
        'BOBJSRVC': 'sra'
        }

    delay = 10
    wait = 10

    i = 0

    while True:

        current_time = time.time()
        wait = prev_time + delay - current_time

        if wait > 0:
            time.sleep(wait)
            prev_time = current_time + wait

        if i * delay >= 900:
            print(f'Oops! Try to check your resalts later (or restart). RID: {RID}.')

        else:
            prev_time = current_time

        resp = requests.get(FASTA_URL, params=params)

        if resp.status_code == 500:
            print('Please, wait. Something with BLAST server.')
            continue

        soup = BeautifulSoup(resp.content, 'lxml')

        return soup


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

            table_params = align.find_all('table', {'class' : "alnParams"})
            nember_al = len(table_params)
            urls = align.find_all('a', {'class' : ""}, href=True)

            sequences = align.find_all('pre')

            for i in range(nember_al):
                parsed_url = urlparse(urls[i]['href'])

                scores_list = pd.read_html(str(table_params[i]))
                df_scores = scores_list[0]

                score = df_scores['Score'][0]
                identity = df_scores['Identities'][0]
                e_value =  df_scores['Expect'][0]

                # more
                #method = df_scores['Method'][0]
                #positives = df_scores['Positives'][0]
                #gaps = df_scores['Gaps'][0]
                #frame = df_scores['Frame'][0]

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

    return  alignments_list


def get_alignments(fasta, database, taxon):
    BLAST_URL = "https://blast.ncbi.nlm.nih.gov/Blast.cgi"

    seq_number = len(fasta.strip('>').split('>'))

    #for i in range(seq_number):

    prev_time, s_code, RID = RID_request(BLAST_URL, fasta, database, taxon)

    if s_code != 200:
        print('Something wrong with request!')
        return

    soup, prev_time = check_results(prev_time, RID, BLAST_URL)

    seq_list = get_seq_list(soup)

    algnmt_soup = get_algnmt(RID, seq_list, prev_time)

    alignments_list = get_results_algnmnt(algnmt_soup)

    return alignments_list


def main(fasta, database, taxon):
    #get_alignments(fasta, database, taxon)
    pass

if __name__ == '__main__': 

    # example protein sequences
    fasta = \
    """>sf
MVMFGNKVSYPYMDLSPKSHWIVYEGNLKFYDKQGRDTASIK
DAASLSFDFFTWGRNPKVAMIETTEVSKLSVESFKSTCYGYIICSYT
>line2
MVMFGNKVSYPYMDLSPKSHWIVYEGNLKFYDKQGRDTASIKDAASLSFDFFTWGRNPKVAMIETTE
>line3
RNPKVAMIETTEVSKLSVESFKSTCYGYIICSYT
>line4
FTWGRNPKVAMIETTEPYMDLRNPKVAMLSFDFFTWGRNPKVAMIETTE
>line5
ETTEVSKLSVESFKSTCYGYIICSYTYMDLRNPKVAMLSFDFFTWGRNPKVAMIETTIICSYTYMDL
RNPEIKDAASLSFDFFTWGRNPKVAMIETTEVSKLSVESFKSTCYGYIICSYT"""

    # example database - wgs (now works only with this DB)
    database = 'Whole_Genome_Shotgun_contigs'

    # example taxon - only taxid and full names (like in web tblastn form) accepted
    taxon = '619693'

    # run search
    alignments_list = get_alignments(fasta, database, taxon)

    for i in alignments_list:
        print(i, '\t', i.identity, '\t',  i.e_value)
