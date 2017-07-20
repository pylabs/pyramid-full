import os
import re
import string
import random


REGEX = r'^#(secret_key|redis\.sessions\.secret) = .+$'

def main():
    working_dir = os.path.abspath(os.path.join(os.path.curdir))
    regex = re.compile(REGEX, flags=re.MULTILINE)

    # generate secret key
    for file_name in ['development.ini', 'production.ini']:
        ini_file = os.path.join(working_dir, file_name)
        with open(ini_file) as f:
            content = f.read()
        random_string = ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(50))
        content = regex.sub(r'\1 = {}'.format(random_string), content)
        with open(ini_file, 'w') as f:
            f.write(content)
    
    # show readme
    with open(os.path.join(working_dir, 'README.txt')) as f:
        print(f.read())

if __name__ == '__main__':
    main()
