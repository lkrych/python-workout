import pig_latin as pl

def pl_sentence(s: str):
    pl_words = []
    for word in s.split():
        pl_words.append(pl.pig_latin(word))
    return " ".join(pl_words)

print(pl_sentence('this is a test translation'))
