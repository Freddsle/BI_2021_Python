# simple work with RNA

class NAOperations:

    COMPLEMENT_MAP = NotImplemented

    def reverse(self, sequence):
        """Makes reverse sequence."""
        return sequence[::-1]

    def reverse_complement(self, sequence):
        """Makes reverse complement sequence."""
        return self.complement(self.reverse(sequence))

    def complement(self, sequence):
        """Makes complement sequence."""
        return sequence.translate(self.COMPLEMENT_MAP)

    def transcribe(self, sequence):
        """This exception is derived from RuntimeError."""
        raise NotImplementedError('Must be redefined in child class.')


class DNAOperations(NAOperations):

    COMPLEMENT_MAP = str.maketrans('atcgATCG',
                                   'tagcTAGC')
    TRANSCRIBE_MAP = str.maketrans('atcgATCG',
                                   'uagcUAGC')

    def transcribe(self, sequence):
        """Transcribes DNA sequence into RNA sequence."""
        return sequence.translate(self.TRANSCRIBE_MAP)


class RNAOperations(NAOperations):

    COMPLEMENT_MAP = str.maketrans('aucgAUCG',
                                   'uagcUAGC')

    def transcribe(self, sequence):
        """Can not ranscribe RNA sequence. Print "Try again"."""
        return 'Oops, I don`t know how to transcribe RNA. Try again.'


def get_operations(sequence):
    """Checks that nucleic acid is DNA OR RNA. If so, returns class operations. Otherwise, returns None"""
    na_letters = {'A', 'G', 'C'}
    dr_letter = {'T', 'U'}

    short_seq = set(sequence.upper()) - na_letters

    if len(short_seq) > 1:
        return None

    if len(short_seq) == 1 and not short_seq <= dr_letter:
        return None

    if short_seq == {'U'}:
        return RNAOperations()

    return DNAOperations()


def get_sequence():
    """Reads the sequence and checks whether it is RNA or DNA."""
    sequence = None

    while True:
        sequence = input('Now, please enter a sequence: ')
        operations = get_operations(sequence)

        if operations is None:
            print('Oops, It`s not a DNA or RNA. Try again.')
            continue

        return sequence, operations


def main():
    print('Hi! I can do simple things with your DNA or RNA')
    print('Now I show your available commands:')
    print('you can "reverse" - "r" or "transcribe" - "t" your sequence',
          'and make "complement" - "c" or "reverse_complement" - "rc"')

    commands_list = {'reverse', 'r', 'transcribe', 't', 'complement', 'c', 'reverse_complement', 'rc', 'exit'}

    # reads the command to work on DNA or RNA
    while True:

        command = input('Choose command or "exit": ')

        if command not in commands_list:
            print('Oops, something wrong. Please, choose another command')
            continue

        if command == 'exit':
            print('Goodbye!')
            break

        sequence, operations = get_sequence()

        if command == 'reverse' or command == 'r':
            print(operations.reverse(sequence))

        elif command == 'complement' or command == 'c':
            print(operations.complement(sequence))

        elif command == 'reverse_complement' or command == 'rc':
            print(operations.reverse_complement(sequence))

        elif command == 'transcribe' or command == 't':
            print(operations.transcribe(sequence))


if __name__ == '__main__':
    main()
