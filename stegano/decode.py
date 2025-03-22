from stegano import lsb
from tqdm import trange
from time import sleep
import os
import sys

file_path = f"{os.path.expanduser("~")}/Desktop/Decode"
files = []

def code_print(message):
    def char_print(string):
        for c in string:
            sys.stdout.write(c)
            sys.stdout.flush()
            sleep(0.04)

    def decorate_message(message):
        decoration = "=" * (len(message) + 4)
        print(decoration)

    print('')
    decorate_message(message)
    char_print(f"| {message} |\n")
    decorate_message(message)
    print('')

mutli_file_exception = """
==========================================================================
| Invalid number of files in Decode folder, try again with only one file |
==========================================================================
"""

decode_message = """
===============
| Decoding... |
===============
"""

no_message = """
============================
| No hidden message found! |
============================
"""

for f in os.listdir(file_path): 
    if not f.startswith('.'):
        files.append(f)

try:
    if len(files) != 1:
        raise Exception(mutli_file_exception)
except Exception as e:
    print(e)
else:
    print(decode_message)

    try:
        for i in trange(20):
            sleep(0.1)
        message = lsb.reveal(f"{file_path}/{files[0]}")
        code_print(message)

    except IndexError:
        print(no_message)