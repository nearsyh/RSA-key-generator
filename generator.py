import random
import sys

length = 1024
trial = 10

def random_int(l):
    s = 1
    for i in range(l-1):
        s = s * 2 + random.randint(0, 1)
    return s

def powMod(b, e, m):
    s = 1
    while e > 0:
        if e % 2 == 1:
            s = (s * b) % m
        b = (b * b) % m
        e = e / 2
    return s

def miller_rabin_test(p):
    s = 0
    n = p - 1
    while n & 1 == 0:
        s += 1
        n = n >> 1
    d = n
    n = p - 1
    for i in range(trial):
        a = random.randint(1, n)
        for r in range(s):
            if powMod(a, d, p) != 1 and powMod(a, 2**r * d, p) != n:
                return False
    return True

def big_prime(l):
    while True:
        p = random_int(l) | 1
        if miller_rabin_test(p):
            return p

def extended_euclid(a, N):
    s0, t0, r0 = 1, 0, a
    s1, t1, r1 = 0, 1, N
    q = int(a/N)
    while True:
        temp1, temp2, temp3 = s1, t1, r1
        s1 = s0 - q*s1
        t1 = t0 - q*t1
        r1 = r0 - q*r1
        s0, t0, r0 = temp1, temp2, temp3
        if r1 == 0:
            return (s0, t0, r0)
        q = r0/r1


def generateKey(l): 
    print "What is the length of key you want ?"
    print "\t(1) 1024 bits"
    print "\t(2) 2048 bits"
    print "\t(3) 4096 bits"
    choice = int(raw_input())
    length = list([1024, 2048, 4098])[choice - 1]
    sys.stdout.write("generating the first prime\r")
    sys.stdout.flush()
    p = big_prime(l/2)
    print "the first prime generated"
    sys.stdout.write("generating the second prime\r")
    sys.stdout.flush()
    q = big_prime(l-l/2)
    print "the second prime generated"
    phi = (p-1) * (q-1)
    e = big_prime(l/3)
    sys.stdout.write("generating e and d\r")
    sys.stdout.flush()
    while True:
        d, temp, r = extended_euclid(e, phi)
        if r != 1:
            e += 2
            continue
        else:
            break
    print "e and d generated"
    print "n =", p * q
    print "e =", e
    print "d =", d % phi

############### Test ###############
# print bin(random_int(10))
# print big_prime(100)
# print extended_euclid(7, 13)

generateKey(length)
