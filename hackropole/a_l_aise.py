
import string

alpha = list(string.ascii_uppercase)
alpha_lower = string.ascii_lowercase

def get_index(c):
    try:
        return alpha_lower.index(c)
    except ValueError:
        return -1

def prepare_key(key):
    tb = []
    for i in key:
        tb.append(get_index(i))
    return tb


def encode(input : str, key: str):
    key_tb = prepare_key(key)
    MAX_ITER_KEY = len(key) - 1

    res = []
    iter_key = 0
    for i in input:
        try:
            j = alpha_lower.index(i)
            res.append(alpha_lower[ (j + key_tb[iter_key]) % 26])
            if iter_key < MAX_ITER_KEY:
                iter_key += 1
            else:
                iter_key = 0
        except ValueError:
            res.append(i)
    return "".join(res)

encoded = encode(input="j'adore", key="musique")
print(encoded)

def decode(encoded, key):
    key_tb = prepare_key(key)
    MAX_ITER_KEY = len(key) - 1

    iter_key = 0
    res = []
    for i in encoded:
        try:
            j = alpha_lower.index(i)
            res.append(alpha_lower[ (j - key_tb[iter_key]) % 26 ])
            if iter_key < MAX_ITER_KEY:
                iter_key += 1
            else:
                iter_key = 0
        except ValueError:
            res.append(i)
    return "".join(res)

encoded = "Gqfltwj emgj clgfv ! Aqltj rjqhjsksg ekxuaqs, ua xtwk" + \
"n'feuguvwb gkwp xwj, ujts f'npxkqvjgw nw tjuwcz" + \
"ugwygjtfkf qz uw efezg sqk gspwonu. Jgsfwb-aqmu f" + \
"Pspygk nj 29 cntnn hqzt dg igtwy fw xtvjg rkkunqf."

encoded = encoded.lower()

print(decode(encoded, key="fcsc"))
