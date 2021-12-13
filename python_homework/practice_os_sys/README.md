# Unix-like Python scripts

The scripts are guaranteed to work on Linux systems. 

## Added scripts:

- **cat.py** - UNIX `cat` analog:
    
    Concatenate FILE(s) to standard output. With no FILE read standard input.

- **head.py** - UNIX `head` analog: 

    Print the first 10 lines of each FILE to standard output. With more than one FILE, precede each with a header giving the file name. With no FILE read standard input. Doesn't work without input.

- **tail.py** - UNIX `tail` analog: 
    
    Print the last 10 lines of each FILE to standard output. With more than one FILE, precede each with a header giving the file name. With no FILE read standard input. Doesn't work without input.

- **wc.py** - UNIX `wc` analog: 
    Print newline, word, and byte counts for each FILE. A word is a non-zero-length sequence of characters delimited by white space. \
    Words at the end of the file without trailing "\n" are also counted. \
    If multiple arguments are passed, the output is in "lines", "words", "bytes" order. Each in new line.

- **sort.py** - UNIX `sort` analog: 
    
    Write sorted concatenation of all FILE(s) to standard output. With no FILE read standard input. The locale specified by the environment affects sort order.

- **uniq.py** - UNIX `uniq` analog: 
    
    Filter adjacent matching lines from INPUT (or standard input), writing to OUTPUT (or standard output). The order in which lines are output is not guaranteed.

- **rm.py** - UNIX `rm` analog: 
    
    Remove the FILE(s) or DIRs. Remove directories with option "-d". If directory is not empty - "-r" ortion should used to remove dir recursively.

- **mv.py** - UNIX `mv` analog: Rename SOURCE to DEST, or move SOURCE(s) to DIRECTORY.

- **cp.py** - UNIX `cp` analog: Copy SOURCE to DEST, or multiple SOURCE(s) to DIRECTORY.

- **mkdir.py** - UNIX `mkdir` analog: 

    Create the DIRECTORY(ies), if they do not already exist. If you need to create directory in subdirectory - use "-p" option.

- **ls.py** - UNIX `ls` analog: List information about the FILEs (from the current directory by default). Sort entries.

- **ln.py** - UNIX `ln` analog: 

    Create a link to TARGET with the name LINK_NAME. Create hard links by default, symbolic links with "--symbolic". \
    Each destination (name of new link) should not already exist. \
    When creating hard links, each TARGET must exist.

- **grep.py** - UNIX `grep` analog: 
    
    Search for PATTERNS in each FILE. \
    PATTERNS can contain multiple patterns separated with pipes, "|", but printed in one string. \
    The line will be printed if at least one pattern is found. When no FILE read standard input.

You can read more info about options when run script with `-h` option.


# Install

Required Python version [3.9-3.10].

**Attention!** To install you shoud have sudo rights!
```
git clone https://github.com/Freddsle/BI_2021_Python.git

cd BI_2021_Python/python_homework/practice_os_sys

sudo python3 ./install.py
``` 


# Tested on
Ubuntu 20.04 LTS, Python 3.9.5.

Scripts are not guaranteed to work as expected on Windows.
