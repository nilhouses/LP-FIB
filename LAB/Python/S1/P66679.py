#Llistes per comprensió
#[expressió for variable in iterable if expressió]

def my_map(f,L):
   return [f(x) for x in L]

#print(my_map(lambda x: x + 1, [1, 2, 3, 4]))

def my_filter(f,L):
    return [x for x in L if f(x)]

#print(my_filter(lambda x: x % 2 == 1, [1, 2, 3, 4, 5]))

def factors(n):
    return [x for x in range(1,n+1) if n % x == 0]

#print(factors(10))

def triplets(n):
    return [(a,b,c) for a in range(1,n+1) for b in range(1,n+1) for c in range(1,n+1) if a**2 + b**2 == c**2]

#print(triplets(20))