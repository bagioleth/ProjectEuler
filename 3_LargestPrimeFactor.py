
number = 600851475143

counter = 2
primeFactors = []

while number >= counter:
    if number % counter == 0:
        if counter not in primeFactors:
            primeFactors.append(counter)
        number = number / counter
    else:
        counter += 1

print("Problem 3: " + str(primeFactors[len(primeFactors) - 1]))
