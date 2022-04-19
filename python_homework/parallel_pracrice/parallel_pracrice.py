import argparse
from collections import Counter
from concurrent.futures import ProcessPoolExecutor
from Bio import SeqIO


# This version would work if reading files was a problem. The problem is the calculations.
# def parallel_requests(fasta_path, threads=1):
#     with open(fasta_path) as fd, ThreadPoolExecutor(threads) as pool:     
#         for record in SeqIO.parse(fd, 'fasta'):
#             pool.submit(symbol_counter, record)


def parallel_counter(fasta_path: str, threads: int=1) -> None:
    """
    Read FASTA file by record and run symbol_counter func for each record in multiprocessing mode.
    Args:
        fasta_path: string, path to FASTA.
        threads: int, number of processes.
    """
    with open(fasta_path) as fd, ProcessPoolExecutor(threads) as pool:
        for record in SeqIO.parse(fd, 'fasta'):
            pool.submit(symbol_counter, record)


def symbol_counter(record):
    """
    Get SeqRecord object and print counted characters in it.
    Args:
        record: SeqRecord object.
    """
    counted_symbols = Counter(record.seq)
    counted_for_print = [f'{key}={value}' for key, value in zip(counted_symbols.keys(), counted_symbols.values())]
    print(f'{record.id}: \t {", ".join(counted_for_print)}')


if __name__ == '__main__':
    """
    Show help message: -h, -- help
    """
    parser = argparse.ArgumentParser()

    parser.add_argument("-i", "--input-fasta", help="path to FASTA file")
    parser.add_argument("-t", "--threads", default=1, type=int, help="number of parallel proceses")

    args = parser.parse_args()

    parallel_counter(fasta_path=args.input_fasta,
                      threads=args.threads)
