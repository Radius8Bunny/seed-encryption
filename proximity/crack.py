def getDivisors(n):
    
    # Create a list to store divisors
    divisors = []

    # Iterate from 1 to n and check divisibility
    for i in range(1, n + 1):
        if n % i == 0:
            
            # If 'i' divides 'n' evenly, it's a divisor
            divisors.append(i)

    return divisors


o = 673190557079056 #output  PROVIDE
i = 1
ctr = 1
while o > 0:
    o -= i
    i+=2
    ctr +=1

#going back 1 iteration
i -= 2
ctr -= 1

fstart = 8 # input (n) PROVIDE
fstop = (fstart + i) + 1
divisors = getDivisors(fstop)
l = len(divisors) - 1

while (l != 0):
    buffer = 1
    if (divisors[l] == divisors[l-1]+1):
        j = l
        while (j > l - fstart):
            buffer*= divisors[j]
            j -=1
        if (buffer == fstop):
            print("seed is", divisors[l])
            break
    l -=1