#Funcions amb llistes
#python3
# from P51956 import *

from functools import reduce

def myLength(L):
    length = 0
    for _ in L:
        length += 1
    return length

def myMaximum(L):
    def max(a,b):
        if a > b:
            return a
        else:
            return b
    return reduce(max,L)

def average(L):
    def suma(x, y): return x + y
    acumulador = reduce(suma, L, 0)
    return acumulador/myLength(L)


def buildPalindrome(L):
    R = []
    for l in L:
        R.insert(0,l)
    return R + L


def remove(L1, L2):
    return [x for x in L1 if x not in L2]

def flatten(L):
    res = []
    for l in L:
        if (isinstance(l, list)):
            res = res + flatten(l)
        else:
            res.append(l)
    return res

def oddsNevens(L):
    odds = list(filter(lambda x: x%2 != 0,L))
    evens = list(filter(lambda x: x%2 == 0,L))
    return (odds,evens)

#de l'exercici anterior#########
def isPrime(x):
    if x == 0 or x == 1:
        return False
    
    for i in range(2,x):
        if x % i == 0:
            return False
    return True
#################################
def primeDivisors(n):
    R = []
    for i in range(1,n+1):
        if n % i == 0 and isPrime(i):
            R.append(i) 
    return R
