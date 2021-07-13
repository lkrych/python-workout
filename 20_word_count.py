import sys

def word_count(filename):
    # number of characters
    # number of words
    # number of lines
    # number of unique words
    chars, words, lines, unique = 0, 0, 0, set()
    with open(filename) as f:
        for line in f:
            lines += 1
            chars += len(line)
            # word computation
            split_words = line.split(" ")
            words += len(split_words)
            unique.update(split_words)

    print(f'wc for {filename}')
    print(f'lines: {lines}')
    print(f'chars: {chars}')
    print(f'words: {words}')
    print(f'unique words: {len(unique)}')



if __name__ == "__main__":
    word_count(sys.argv[1])
