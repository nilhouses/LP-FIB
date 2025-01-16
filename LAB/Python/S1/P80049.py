#Ús d'iterables
from functools import reduce

def count_unique(L):
    return len(set(L))
    #MASSA PAJA
    #u = 0
    #unics = []
    #for e in L:
    #    if e not in unics:
    #        u += 1
    #        unics.append(e)
    #return u

def remove_duplicates(L):
    return set(L)

def flatten(L):
    return reduce(lambda acc, l: acc+l , L,[]) #donat acc i l els concatena, i passo els parámetres

def flatten_rec(L):
    f = lambda acc, l: acc+flatten_rec(l) if isinstance(l,list) else acc + [l]
    return reduce(f,L,[])
