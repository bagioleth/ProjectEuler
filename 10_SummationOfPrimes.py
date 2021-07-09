#takes an hour to get the answer. Really bad

#borrowed from problem 7
def isPrime(x):
    isPrime = True
    for i in range(3, x, 2):
        if x % i == 0:
            isPrime = False
            break
    return isPrime

sumVal = 2

for i in range(3, 2000000, 2):
    if isPrime(i):
        sumVal += i
    if i % 9999 == 0:
        print(i)

print("Problem 10: " + str(sumVal))