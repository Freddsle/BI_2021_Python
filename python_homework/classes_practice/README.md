# Practice with Python classes.

The `practice.py` and `practice.ipynb` contain same code.


# Contents

## `class Hamster`

Python Class that describes hamsters.\
For creation "hamster" object it is nedeed to know its name and age (in months). Optionally, one can specify the type of hamster (for example, Syrian or Chinese). Default "Not defined".

**Methods**:
- `life_stage` - returns the age of a hamster: young, adult or old.
- `is_active` - checks if the hamster is probably asleep now. The system time is used. Return the string with state.
- `properties` - return string with the basic parameters of the hamster.

## `class RNASequence`

Class for operations with RNA sequences. Parent class - str.\

With two methods:
- `RNA_translation` - Translation - returns a string corresponding to the protein from the RNA, according to the standard code, using Biopython.
- `RNA_to_DNA` - Reverse transcription method - returns a string corresponding to the DNA from RNA, using Biopython

## `class PositiveSet`

A class inherited from sets. \
Contains only positive numbers when created and does not add non-positive numbers.\

Two methods redefined:
- `add` - checks if number for adding is positive. If so, it adds it to the PositiveSet using the regular set `add` method.
- `update` - update PositiveSet using positive values (PositiveSet `add` method) from the given args.

## `class FastaStats`

Class for collecting statistics on FASTA files. Parse FASTA file with Biopython.\
If you want print class instance it is a path to fasta file. Only __str__ defined, not __repr__.

**Input parameters:** Path to FASTS file

**Methods:**

1. `__init__` - Initialize FastaStats object, with:
    - `self.fasta_path` - path to FASTA file;
    - `self.alphabet` - "letters" in FASTA file;
    - `self.seq_type` - string with type of FASTA sequences.
 
2. `__str__` - for print `self.fasta_path` while print FastaStats object.

3. `count_seq` - counts the number of sequences in input FASTA file. Return `self.seq_number.

4. `fasta_alphabet` - Return a set with "letters" found in the FASTA file, `self.alphabet`.

5. `sequence_type` - Return a type of sequences (`self.seq_type`), RNA or DNA. If it is not possible to uniquely determine the type, it returns a conjectural type with ambiguous "letters".

6. `minmax_len` - Return min and max lenght of sequences in input FASTA file, self.min_len and self.max_len.

7. `histo_length(save_img_path=None)` - Building a histogram of sequences lengths in input FASTA file. If `save_img_path` is specified - save `.png` output there.

8. `percent_GC` - Returns the GC percentage of all sequences in a FASTA file, `self.GC`.
    
9. `histo_4_mers(save_img_path=None)` - Plot density plot of the frequency of 4-mers. If `save_img_path` is specified - save `.png` output there. On the x-axis each of the possible 4-mers, and on the y - their frequency. Work only for DNA sequences (`self.seq_type` should contain 'DNA'). Counted only 4-mers with A,T,C,G, not N.

10. `run_all_metrics(new_path=None)` - Run all implemented in the FastaStats class methods for calculating FASTA metrics. Create report, the `Metric_Result.csv` file and `.png` histograms. Save report in `'FASTAname'_report` folder with FASTA file, if other folder path not specified (new_path).


# Environment

Tested on Ubuntu 20.04.3 LTS.

Test on Python 3.10.

You can install venv with:
```console
sudo apt-get install python3.10 python3.10-venv
```

Required git:
```console
sudo apt install git
```

# Install and run with pip
## Installation

```console
git clone https://github.com/Freddsle/BI_2021_Python
cd ./BI_2021_Python/python_homework/classes_practice

# Create and activate your virtual environment

# create virtual environment
python3.10 -m venv ./venv

# activate virtual environment
source ./venv/bin/activate

# if you install it not from main or master, change branch
git checkout classes_task

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
cd ./BI_2021_Python/python_homework/classes_practice

# if you install it not from main or master, change branch
git checkout classes_task

poetry env use python3.10
poetry install

# Run
poetry run python practice.py
```
