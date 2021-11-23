import urllib.request
import re


def file_dowload(url, file_reference):
    '''
    Download file from url and save it to file_output (fale_path + file_name).
    '''
    with urllib.request.urlopen(url) as response, open(file_reference, 'wb') as out_file:
        data = response.read() # a `bytes` object
        out_file.write(data)


def ftp_parser(file_reference, file_output):
    '''
    Parse the references file and write all "ftp" links from there to the "ftps" file.
    '''
    ftp_regexp = re.compile(r'\bftp[#\.\w\/]+\b')
    all_ftp = []

    with open(file_reference, 'r') as ref_file:
        for line in ref_file:
            all_ftp.append('\n'.join(map(str, re.findall(ftp_regexp, line))))

    with open(file_output, 'a') as out_file:
        out_file.writelines('\n'.join(map(str, all_ftp)))


def main():
    # https://raw.githubusercontent.com/Serfentum/bf_course/master/15.re/references
    url = 'https://raw.githubusercontent.com/Serfentum/bf_course/master/15.re/references'
    file_reference = './references.txt'
    file_dowload(url, file_reference)

    # Parse the references file and write all "ftp" links from there to the "ftps" file
    file_output = './ftps_links_references.txt'
    ftp_parser(file_reference, file_output)





if __name__ == '__main__':
    main()
