from collections import Counter
from itertools import product

valid = []
rejected = []

with open('passphrases.txt') as passphrases:
    passphrases = passphrases.readlines()

    for phrase in passphrases:
        phrase = phrase.strip().split()
        if len(set(phrase)) == len(phrase):
            valid.append(phrase)
        else:
            rejected.append(phrase)

print(f'Number of phrases: {len(passphrases)}')
print(f'Number of valid: {len(valid)}')
print(f'Number of rejected: {len(rejected)}')


# Part Two

def is_anagram(word1, word2: str) -> bool:
    c1 = Counter(word1)
    c2 = Counter(word2)
    if list(c1) == list(c2):
        print(word1, word2)
    return c1 == c2


valid_anagram = []
rejected = []

for phrase in valid:
    reject = False
    for word1, word2 in product(phrase, phrase):
        if phrase.index(word1) == phrase.index(word2):
            continue
        if len(word1) != len(word2):
            continue

        if is_anagram(word1, word2):
            rejected.append(phrase)
            reject = True
            break

    if not reject:
        valid_anagram.append(phrase)

print(f'Number of valid, non-anagram: {len(valid_anagram)}')
