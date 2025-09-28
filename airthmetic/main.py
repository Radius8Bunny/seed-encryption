import random

ops = ["+", "-", "*", "/"]
seed = 41

def get_pn(ops):
    p = 0
    n = 0
    
    return (p, n)

def intent(rs, ops):
    chain = []
    i = 0
    while i < len(rs):
        chain.append(ops[rs[i]])
        i += 1
    return chain 

def ret_rand(level):
    i = 0
    rs = []
    while i < level:
        r = random.randrange(0, 4)
        rs.append(r)
        i += 1
    return rs

def main(i):
    rs = ret_rand(8)
    chain = intent(rs, ops)
    get_pn(chain)
    return chain

num = 2
out = main(num)