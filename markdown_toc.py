import argparse
from functools import reduce
import os
import string

def link_style(title):
    #strip punctuation
    stripped = title.translate(str.maketrans('', '', string.punctuation))
    split = stripped.split(" ")
    lowercase = list(map(lambda x: x.lower().strip(), split))
    filtered = filter(lambda x: len(x) > 0, lowercase)
    return "-".join(filtered)

def create_toc(filename):
    f = open(filename, "r")
    for x in f:
        #we've found a heading
        if x.startswith("#"):
            last_indx = x.rfind("#")
            title = x[last_indx+1:]
            print(f"* [{title.strip()}](#{link_style(title)})")
    f.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Read Markdown File and output TOC in lkrych style')
    parser.add_argument('file', type=str, nargs='+',
                    help='a filename to open')
    args = parser.parse_args()
    create_toc(args.file[0])