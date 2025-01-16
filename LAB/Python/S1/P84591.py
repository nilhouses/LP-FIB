#Funcions amb nombres
#python3 P84591.py

def absValue(x):
    if x < 0:
        return -x
    else: 
        return x

#print("Valor absolut de -666: ", absValue(-666))

def power(x,p):
    return x**p

#print("2Â³ = ", power(2,3))

def isPrime(x):
    if x == 0 or x == 1:
        return False
    
    for i in range(2,x):
        if x % i == 0:
            return False
    return True

#print("isPrime 17 = ",isPrime(3))

def slowFib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return slowFib(n-1) + slowFib(n-2)

#print(slowFib(5))

def fib(n):
    if n < 2:
        return (0,n)
    (f2,f1) = fib(n-1)
    return  (f1,f1+f2)


def quickFib(n):
    return fib(n)[1] # retorna ([0],[1]), i vull [1]


#print(quickFib(5))