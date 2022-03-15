# Practise with SQLite in Python

1. Create SQL db from `.scv` files:

- get_scheme_df - Create SQL scheme from DataFrame colnames. Return SQL scheme and list with processed colnames.

- bid_DB - Create SQL DB from `.scv` files. Create one file with two tables. Return nothing.

`__if__` module contains SELECT example for this DB.


2. Create SQL DB with human SNP data from NCBI (It takes a very long time to download the result from NCBI (hours):

- get_genes - Get Human Gene names from [genomics.senescence.info](genomics.senescence.info). Return list with names.

- snp_search - Search first 20 SNP in ncbi snp database. Return soup object.

- parse_soup - Extract SNP ID from soup. Return list with rs-id.

- get_id_list - Search first 20 SNP in ncbi snp database and extract SNP ID from soup. Wait 5 seconds between get requests. Return lists with SNP ID`s for all genes.

- add_to_sql - Open connection to SNP_human DB, add some info to it and close connection. Return nothing.

- get_snp_info - Get info about SNP from soup object and add it to the SQL DB. Wait 5 seconds between get requests. Return 'DONE' when done.

- create_SNP_db - Create DB with two tables with info about human genes SNP. Gets information about the name of human genes from the "genomics.senescence.info" site. When searching for SNPs for each gene in SNP NCBI, returns no more than 20 SNPs.

    Write found SNPs to the SNP_ids.txt file. Search info about each SNP in SNP NCBI.Add info about found SNPs to SNP_human.db.
    
    Return DONE when done.

`__if__` module contains SELECT, GROUP BY, HAVING, LEFT JOIN, TRANSACTION, DELETE examples for this DB.


# Install and run with pip
## Installation

```console
git clone https://github.com/Freddsle/BI_2021_Python
cd ./BI_2021_Python/python_homework/data_bases_practice

# Create and activate your virtual environment

# create virtual environment
python3.10 -m venv ./venv

# activate virtual environment
source ./venv/bin/activate

# if you install it not from main or master, change branch
git checkout data_bases

# required by pip to build wheels
pip install wheel==0.37.0 

# Install requirements
pip install -r ./requirements.txt
```

## Run file
```console
python3.10 practice.py
```

# Install and run with poetry
```console
# install poetry
# for details look for https://python-poetry.org/docs/
sudo apt-get install curl
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3.10 -

# poetry will be accessible in current session
source $HOME/.poetry/env

# prepare project (if you have previously installed poetry - start here)
git clone https://github.com/Freddsle/BI_2021_Python
cd ./BI_2021_Python/python_homework/data_bases_practice

# if you install it not from main or master, change branch
git checkout data_bases

poetry env use python3.10
poetry install

# Run
poetry run python db.py

# or for run .ipynb files
poetry run jupyter notebook
```
