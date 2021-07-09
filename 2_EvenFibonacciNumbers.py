fibNumbers = [1, 1]

counter = 1

while fibNumbers[counter] <= 4000000:
    fibNumbers.append(fibNumbers[counter] + fibNumbers[counter - 1])
    counter += 1

sumVal = 0
for x in fibNumbers:
    if x % 2 == 0:
        sumVal += x

print("Problem 2: " + str(sumVal))