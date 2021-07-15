import os

def find_longest_word(filename):
    longest_word = ''
    with open(filename) as f:
        for line in f:
            for word in line.strip().split():
                if len(word) > len(longest_word):
                    longest_word = word
    return longest_word


def find_all_longest_words(dirname):
    longest_words = {}
    for _, _, files in os.walk(dirname):
        for file in files:
            long = find_longest_word(dirname + "/" + file)
            longest_words[file] = long
    return longest_words

print(find_all_longest_words("./testdir"))
