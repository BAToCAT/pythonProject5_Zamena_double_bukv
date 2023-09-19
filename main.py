from collections import Counter
import string

def replace_duplicates(s):
    alphabet = string.ascii_lowercase * 2
    while len(s) != len(set(s)):
        counter = Counter(s)
        mc = counter.most_common(1)[0]
        k, v = mc
        if v > 1:
            v -= 2
        counter[k] = v
        alph_ind = alphabet.find(k) + 1
        s = alphabet[alph_ind] + "".join([k*v for k, v in counter.items()])
    return s