

def reverse_lines(in_file, out_file):
    with open(in_file) as fin, open(out_file, 'w') as fout:
        for line in fin:
            fout.write(f'{line.rstrip()[::-1]}\n')

reverse_lines("./testdir/test1.txt", "./testdir/test1-rev.txt")
