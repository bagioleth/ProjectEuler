

def isPrime(x):
    isPrime = True
    for i in range(2, x):
        if x % i == 0:
            isPrime = False
            break
    return isPrime

counter = 0
possiblePrime = 3
primes = [2]

while counter < 10001:
    if isPrime(possiblePrime):
        primes.append(possiblePrime)
        counter += 1
    possiblePrime += 2

print("Problem 7: " + str(primes[10000]))
