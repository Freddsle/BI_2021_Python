# python3 -m pytest python_homework/classes_practice
import pytest  # noqa: F401; pylint: disable=unused-variable
from .practice import Hamster, RNASequence


def test_Hamster():
    Bun = Hamster('Bun', 18, 'Djungarian hamster')
    assert Bun.properties() == 'The hamster\'s name is Bun. It\'s old Djungarian hamster hamster, 18 months.'
    assert Bun.life_stage() == 'Bun is an old hamster. It\'s 18 months.'


def test_RNASequence():
    rna_seq_1 = RNASequence('AUGGCCAUUGUAAUGGGCCGCUGAAAGGGUGCCCGAUAG')
    rna_seq_2 = RNASequence('AUGC')

    assert rna_seq_1.RNA_translation() == 'MAIVMGR*KGAR*'
    assert rna_seq_1.RNA_to_DNA() == 'ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG'

    assert rna_seq_2.RNA_translation() == 'M'
    assert rna_seq_2.RNA_to_DNA() == 'ATGC'
