#very inefficient as only increments by 20 each time it checks, may be able to find primes and use those better for bigger increments

counter = 20
solutionFound = False

while solutionFound == False:
    solutionFound = True
    for i in range(1, 21):
        if counter % i != 0:
            counter += 20
            solutionFound = False
            break
    if(solutionFound):
        break

print("Problem 5: " + str(counter))