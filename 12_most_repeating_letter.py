from collections import Counter

def most_repeating_letter(seq):
    most_repeat = ('none', 0)
    most_repeat_s = None
    for word in seq:
        most_common = Counter(word).most_common(1)[0]
        if most_common[1] > most_repeat[1]:
            most_repeat = most_common
            most_repeat_s = word

    return most_repeat_s, most_repeat

print(most_repeating_letter(['this', 'is', 'an', 'elementary', 'example']))
