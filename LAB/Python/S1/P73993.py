#Funcions d'ordre superior

# ATENCIO, a reduce es com si els paràmetres estéssin donats la volta, primer x i després acc

from functools import reduce

def evens_product(L):
    return reduce(lambda acc, x: acc*x if x%2 == 0 else acc, L, 1)    

#print(evens_product([1,2,4,3]))

def reverse(L):
    return reduce(lambda acc, x: [x] + acc, L, []) # x de L i acc = []

#print(reverse([1,2,3]))

def zip_with(f,L1,L2):
    return [f(x,y) for (x,y) in zip(L1,L2)]

#print(zip_with(lambda x, y: x * y, [1, 2, 3], [10, 2]))

def count_if(f,L):
    return len([x for x in L if f(x)])

#print(count_if(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]))