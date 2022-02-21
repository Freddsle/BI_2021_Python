# Practice with Pandas library

## Task 1. Plot hists.
df contains information about the number of reads with each of the 4 nucleotides at different positions (columns A, T, G, C). Plot a histogram of the distribution of these numbers.

Resultuing plot in `./data/task_1_hist.png`.

## Task 2. Select data.

Write to the file `train_part.csv` some parts of the `train.csv` (from prev task):
1. Strings where matches bigger than mean;
2. Cols 'pos', 'reads_all', 'mismatches', 'deletions', 'insertions'

Resulting DataFrame in `./data/train_part.csv`.

## Task 3. Small EDA 

[Vine Data](https://www.kaggle.com/yasserh/wine-quality-dataset) or `./data/WineQT.csv`.

EDA of DataFrame of Vine Data: correlation plot, distribution plots, EDA with pandas_profiling.

Results in `./data/correlation_01.png`, `./data/correlation_02.png`, `./data/Scatter/`, `./data/Histogram/`, `./data/Boxplot/`, and .html report created with pandas_profiling library in `./data/EDA_report.html`.

## Task 4. Work with bioinf data

- `rrna_annotation.gff` - annotation of ribosomal RNA.
- `alignment.bed` - file with metagenomic assembly alignment to the same dataset. 

### 4.1. read_gff and read_bed6
Functions `read_gff()` and `read_bed6()` for read .gff and .bed6 files.

Returns Pandas DataFrame.

### 4.2. Truncate attributes column

Truncate attributes column - leave only info about RNA type (16S, 23S, 5S).

### 4.3. Count RNA types for each chr

Count RNA types for each "chromosome" and plot barplot (`./data/attributes_barhplot.png`).

### 4.4. Pandas as bedtools intersect

We want to know how much rRNA was successfully assembled during the assembly process. 

Creates a DataFrame containing initial records about rRNA completely included in the assembly (not a fragment), as well as a record about the contig in which this RNA got.


# Install and run with pip
## Installation

```console
git clone https://github.com/Freddsle/BI_2021_Python
cd ./BI_2021_Python/python_homework/pandas_practice

# Create and activate your virtual environment

# create virtual environment
python3.10 -m venv ./venv

# activate virtual environment
source ./venv/bin/activate

# if you install it not from main or master, change branch
git checkout practice_pandas

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
cd ./BI_2021_Python/python_homework/pandas_practice

# if you install it not from main or master, change branch
git checkout practice_pandas

poetry env use python3.10
poetry install

# Run
poetry run python ppractice.py

# or for run .ipynb files
poetry run jupyter notebook
```