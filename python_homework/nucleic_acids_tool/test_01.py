# pytest python_homework/nucleic_acids_tool
import pytest  # noqa: F401; pylint: disable=unused-variable
from .nucleid_acids_01 import get_operations, DNAOperations, RNAOperations


def test_get_operations():
    assert isinstance(get_operations('tTgggcCAAAAAaa'), DNAOperations) == 1
    assert isinstance(get_operations('AUGC'), RNAOperations) == 1
    assert isinstance(get_operations('aaaaaa'), DNAOperations) == 1
    assert isinstance(get_operations('GccccUA'), RNAOperations) == 1
    assert isinstance(get_operations('AuT'), DNAOperations) == 0
    assert isinstance(get_operations('UUUUUU'), RNAOperations) == 1
    assert isinstance(get_operations('9hg3'), DNAOperations) == 0


def test_DNAreverse():
    assert DNAOperations().reverse('tTgggcCAAAAAaa') == 'aaAAAAACcgggTt'
    assert DNAOperations().reverse('aaaaaa') == 'aaaaaa'
    assert DNAOperations().reverse('c') == 'c'


def test_RNAreverse():
    assert RNAOperations().reverse('AUGC') == 'CGUA'
    assert RNAOperations().reverse('ugC') == 'Cgu'
    assert RNAOperations().reverse('U') == 'U'


def test_DNAcomplement():
    assert DNAOperations().complement('tTgggcCAAAAAaa') == 'aAcccgGTTTTTtt'
    assert DNAOperations().complement('aaaaaa') == 'tttttt'


def test_RNAcomplement():
    assert RNAOperations().complement('AUGC') == 'UACG'
    assert RNAOperations().complement('GccccUA') == 'CggggAU'


def test_DNAreverse_complement():
    assert DNAOperations().reverse_complement('tTgggcCAAAAAaa') == 'ttTTTTTGgcccAa'
    assert DNAOperations().reverse_complement('t') == 'a'
    assert DNAOperations().reverse_complement('Aaaaaa') == 'tttttT'


def test_RNAreverse_complement():
    assert RNAOperations().reverse_complement('U') == 'A'
    assert RNAOperations().reverse_complement('AUGC') == 'GCAU'
    assert RNAOperations().reverse_complement('GccccUA') == 'UAggggC'


def test_DNAtranscribe():
    assert DNAOperations().transcribe('tTgggcCAAAAAaa') == 'aAcccgGUUUUUuu'
    assert DNAOperations().transcribe('aaaaaa') == 'uuuuuu'
    assert DNAOperations().transcribe('A') == 'U'


def test_RNAtranscribe():
    assert RNAOperations().transcribe('AUGC') == 'Oops, I don`t know how to transcribe RNA. Try again.'
    assert RNAOperations().transcribe('U') == 'Oops, I don`t know how to transcribe RNA. Try again.'
