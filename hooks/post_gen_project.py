import os
import re
import string
import random


REGEX_LIST = [r'^(session.key) = .+$', r'^(session.secret) = .+$', r'^(auth.key) = .+$']

def main():
    working_dir = os.path.abspath(os.path.join(os.path.curdir))
    regex_list = [re.compile(i, re.MULTILINE) for i in REGEX_LIST]

    # generate pyramid_beaker secret key
    for file_name in ['development.ini.sample', 'production.ini.sample']:
        ini_file = os.path.join(working_dir, os.path.splitext(file_name)[0])
        with open(file_name) as f:
            content = f.read()
        for regex in regex_list:
            random_string = ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.digits) \
                                    for _ in range(50))
            content = regex.sub(r'\1 = {}'.format(random_string), content)
        with open(ini_file, 'w') as f:
            f.write(content)
    
    # show readme
    with open(os.path.join(working_dir, 'README.txt')) as f:
        print(f.read())

if __name__ == '__main__':
    main()
