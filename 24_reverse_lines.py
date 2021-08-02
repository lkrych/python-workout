

def reverse_lines(in_file, out_file):
    fin = open(in_file, "r")
    fout = open(out_file, "w")
    lines = fin.readlines()
    fin.close()
    for line in lines:
        fout.write(f'{line.rstrip()[::-1]}\n')
    fout.close()

reverse_lines("./testdir/test1.txt", "./testdir/test1-rev.txt")
