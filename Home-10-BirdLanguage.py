import re
import string

VOWELS = "aeiouy"
CONSONANTS = re.sub("[aeiouy]", "", string.ascii_lowercase)

def translate(phrase):
    for c in CONSONANTS:
        phrase = re.sub( "{}\w".format(c), "{}".format(c), phrase)
    for v in VOWELS:
        phrase = phrase.replace(v*3, v)
    return phrase

if __name__ == '__main__':
    print("Example:")
    print(translate("hieeelalaooo"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
