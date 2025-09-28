import math

def paired(ls):
    pairs = []
    i = 0
    while i < len(ls):
        n1 = ls[i]
        n2 = ls[len(ls)- i - 1]
        tup = (n1, n2)
        pairs.append(tup)
        i += 1
    return pairs

def chop(pairs, i):
    ls = []
    f = 0
    while f < i:
        ls.append(pairs[f])
        f += 1
    return ls

def get_pairs(seed, n):
    f_start = n
    f_stop = int(math.factorial(seed)/math.factorial(seed-n))
    k_ls = list(range(f_start, f_stop))
    S = paired(k_ls)
    c_i = len(S)/2
    PS = chop(S, c_i)
    return PS

def unpack(pairs):
    i = 0 
    unp = []
    while i < len(pairs):
        x1, x2 = pairs[i]
        md = abs(x1 - x2)
        unp.append(md)
        i += 1
    return unp

def resolve(u_p):
    r = sum(u_p)
    return r

seed = 13 # always odd
n = 8    # always even
pairs = get_pairs(seed, n)
unp = unpack(pairs)
print(resolve(unp))