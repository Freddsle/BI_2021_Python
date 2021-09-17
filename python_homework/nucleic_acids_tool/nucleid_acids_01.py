#simple work with RNA

class NAOperations:

    def reverse(self, sequence):
        'Makes reverse sequence.'
        return sequence[::-1]

    def reverse_complement(self, sequence):
        'Makes reverse complement sequence.'
        return self.complement(self.reverse(sequence))


class DNAOperations(NAOperations):

    def complement(self, sequence):
        'Makes complement sequence.'
        dna_dict_com = {'a':'t', 't':'a', 'c':'g', 'g':'c', 'A':'T', 'T':'A', 'C':'G', 'G':'C'}
        dna_table_com = sequence.maketrans(dna_dict_com)        
        return sequence.translate(dna_table_com)


    def transcribe(self, sequence):
        'Transcribes DNA sequence into RNA sequence.'
        dna_dict_trans = {'a':'u', 't':'a', 'c':'g', 'g':'c', 'A':'U', 'T':'A', 'C':'G', 'G':'C'}
        dna_table_trans = sequence.maketrans(dna_dict_trans)        
        return sequence.translate(dna_table_trans)


class RNAOperations(NAOperations):

    def complement(self, sequence):
        'Makes complement sequence.'
        rna_dict = {'a':'u', 'u':'a', 'c':'g', 'g':'c', 'A':'U', 'U':'A', 'C':'G', 'G':'C'}
        rna_table = sequence.maketrans(rna_dict)        
        return sequence.translate(rna_table)


    def transcribe(self, sequence):
        'Can not ranscribe RNA sequence. Print "Try again".'
        return 'Oops, I don`t know how to transcribe RNA. Try again.'
    

def get_operations(sequence):
    'Checks that nucleic acid is DNA OR RNA. If so, returns class operations. Otherwise, returns None'
    na_letters = {'A','G', 'C'}
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
    'Reads the sequence and checks whether it is RNA or DNA.'
    sequence = None

    while True:
        sequence = str(input('Now, please enter a sequence: '))
        operations = get_operations(sequence)

        if operations is None:
            print('Oops, It`s not a DNA or RNA. Try again.')
            continue

        return sequence, operations


def main():
    print('Hi! I can do simple things with your DNA or RNA')
    print('Now I show your available commands:')
    print('you can "reverse" - "r" or "transcribe" - "t" your sequence and make "complement" - "c" or "reverse_complement" - "rc"')
    
    commands_list = ('reverse', 'r', 'transcribe', 't', 'complement', 'c', 'reverse_complement', 'rc', 'exit')
    
    #reads the command to work on DNA or RNA
    while True:

        command = str(input('Choose command or "exit": '))

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
