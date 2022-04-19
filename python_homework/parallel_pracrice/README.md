
# Parallel counter

Command line tool. Read FASTA file record by record and run `symbol_counter` func for each record in multiprocessing mode. Print number of each character in record string.

Also can be imported as module (`parallel_counter` from `parallel_pracrice.py`)

You can set `-t` or `--threads` parameter to some number. ProcessPoolExecutor is used for work in multiprocessing mode.

## Example run

You can test the tool with human genome FASTA file (you can dowload `fna.gz` file from [link](https://ftp.ncbi.nlm.nih.gov/refseq/H_sapiens/annotation/GRCh38_latest/refseq_identifiers/GRCh38_latest_genomic.fna.gz)).

Unpack it ().

Test run:
```console
time poetry run python parallel_pracrice.py -i GRCh38_latest_genomic.fna -t 2
```

Example run time:
- with t=1 - real: 11m34,085s
- with t=2 - real: 6m52,060s
- with t=4 - real: 4m17,901s


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
cd ./BI_2021_Python/python_homework/parallel_pracrice/

# if you install it not from main or master, change branch
git checkout parallel_pracrice

poetry env use python3.10
poetry install

# Run
poetry run python parallel_pracrice.py

```