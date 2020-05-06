import math 

number = input("Enter your number: ")

def primeCalculator(number):
    if number < 2:
        return False
    
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

print (primeCalculator(2))
print (primeCalculator(4))

## Sieves algorithm

def primeSieve(sieveSize):
    sieve = [True] * sieveSize
    sieve[0] = False
    sieve[1] = False

    for i in range(2, int(math.sqrt(sieveSize)) + 1):
        pointer = i * 2
        while pointer < sieveSize:
            sieve[pointer] = False
            pointer += i
    
    primes = []
    for i in range(sieveSize):
        if sieve[i] == True:
            primes.append(i)
    return primes

print(primeSieve(100))