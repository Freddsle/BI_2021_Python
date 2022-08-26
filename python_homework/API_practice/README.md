
# API function for tblasn WGS search

With example run in ` if __name__ == "__main__"`.

The delay between calls to the server is 10 seconds. 

## Contains:

1. **class Alignment** - Class for creation and store Alignments from tblasn Alignment output.

    Create Alignment object with the following attributes:
        - score: alignment score (string);
        - subj_range: (tuple);
        - subj_name: subject sequence name (string);
        - subj_id: subject sequence GenBank ID (ACCESSION, string);
        - subj_len: subject sequence full length (int);
        - e_value: alignment e_value (string);
        - identity: identity between query seq and subject (string), identical letters/alignment length (identity %);
        - query_seq: query string in pairwise alignment format (with gaps);
        - subj_seq: subject in pairwise alignment format (with gaps).

    When printing alignment object - print subj_id and score of alignment.


Functions:

1. **get_alignments** function - main function.

    The function that searches the tblastn database by the specified parameters (fasta, database, taxon),
    all other parameters are used by default.

    Several amino acid sequences can be included in one search (one file), 
    if their total length is up to 1,000 amino acids.
    Otherwise, one lookup per sequence. The length of the sequence is limited by the size of the memory
    (because the file is opened and the sequence is passed as a string).

    You can pass not only the path to the file, but a string - in this case set input_file=False.

    At the moment, "exclusion" of organisms is not supported.
    But the search can be done using several organisms (taxid`s).

    If input taxon not in taxid format (in taxid only numbers are allowed) - set the search_taxid=True.
    If search_taxid=True, an additional search will be performed to extract the full taxid of taxon
    (only the first match will be used - as when selecting from the drop-down list in the web tblastn).

    Return list with Alignment objects for one fasta sequence.
    If multiple sequences were passed, returns a list of lists of Alignment objects.  
    If no significant similarity found - return the empty list.


2. **taxid_search** function. 

    Searches the database for an taxid (from list), returns the first match.\
    If the database is searched for by taxid (i.e. only numbers were used for the search) and such taxid does not exist, then no blast is performed for this taxid (taxid will not be added to the blast).

    Return the list with taxid`s.
  
3. **taxid_prepare** function.
    If set search_taxid=True, passes the list of taxons to the taxid_search function to find the first best match.\
    If set search_taxid=False, check if taxon is string, if so - wraps a string into a list.

    Returns a list with taxid`s.


3. **RID_request** function.
    
    Send search (payload) to tblasn server. Starts search.\
    Input 'taxon' should be in list format (list contains strings or string).\
    The search is performed with standard parameters in the wgs database when specifying an organism.\
    Exclusion of an organism (taksaidi) from the search is not yet provided.\
    Return status code, the time the request was sent, and RID - Request ID.
    
4. **check_results** function.

    Requests to the tblasn server until a result is received.\    
    Errors (ValueError, urllib3.exceptions.InvalidChunkLength, urllib3.exceptions.ProtocolError, requests.exceptions.ChunkedEncodingError) are used to check for the existence of a result.\      
    Also requests will continue if the server response status code is 500.  
    When the search is complete, print a `DONE` message containing the status code value.
    
    Return soup object (for align_seq_list) and the time when the last request was sent.

5. **get_algnmt** function.

    Requests to the tblasn server (using ACCESSION ID) to get a page of results with alignments.\
    Uses an QUERY_INDEX to refer to a page with alignments based on the ordinal number of the searched sequence.

    Return soup object and the time when the last request was sent.

6. **get_results_algnmnt** function.
    
    Parses soup object with alignments results.\
    Create Alignment object with attributes from parsed result.\

    Returns list with Alignment objects.


# Install and run with pip
## Installation

```console
git clone https://github.com/Freddsle/BI_2021_Python
cd ./BI_2021_Python/python_homework/API_practice/

# Create and activate your virtual environment

# create virtual environment
python3.10 -m venv ./venv

# activate virtual environment
source ./venv/bin/activate

# if you install it not from main or master, change branch
git checkout practice_api

# required by pip to build wheels
pip install wheel==0.37.0 

# Install requirements
pip install -r ./requirements.txt
```

## Run file
```console
python3.10 project_api.py
```

# Install and run with poetry
```console
# install poetry
# for details look for https://python-poetry.org/docs/
sudo apt-get install curl
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3.10 -

# poetry will be accessible in current session
source $HOME/.poetry/env

# prepare project
git clone https://github.com/Freddsle/BI_2021_Python
cd ./BI_2021_Python/python_homework/API_practice/

# if you install it not from main or master, change branch
git checkout practice_api

poetry env use python3.10
poetry install

# Run
poetry run python project_api.py

```

# Example run

```
# path to example protein sequences
fasta = './example.fa'

# example database - wgs (now works only with this DB)
database = 'Whole_Genome_Shotgun_contigs'

# example taxon - only taxid and full names (like in web tblastn form) accepted for post request.
# if multiple - should be in list.
taxon = '619693'    # results exists
# taxon = ['6179', '296']   # results doesnt exists
```

## Example run output:
```
 RID: 2U4APSEX013
status code: 200, SEARCH DONE.
Example output (part):
ACZS01000003.1: 187 bits(474) 	 89/89(100%) 	 1e-57()
ACZS01000003.1: 34.7 bits(78) 	 18/41(44%) 	 4e-04()
ACZS01000174.1: 77.8 bits(190) 	 39/86(45%) 	 2e-19()
ACZS01000173.1: 75.5 bits(184) 	 40/87(46%) 	 2e-18()
ACZS01000173.1: 73.6 bits(179) 	 37/82(45%) 	 7e-18()
ACZS01000087.1: 47.4 bits(111) 	 21/34(62%) 	 1e-08()
-----
ACZS01000003.1: 143 bits(360) 	 67/67(100%) 	 1e-42()
ACZS01000173.1: 61.2 bits(147) 	 29/56(52%) 	 6e-14()
ACZS01000173.1: 55.8 bits(133) 	 26/54(48%) 	 5e-12()
ACZS01000174.1: 60.5 bits(145) 	 28/58(48%) 	 1e-13()
ACZS01000087.1: 47.4 bits(111) 	 21/33(64%) 	 4e-09()
-----
ACZS01000003.1: 71.6 bits(174) 	 34/34(100%) 	 3e-18()
ACZS01000003.1: 26.6 bits(57) 	 12/24(50%) 	 0.027()
ACZS01000174.1: 26.6 bits(57) 	 11/16(69%) 	 0.027()
-----
ACZS01000003.1: 49.3 bits(116) 	 22/24(92%) 	 5e-10()
ACZS01000003.1: 37.7 bits(86) 	 16/16(100%) 	 5e-06()
-----
ACZS01000003.1: 102 bits(253) 	 49/49(100%) 	 2e-27()
ACZS01000003.1: 53.9 bits(128) 	 26/26(100%) 	 2e-10()
ACZS01000003.1: 34.7 bits(78) 	 18/41(44%) 	 0.001()
ACZS01000173.1: 44.7 bits(104) 	 24/58(41%) 	 3e-07()
ACZS01000173.1: 38.5 bits(88) 	 21/50(42%) 	 3e-05()
ACZS01000174.1: 38.9 bits(89) 	 18/47(38%) 	 3e-05()
-----
```
