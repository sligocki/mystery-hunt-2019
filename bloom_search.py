import string

offset = 14695981039346656037
multiplier = 1099511628211
mask = 2**64 - 1

def FNV_1a_64bit(str):
    val = offset;
    l = len(str)

    for c in str:
        val = (((val ^ ord(c)) * multiplier) & mask);

    return val;  

primeTable = [
    2196119, 2734343, 1503683, 1126787, 2249053, 1024921, 1444943, 2031223, 
    2887777, 1717099, 4111633, 1816337, 1565261, 4990243, 2503327, 1616827, 
    1968017, 2816969, 3403613, 1363717, 5012243, 1082717, 1136717, 2621669, 
    3157577, 5737961, 1042523, 2188409, 1330487, 1422923, 1047131, 1143647, 
    2021629, 3838477, 3525377, 4735589, 7042933, 1801433, 2923367, 1144399, 
    1594261, 2709601, 3307609, 
];

bitVector = [
    0x3e13e58b, 0xb93064dd, 0x3b3a13c2, 0x43c17b17, 0x77c8170f, 0x72d684f3, 0x4e94bde3, 0x178ea819, 
    0x9c643453, 0xe7e1f598, 0x0953e1d4, 0xc26a17da, 0xb5281dd5, 0x83fcd020, 0xdf5b8585, 0x7cfc9c7d, 
    0x4326ebfa, 0x44ef1acb, 0x5397a9d1, 0x541d641b, 0xf1cc70f0, 0xe7debb71, 0xfdadfc8d, 0x703d5b23, 
    0x91e7b18e, 0x6adeb3d1, 0x17f2f1da, 0x66b75403, 0xb34d986b, 0xcac1c344, 0x39b7cd33, 0x9a8ea8fc, 
    0x8b3aac29, 0xfc4a4997, 0xf6554b0d, 0x4d31de6a, 0x7d121515, 0xff25b2a3, 0xb19185fa, 0xfea0fe00, 
    0xc795909a, 0x3e007be3, 0x458562f1, 0x5807a052, 0xf9edd76e, 0x2b912489, 0xcc3af4d3, 0xec353c96, 
    0x319d21b1, 0xf4d8d832, 0x3737f8a3, 0xabc4b4aa, 0xedeb3062, 0x03faf091, 0x75e9879e, 0xa283f707, 
    0xf1819b7f, 0x4ccbfd1b, 0xc8e9c576, 0x9fea7800, 0x095d1f42, 0x311af940, 0xe8ce5b49, 0xe46d4fef, 
    0xaabea74a, 0x5e9fc668, 0xaa0ca532, 0xf0902b05, 0x165be527, 0xca9c9474, 0xf078def1, 0x0663a350, 
    0x62952874, 0x40aec582, 0x84b07c16, 0xa5e772a5, 0xd72523b7, 0xf831cc58, 0xce9af317, 0xdca9997e, 
    0x5fdf8d2f, 0x55cff37e, 0xac50b3e1, 0x217b3a2a, 0x9ed334a9, 0xb4199163, 0x69270573, 0xb3c63b38, 
    0xb9e6eb67, 0xf67a2cc4, 0x8b527cfc, 0x1b69a598, 0x0cd1f9ec, 0xd6f0a25b, 0x7a6396d8, 0xef27d441, 
    0x27d9e083, 0xb7724e16, 0x24939fba, 0x4f862321, 0x83deba38, 0x91a2abb1, 0xa16bea81, 0xb688aece, 
    0x0f6a3764, 0x325531cd, 0x832c3c30, 0x02167d30, 0x349314e6, 0x29d04e45, 0x01eef553, 0x4587d7c1, 
    0x1ca6f9c3, 0x6f1b3f66, 0x55faba32, 0x4d1b6af3, 0x005b3030, 0x2c975110, 0xb3953d5b, 0xdce5cfd1, 
    0xfd3f173b, 0x2fba9dc0, 0xb1108b7b, 0x414d78a6, 0x7765fbc8, 0xd2bdb9f1, 0x141986df, 0xc5c8ec43, 
]

bitVectorLength = len(bitVector) * 32

def bitAt(pos):
    return (bitVector[pos >> 5] >> (31 - (pos & 31))) & 1;

def hash(row, prime):
    s = row.lower()
    h = FNV_1a_64bit(s) % prime

    return h % bitVectorLength;

def checkWord(s):
    for prime in primeTable:
        if bitAt(hash(s, prime)) == 0:
            return False

    return True


import sys
str = sys.argv[1]
print(checkWord(str))
