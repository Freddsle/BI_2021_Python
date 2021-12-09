import urllib.request
import re
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def file_dowload(url, file_reference):
    '''
    Download file from url and save it to file_output (fale_path + file_name).
    '''
    with urllib.request.urlopen(url) as response, open(file_reference, 'wb') as out_file:
        data = response.read()
        out_file.write(data)


def write_matches(file_output, matches):
    with open(file_output, 'a') as out_file:
        out_file.writelines('\n'.join(map(str, matches)))


def read_file_lines(file_input, match_regexp):
    '''
    It parse input file and write to output file all regexp matches.
    '''
    all_matches = []

    with open(file_input, 'r') as ref_file:
        for line in ref_file:
            find_list = re.findall(match_regexp, line)
            if find_list:
                all_matches.extend(find_list)

    return all_matches


def ftp_parser(url):
    '''
    Parses the references file and write all "ftp" links from there to the "ftps" file.
    '''
    file_reference = 'python_homework/reg_exp_practice/files/references.txt'
    file_dowload(url, file_reference)

    file_output = 'python_homework/reg_exp_practice/files/ftps.txt'
    ftp_matches = read_file_lines(file_reference, re.compile(r'\bftp[#\.\w\/]+\b'))
    write_matches(file_output, ftp_matches)


def tale_parser(url):
    '''
    Parses the tale file and write all numbers from there to the .txt file.
    '''
    file_tale = 'python_homework/reg_exp_practice/files/tale.txt'
    file_dowload(url, file_tale)

    # Extract from the tale 2430 A.D. all numbers
    file_output_numbers = 'python_homework/reg_exp_practice/files/tale_numbers.txt'
    number_regexp = re.compile(r'(?<=\D)\d+\.{0,1}\d*(?=\D)')
    number_matches = read_file_lines(file_tale, number_regexp)
    write_matches(file_output_numbers, number_matches)

    # From the same tale, extract all words that contain the letter a, case is not important
    file_output_words = 'python_homework/reg_exp_practice/files/tale_a_words.txt'
    a_word_regexp = re.compile(r'(?<=\b)\w*[aA][\w\']*\.*\S*(?=\b)')
    a_word__matches = read_file_lines(file_tale, a_word_regexp)
    write_matches(file_output_words, a_word__matches)

    # Extract all exclamation sentences from the story
    file_output_ex = 'python_homework/reg_exp_practice/files/tale_exclamation.txt'
    ex_regexp = re.compile(r'(?<=[(\s\"])[A-Z]+[\w\s\'\,]*!(?=[\s\"])')
    ex_matches = read_file_lines(file_tale, ex_regexp)
    write_matches(file_output_ex, ex_matches)

    # Plot a histogram of the distribution of the lengths of unique words (case-insensitive, length from 1) in the text.
    words_regexp = re.compile(r'(?<=\b)[\w\']\S*(?=\b)')
    words = read_file_lines(file_tale, words_regexp)
    words = set([word.lower() for word in read_file_lines(file_tale, words_regexp)])
    print("\n".join(words))
    uniqe_words_plot(words)


def uniqe_words_plot(uniqe_wors):
    '''
    Plots a histogram of the distribution of the lengths of unique words (case-insensitive, length from 1) in the text.
    '''
    data = pd.DataFrame(uniqe_wors, columns=['word'])
    data['word_len'] = data['word'].str.len()

    plt.margins(0)
    sns.histplot(data['word_len'], stat="density", common_norm=False)
    plt.title('Distribution of lengths of unique words')
    plt.xlabel('word lenght')
    plt.gcf().set_size_inches(8, 6)
    plt.savefig('python_homework/reg_exp_practice/files/Words lenght density.png', dpi=100, bbox_inches='tight')
    plt.close()


def shuffle_text(input_text):
    'Shuffle words in text. Shuffle from second to penultimate letter (like "word[1:-1]".'

    input_text = input_text.split(' ')
    
    for i, word in enumerate(input_text):
        if len(word) > 2 and len(word[1:-1]) > 1:
            if word[-1] != '.' and word[-1] != ',':
                inside_letters = word[1:-1]
                inside_letters = ''.join(random.sample(inside_letters, len(inside_letters)))
                input_text[i] = word[0] + inside_letters + word[-1]
            else:
                inside_letters = word[1:-2]
                inside_letters = ''.join(random.sample(inside_letters, len(inside_letters)))
                input_text[i] = word[0] + inside_letters + word[-2:]
                
    
    return ' '.join(input_text)


def main():

    # Parse the references file and write all "ftp" links from there to the "ftps" file
    # # https://raw.githubusercontent.com/Serfentum/bf_course/master/15.re/references
    url = 'https://raw.githubusercontent.com/Serfentum/bf_course/master/15.re/references'
    ftp_parser(url)

    # https://raw.githubusercontent.com/Serfentum/bf_course/master/15.re/2430AD
    url = 'https://raw.githubusercontent.com/Serfentum/bf_course/master/15.re/2430AD'
    tale_parser(url)


if __name__ == '__main__':
    main()
