import string
import enchant


def encrypt(sentance, k):
    letters = list(string.ascii_lowercase)
    new = []
    for index, value in enumerate(list(sentance)):
        new.append(letters[letters.index(value) + k])
    return ''.join(new)


print(encrypt('hello', 4))


def decrypt(sentance):
    letters = list(string.ascii_lowercase)
    d = enchant.Dict('en_US')
    new_sentance = sentance.split(' ')
    for i, val in enumerate(new_sentance):
        current = 0
        for index in range(26):
            for x in val:
                if letters.index(x) + index > 26:
                    index = 26 - letters.index(x)
                    print(index)


print(decrypt('lipps'))