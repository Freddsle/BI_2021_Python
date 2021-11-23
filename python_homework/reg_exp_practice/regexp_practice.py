import urllib.request
import re


def file_dowload(url, file_reference):
    '''
    Download file from url and save it to file_output (fale_path + file_name).
    '''
    with urllib.request.urlopen(url) as response, open(file_reference, 'wb') as out_file:
        data = response.read() # a `bytes` object
        out_file.write(data)


def read_write(file_input, file_output, match_regexp):
    all_matches = []

    with open(file_input, 'r') as ref_file:
        for line in ref_file:
            find_list = re.findall(match_regexp, line)
            if find_list:
                all_matches.append('\n'.join(map(str, find_list)))

    with open(file_output, 'a') as out_file:
        out_file.writelines('\n'.join(map(str, all_matches)))


def ftp_parser(url):
    '''
    Parse the references file and write all "ftp" links from there to the "ftps" file.
    '''
    file_reference = 'python_homework/reg_exp_practice/files/references.txt'
    file_dowload(url, file_reference)
    file_output = 'python_homework/reg_exp_practice/files/ftps.txt'

    ftp_regexp = re.compile(r'\bftp[#\.\w\/]+\b')
    read_write(file_reference, file_output, ftp_regexp)


def numbers_parser(url):
    '''
    Parse the tale file and write all numbers from there to the .txt file.
    '''
    file_tale = 'python_homework/reg_exp_practice/files/tale.txt'
    file_dowload(url, file_tale)

    # Extract from the tale 2430 A.D. all numbers
    file_output_numbers = 'python_homework/reg_exp_practice/files/tale_numbers.txt'
    number_regexp = re.compile(r'(?<=\D)\d+\.{0,1}\d*(?=\D)')
    read_write(file_tale, file_output_numbers, number_regexp)

    # From the same tale, extract all words that contain the letter a, case is not important
    file_output_words = 'python_homework/reg_exp_practice/files/tale_a_words.txt'
    a_word_regexp = re.compile(r'(?<=\b)\w*[aA][\w\']*(?=\b)')
    read_write(file_tale, file_output_words, a_word_regexp)


def main():

    # Parse the references file and write all "ftp" links from there to the "ftps" file
    # # https://raw.githubusercontent.com/Serfentum/bf_course/master/15.re/references
    url = 'https://raw.githubusercontent.com/Serfentum/bf_course/master/15.re/references'
    ftp_parser(url)
    
    # https://raw.githubusercontent.com/Serfentum/bf_course/master/15.re/2430AD
    url = 'https://raw.githubusercontent.com/Serfentum/bf_course/master/15.re/2430AD'
    numbers_parser(url)


if __name__ == '__main__':
    main()
