# copyfile takes one mandatory argument -> the input file
# additional arguments -> name of files to which file should be copied
def copyfile(src, *args):
    if len(args) == 0:
        print(f'No destination to copy {src} to')
    
    with open(src, 'r') as fsrc:
        for dst in args:
            fsrc.seek(0)
            print(f'writing to {dst}')
            with open(dst, 'a') as fdst:
                for line in fsrc.readlines():
                    fdst.write(line)


copyfile('./testdir/test1.txt', './testdir/test1-copy1.txt', './testdir/test1-copy2.txt')
