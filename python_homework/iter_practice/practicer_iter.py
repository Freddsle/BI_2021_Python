# Practise with iterators
import random


class AASequenceChanger:
    '''Read a file with amino acid sequnces and make deletions,
    substitutions and insertions during iteration.
    If the file is end, then the iteration continues from its beginning.
    Any change in the sequence occurs with a probability of 50%.
    Which change will occur is chosen randomly.
    '''
    AA_ALPHABET = 'ACDEFGHIKLMNPQRSTVWY'

    def __init__(self, fasta_path):
        """Create AASequenceChanger object.
        Read file from path and add all sequences to list self.text.
        Args:
            file_path: Path to the FASTA file with amino acid sequnces.
        Return:
            nothing.
        """
        self.fasta_path = fasta_path
        self.text = self.read_sequences(self.fasta_path)
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        """Return next element from self.text - list with AA sequnces.
        Newer stop iteration. When elements end, then the iteration continues from its beginning.
        Args:
            self.
        Return:
            string: string with altered amino acid sequence.
        """
        try:
            result = self.text[self.index]

        except IndexError:
            self.index = 0
            result = self.text[self.index]

        self.index += 1
        return self.random_changes(result)

    def random_changes(self, sequence):
        """Make random change in sequence with 50% probability for each letter.
        Args:
            self
            sequence: amino acid sequence for changes.
        Return:
            new_seq: string with altered amino acid sequence.
        """
        new_seq = []
        changes = [self.make_deletion, self.make_substitution, self.make_insertion]

        for i in sequence:
            if random.randint(0, 1):
                new_seq.append(i)

            else:
                selected_change = random.choice(changes)
                new_seq.append(selected_change(i))

        new_seq = ''.join(new_seq)
        return new_seq

    def make_deletion(self, letter):
        """Remove an amino acid from a sequence.
        Return empty string for this.
        Args:
            self
            letter: letter for changes.
        Return:
            '': empty string.
        """
        return ''

    def make_substitution(self, letter):
        """Replaces an amino acid in a sequence with a random amino acid.
        Return random letter for this.
        Args:
            self
            letter: letter for changes.
        Return:
            string: randomly selected letter from AA_ALPHABET.
        """
        return random.choice(self.AA_ALPHABET)

    def make_insertion(self, letter):
        """Insert a random amino acid in a sequence.
        Return random letter and initial letter for this.
        Args:
            self
            letter: letter for changes.
        Return:
            string: initial letter plus randomly selected letter from AA_ALPHABET.
        """
        return ''.join([letter, random.choice(self.AA_ALPHABET)])

    def read_sequences(self, file_path):
        """Takes as input the path to the FASTA file and outputs list with sequence.
        Args:
            file_path: Path to the FASTA file.
        Return:
            list with sequences strings.
        """
        temp_list = []
        seq_strings = []

        with open(file_path) as inf:
            for line in inf:
                line = line.rstrip()

                if line.startswith('>'):
                    if temp_list:
                        seq_strings.append(''.join(temp_list[1:]))
                        temp_list = []

                temp_list.append(line)

        return seq_strings


def fasta_reader(file_path):
    """Generetor.
    Takes as input the path to the FASTA file and outputs pairs sequence id and sequence in turn.
    Args:
        file_path: Path to the FASTA file.
    Yields:
        seq_id, sequence.
    """
    temp_list = []

    with open(file_path) as inf:
        for line in inf:
            line = line.rstrip()

            if line.startswith('>'):
                if temp_list:
                    yield temp_list[0], ''.join(temp_list[1:])
                    temp_list = []

            temp_list.append(line)


if __name__ == '__main__':
    # test print for first task - read fasta file from data folder.
    # Print type of fasta_reader object.
    # Print seq ID and first 50 letter of sequence for each sequence.
    path_fasta_long = './data/sequences.fasta'
    reader = fasta_reader(path_fasta_long)
    print(type(reader))

    for id_, seq in reader:
        print(id_, seq[:50])

    # separator
    print('----------------------')

    # Example for class
    # Print 20 rows with changed sequneces from fasta file.
    path_fasta_short = './data/seq.fasta'
    seq_for_change = AASequenceChanger(path_fasta_short)

    j = 0
    for seq in seq_for_change:
        if j < 20:
            print(seq)
        else:
            break
        j += 1
