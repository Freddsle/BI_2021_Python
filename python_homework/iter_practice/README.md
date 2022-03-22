# Practise with iterators in Python

1. **Generetor `fasta_reader`**.
    Takes as input the path to the FASTA file and outputs pairs sequence id and sequence in turn.\
    Arg: file_path: Path to the FASTA file.
    Yield: seq_id, sequence.\
    Test print in `if __name__ == '__main__` block - read fasta file from data folder. Print type of fasta_reader object. Print seq ID and first 50 letter of sequence for each sequence.
   
2. **class AASequenceChanger:**\
    Read a file with amino acid sequnces and make deletion, substitutions and insertions during iteration. \    
    If the file is end, then the iteration continues from its beginning.\
    Any change in the sequence occurs with a probability of 50%. Which change will occur is chosen randomly.\
    
    Contains methods:
    
    - `__init__` - Create AASequenceChanger object. Read file from path and add all sequences to list self.text.\
        Args: file_path: Path to the FASTA file with amino acid sequnces.\
        Return: nothing.
    
    - `__next__` - Return next element from self.text - list with AA sequnces. Newer stops iteration. When elements end, then the iteration continues from its beginning.\
        Return: string: string with altered amino acid sequence.

    - `random_changes` - Make random change in sequence with 50% probability for each letter.\
        Return: new_seq: string with altered amino acid sequence.

    - `make_deletion` - Remove an amino acid from a sequence. Take one letter from `random_changes`. Return empty string for this.

    - `make_substitution` - Replaces an amino acid in a sequence with a random amino acid. Take one letter from `random_changes`. Return random letter for this. \
        Return: string: randomly selected letter from AA_ALPHABET.

    - `make_insertion` - Insert a random amino acid in a sequence. Take one letter from `random_changes`. Return random letter and initial letter for this.\
        Return: string: initial letter plus randomly selected letter from AA_ALPHABET.
      
    - `read_sequences` - Takes as input the path to the FASTA file and outputs list with sequence.\
        Arg: file_path: Path to the FASTA file.\
        Return: list with sequences strings.

    Example for class in `if __name__ == '__main__` block. Print 20 rows with changed sequneces from fasta file.


3. **Generetor `iter_append`**.

    A generator that "adds" an item element to the "end" of an iterable.\
    Args:\
        - iterable: something iterable.\
        - item: object to add at the end of iterable.\
    Yields:\
        - from iterable.\
        - item.

Example for generetor in `if __name__ == '__main__` block.

4. **Function `nested_list_unpacker` for "unpacks" nested lists**.

    Function for "unpacks" nested lists. Uses unpack_generator for it. Lists can be nested at any level. Creates empty list when starts.
    
    Args:\
        - iterable: iterable for unpacking.\
        - resulting: list for result, empty when unpacking starts.
    
    Return: resulting: resulting list with unpacked iterable.

    Uses `unpack_generator` for unpacking. Function for unpacking iterable. When iterable is list, unpack it. When not, yield iterable.\
    Args: iterable: iterable for unpacking.\
    Yields: i: all elements from i if iterable of i if not.

Example for `nested_list_unpacker` in `if __name__ == '__main__` block.

# Install and run with pip
## Installation

```console
git clone https://github.com/Freddsle/BI_2021_Python
cd ./BI_2021_Python/python_homework/iter_practice

# Create and activate your virtual environment

# create virtual environment
python3.10 -m venv ./venv

# activate virtual environment
source ./venv/bin/activate

# if you install it not from main or master, change branch
git checkout iterators

# required by pip to build wheels
pip install wheel==0.37.0 

# Install requirements
pip install -r ./requirements.txt
```

## Run file
```console
python3.10 practicer_iter.py
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
cd ./BI_2021_Python/python_homework/iter_practice

# if you install it not from main or master, change branch
git checkout iterators

poetry env use python3.10
poetry install

# Run
poetry run python practicer_iter.py

# or for run .ipynb files
poetry run jupyter notebook
```
