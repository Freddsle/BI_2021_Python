import urllib.request


def file_dowload(url, file_output):
    '''
    Download file from url and save it to file_output (fale_path + file_name).
    '''
    with urllib.request.urlopen(url) as response, open(file_output, 'wb') as out_file:
        data = response.read() # a `bytes` object
        out_file.write(data)


def main():

    # Parse the references file and write all "ftp" links from there to the "ftps" file
    # https://raw.githubusercontent.com/Serfentum/bf_course/master/15.re/references
    url = 'https://raw.githubusercontent.com/Serfentum/bf_course/master/15.re/references'
    file_output = './references.txt'
    file_dowload(url, file_output)


if __name__ == '__main__':
    main()
