import math

aSol = 0
bSol = 0
cSol = 0

solutionFound = False
for a in range(1, 1001):
    for b in range(a, 1001):
        c = math.sqrt(a * a + b * b)
        if (a + b + c == 1000):
            aSol = a
            bSol = b
            cSol = c
            solutionFound = True
            break
    if solutionFound:
        break



print("Problem 9: " + str((aSol * bSol * cSol)))