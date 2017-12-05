
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
        print(phrase)
#
# print(valid)
# print(rejected)
print(f'Number of phrases: {len(passphrases)}')
print(f'Number of valid: {len(valid)}')
print(f'Number of rejected: {len(rejected)}')
