from prime import is_probable_prime
from math import sqrt,ceil
import random


#Exercice 1
#Q1
def bezout(a, b):
    u0,v0,u1,v1=0,1,1,0
    while(a!=0):
        q, b, a = b // a, a, b % a
        v0, v1 = v1, v0 - q * v1
        u0, u1 = u1, u0 - q * u1

    return b,u0,v0


#Q2
def inv_mod(a, n):
    pgcd,x,y=bezout(a,n)
    if(pgcd==1):
        return x
    return None


def invertibles(N):
    l=[]
    for i in range(N):
        if(inv_mod(i,N)!=None):
            l.append(i)
    return l


#Q3
def phi(N):
    return len(invertibles(N))


#Exercice 2
#Q1
def exp(a, n, p):
    res =1
    while n > 0:
        if n % 2 == 1:
            res = (res * a) % p
        a = (a * a) % p
        n = n // 2

    return res


#Q2
def factor(n):
    facteurs = []
    diviseur = 2
    while diviseur <= n:
        if n % diviseur == 0:
            exposant = 0
            while n % diviseur == 0:
                n //= diviseur
                exposant += 1
            facteurs.append((diviseur, exposant))
        else:
            diviseur += 1
    
    return facteurs


#Q3
def order(a, p, factors_p_minus1):

    a %= p
    order_a = p - 1
    for (diviseur, exposant) in factors_p_minus1:
        order_a //= diviseur**exposant
        a2 = exp(a, order_a, p)
        for i in range(exposant + 1):
            if a2 == 1:
                break
            a2 = exp(a2, diviseur, p)
            order_a *= diviseur
    return order_a


#Q4
def find_generator(p, factors_p_minus1):
    a = random.randint(0, p - 1)
    while order(a, p, factors_p_minus1) != p - 1:
     a = random.randint(0, p - 1)
    return a


#Q5
def generate_safe_prime(k):
    p = random.randint(2**(k-1), 2**k - 1)
    while not (is_probable_prime(p) and is_probable_prime(2 * p + 1)):
        p = random.randint(2**(k-1), 2**k - 1)
    return 2 * p + 1


#Q6
def bsgs(n, g, p):
    s = int(sqrt(p)) + 1
    tabg = dict()
    gs = exp(g, s, p)
    invgs = inv_mod(gs, p)
    tabg[n] = 0
    v = n
    for q in range(s):
        tabg[v] = q
        v = (v * invgs) % p
        tabb = 1
    for r in range(s):
        if tabb in tabg:
            log = (r + tabg[tabb] * s) % (p - 1)
            return log
        tabb = (tabb * g) % p
