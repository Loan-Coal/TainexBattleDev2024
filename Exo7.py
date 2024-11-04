#NE PAS TOUCHER
keys = ['v622w7x344f5', '37c3yq47c87', '8g1s2r88vb2', '7o26nc15k2aa1', 'a98189rbu4', 'bf873h93e3', '26b8s7eq1p93v', 'f6dd38l7942']
#NE PAS TOUCHER


dico = {
    '0':0 , '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15, 'g': 16, 'h': 17, 'i': 18, 'j': 19,
    'k': 20, 'l': 21, 'm': 22, 'n': 23, 'o': 24, 'p': 25, 'q': 26, 'r': 27, 's': 28, 't': 29,
    'u': 30, 'v': 31, 'w': 32, 'x': 33, 'y': 34, 'z': 35
}

dico_reverse = {
    0:'0' , 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
    10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f', 16: 'g', 17: 'h', 18: 'i', 19: 'j',
    20: 'k', 21: 'l', 22: 'm', 23: 'n', 24: 'o', 25: 'p', 26: 'q', 27: 'r', 28: 's', 29: 't',
    30: 'u', 31: 'v', 32: 'w', 33: 'x', 34: 'y', 35: 'z'
}

result = ''
values = []
keys_duo = []


for i in range(len(keys)):

    c = sum(dico[char] for char in keys[i])

    values.append(format(c, '08b'))


for p in range(len(values)-1):

    for q in range(p+1, len(values)):

        n = ''

        for r in range(len(values[p])):

            n += '1' if values[p][r] == values[q][r] else '0'

        keys_duo.append(n)


keys_duo = sorted(set(keys_duo))

for d in range(len(keys_duo)):

    keys_duo[d] = int(keys_duo[d] , 2) % 36


for a in keys_duo:
    result += dico_reverse[a]

print(result)