#pytest python_homework/nucleid_acids_tool


import pytest
from .nucleid_acids_01 import check_na, reverse, complement, reverse_complement, transcribe


def test_check_na():
    assert check_na('tTgggcCAAAAAaa') == 1
    assert check_na('AUGC') == 1
    assert check_na('aaaaaa') == 1
    assert check_na('GccccUA') == 1
    assert check_na('AuT') == 0
    assert check_na('UUUUUU') == 1
    assert check_na('Ac9G') == 0
    assert check_na('9hg3') == 0


def test_reverse():
    assert reverse('tTgggcCAAAAAaa') == 'aaAAAAACcgggTt'
    assert reverse('AUGC') == 'CGUA'
    assert reverse('aaaaaa') == 'aaaaaa'
    assert reverse('GccccUA') == 'AUccccG'


def test_complement():
    assert complement('tTgggcCAAAAAaa') == 'aAcccgGTTTTTtt'
    assert complement('AUGC') == 'UACG'
    assert complement('aaaaaa') == 'tttttt'
    assert complement('GccccUA') == 'CggggAU'


def test_reverse_complement():
    assert reverse_complement('tTgggcCAAAAAaa') == 'ttTTTTTGgcccAa'
    assert reverse_complement('U') == 'A'
    assert reverse_complement('AUGC') == 'GCAU'
    assert reverse_complement('aaaaaa') == 'tttttt'
    assert reverse_complement('GccccUA') == 'UAggggC'


def test_transcribe():
    assert transcribe('tTgggcCAAAAAaa') == 'aAcccgGUUUUUuu'
    assert transcribe('AUGC') == 'Oops, I don`t know how to transcribe RNA'
    assert transcribe('aaaaaa') == 'uuuuuu'
    assert transcribe('A') == 'U'
    