#simple work with RNA

class DNAOperations:

    def reverse(self, sequence):
        'Makes reverse sequence.'
        return sequence[::-1]


    def complement(self, sequence):
        'Makes complement sequence. If u or U in sequence - works like with RNA, otherwise, like with DNA.'
        dna_dict = {'a':'t', 't':'a', 'c':'g', 'g':'c', 'A':'T', 'T':'A', 'C':'G', 'G':'C'}
        answer = ''
    
        for letter in sequence:
                answer += dna_dict[letter]
        
        return answer


    def transcribe(self, sequence):
        'Transcribes DNA sequence to RNA sequence.'
        dna_dict = {'a':'u', 't':'a', 'c':'g', 'g':'c', 'A':'U', 'T':'A', 'C':'G', 'G':'C'}
        answer = ''

        for letter in sequence:
            answer += dna_dict[letter]
    
        return answer


    def reverse_complement(self, sequence):
        'Makes reverse complement sequence.'
        return self.complement(self.reverse(sequence))


class RNAOperations:

    def reverse(self, sequence):
        'Makes reverse sequence.'
        return sequence[::-1]


    def complement(self, sequence):
        'Makes complement sequence. If u or U in sequence - works like with RNA, otherwise, like with DNA.'
        rna_dict = {'a':'u', 'u':'a', 'c':'g', 'g':'c', 'A':'U', 'U':'A', 'C':'G', 'G':'C'}
        answer = ''
        
        for letter in sequence:
            answer += rna_dict[letter]
        
        return answer


    def transcribe(self, sequence):
        'Can not ranscribe RNA sequence. Print "Try again".'
        return 'Oops, I don`t know how to transcribe RNA. Try again.'


    def reverse_complement(self, sequence):
        'Makes reverse complement sequence.'
        return self.complement(self.reverse(sequence))
    

def check_na(sequence):
    'checks that nucleic acid is DNA OR RNA. If so, returns 1 otherwise, returns 0'
    na_letters = {'A','G', 'C'}
    dr_letter = {'T', 'U'}

    short_seq = set(sequence.upper()) - na_letters

    if len(short_seq) > 1:
        return False
    
    if len(short_seq) == 1 and not short_seq <= dr_letter:
        return False

    if short_seq == {'U'}:
        return RNAOperations()

    return DNAOperations()


def main():
    print('Hi! I can do simple things with your DNA or RNA')
    print('Now I show your available commands:')
    print('you can "reverse" - "r" or "transcribe" - "t" your sequence and make "complement" - "c" or "reverse_complement" - "rc"')
    
    #reads the first command to work on DNA or RNA
    command = str(input('Choose command or "exit": '))

    while command != 'exit':
        
        #reads the sequence and checks whether it is RNA or DNA
        sequence = str(input('Now, please enter a sequence: '))
        operations = check_na(sequence)
        
        if not operations:
            if sequence == 'exit':
                command = sequence
            else:
                print('Oops, It`s not a DNA or RNA. Try again.')
            continue

        if command == 'reverse' or command == 'r':
            print(operations.reverse(sequence))

        elif command == 'complement' or command == 'c':
            print(operations.complement(sequence))
    
        elif command == 'reverse_complement' or command == 'rc':
            print(operations.reverse_complement(sequence))
    
        elif command == 'transcribe' or command == 't':
            print(operations.transcribe(sequence))

        else:
            print('Oops, something wrong. Please, choose another command')


        #Asks next command and moves to the next cycle
        command = str(input('Choose command or "exit": '))


    print('Goodbye!')


if __name__ == '__main__':
    main()
