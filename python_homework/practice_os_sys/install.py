import os
import shutil


def main():
    '''
    Copy scripts from "./" to PATH.
    '''

    scripts = ['./wc.py', './tail.py', './sort.py', './rm.py',
               './mkdir.py', './ls.py', './ln.py', './head.py',
               './grep.py', './cp.py', './cat.py', './mv.py',
               './uniq.py']

    standart_path = '/usr/local/bin'
    now_paths = os.environ['PATH'].split(':')

    if os.path.isdir(standart_path) and standart_path in now_paths:
        for script in scripts:
            shutil.copy(script, standart_path)

    else:
        for script in scripts:
            shutil.copy(script, now_paths[0])


if __name__ == '__main__':
    """
    Show help message: -h, -- help.
    """
    main()
