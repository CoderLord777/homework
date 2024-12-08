from itertools import *


def all_variants(text):
    text = text.lower()
    for i in range(1, len(text) + 1):
        for j in combinations(text, i):
            yield ''.join(j)


a = all_variants("abc")
for i in a:
    print(i)
