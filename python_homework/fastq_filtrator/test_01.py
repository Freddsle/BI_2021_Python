# pytest python_homework/fastq_filtrator
import pytest  # noqa: F401; pylint: disable=unused-variable
from fastq_filtrator import fastq_filtrator


def test_check_bound():
    assert fastq_filtrator.check_bound(['1', '100']) == [1.0, 100.0]
    assert fastq_filtrator.check_bound(['1', '100', '35']) == None
    assert fastq_filtrator.check_bound(['1', 'a']) == None
    assert fastq_filtrator.check_bound(['56']) == [56.0]


def test_make_len_bounds():
    assert fastq_filtrator.make_len_bounds(['1', '100']) == [1.0, 100.0]
    assert fastq_filtrator.make_len_bounds(['1', '100', '35']) == None
    assert fastq_filtrator.make_len_bounds(['1', 'a']) == None
    assert fastq_filtrator.make_len_bounds(['56']) == [0, 56.0]


def test_make_gc_bounds():
    assert fastq_filtrator.make_gc_bounds(['1', '100']) == [1.0, 100.0]
    assert fastq_filtrator.make_gc_bounds(['1', '100', '35']) == None
    assert fastq_filtrator.make_gc_bounds(['1', 'a']) == None
    assert fastq_filtrator.make_gc_bounds(['56']) == [0, 56.0]


def test_filter_gc():
    assert fastq_filtrator.filter_gc('ACTGACTG', 8, [0, 100.0]) == True
    assert fastq_filtrator.filter_gc('ACTGACTG', 8, [0, 40.0]) == False
    assert fastq_filtrator.filter_gc('ACTGACTG', 8, [80.0, 100.0]) == False


def test_filter_length():
    assert fastq_filtrator.filter_length(507, [0, 1000.0]) == True
    assert fastq_filtrator.filter_length(8, [0, 40.0]) == True
    assert fastq_filtrator.filter_length(108, [0, 100.0]) == False


def test_filter_quality():
    assert fastq_filtrator.filter_quality(23, '???BDB:DFHBFD@9;;+A;AFG', 0) == True
    assert fastq_filtrator.filter_quality(23, '???BDB:DFHBFD@9;;+A;AFG', 35) == False

def test_filter_fastq():
    assert fastq_filtrator.filter_fastq([0, 'ACTGACTG\n', '', 'BDB:DFHB\n'], [0, 100.0], [0, 1000.0], 0) == True
    assert fastq_filtrator.filter_fastq([0, 'ACTGACTG\n', '', 'BDB:DFHB\n'], [0, 100.0], [0, 5], 0) == False
    assert fastq_filtrator.filter_fastq([0, 'GGGGGGGG\n', '', 'BDB:DFHB\n'], [0, 40.0], [0, 1000.0], 0) == False
