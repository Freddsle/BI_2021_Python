#simple work with RNA

# Reads commands from the user in an endless loop.
# After the command, the program prompts the user for the nucleic acid sequence, converts it, and outputs the result.
# Program preserves case (e.g. complement AtGc is TaCg)
# Works only with DNA OR RNA, not with mixed.


def check_na(sequence):
    'checks that nucleic acid is DNA OR RNA. If so, returns 1 otherwise, returns 0'
    na_letters = {'A','G', 'C'}
    dr_letter = {'T', 'U'}

    short_seq = set(sequence.upper()) - na_letters

    if len(short_seq) > 1:
        return 0
    
    if len(short_seq) == 1 and not short_seq <= dr_letter:
        return 0

    return 1


def reverse(sequence):
    'makes reverse sequence'
    return sequence[::-1]


def complement(sequence):
    'makes complement sequence. If u or U in sequence - works like with RNA, otherwise, like with DNA'
    dna_dict = {'a':'t', 't':'a', 'c':'g', 'g':'c', 'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    rna_dict = {'a':'u', 'u':'a', 'c':'g', 'g':'c', 'A':'U', 'U':'A', 'C':'G', 'G':'C'}

    answer = ''

    if 'u' in sequence or 'U' in sequence:
        for letter in sequence:
            answer += rna_dict[letter]
    else:
        for letter in sequence:
            answer += dna_dict[letter]

    return answer


def reverse_complement(sequence):
    'makes reverse complement sequence'
    return complement(reverse(sequence))


def transcribe(sequence):
    'transcribes DNA sequence'
    dna_dict = {'a':'u', 't':'a', 'c':'g', 'g':'c', 'A':'U', 'T':'A', 'C':'G', 'G':'C'}
    answer = ''

    if 'u' in sequence or 'U' in sequence:
        return 'Oops, I don`t know how to transcribe RNA. Try again.'
    else:
        for letter in sequence:
            answer += dna_dict[letter]
        return answer


def main():
    print('Hi! I can do simple things with your DNA or RNA')
    print('Now I show your available commands:')
    print('you can "reverse" - "r" or "transcribe" - "t" your sequence and make "complement" - "c" or "reverse_complement" - "rc"')
    
    'reads the first command to work on DNA or RNA'
    command = str(input('Chose command or "exit": '))

    while command != 'exit':
        
        'reads the sequence and checks whether it is RNA or DNA'
        sequence = str(input('Now, please enter a sequence: '))
        correct_check = check_na(sequence)
        
        if correct_check:
            print('Great, lets work with nucleic acid')
        else:
            if sequence == 'exit':
                command = sequence
            else:
                print('Oops, It`s not a DNA or RNA. Try again.')
            continue
        
        'executes the required command on the given sequence'
        if command == 'reverse' or command == 'r':
            print(reverse(sequence))
            
        elif command == 'complement' or command == 'c':
            print(complement(sequence))
        
        elif command == 'reverse_complement' or command == 'rc':
            print(reverse_complement(sequence))
        
        elif command == 'transcribe' or command == 't':
            print(transcribe(sequence))

        else:
            print('Oops, something wrong. Please, chose another command')

        'Asks next command and moves to the next cycle'
        command = str(input('Chose command or "exit": '))


    print('Goodbye!')


if __name__ == '__main__':
    main()
