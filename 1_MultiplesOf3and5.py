
counter = 1
multiplesList = []

while counter < 1000:
    if counter % 3 == 0 or counter % 5 == 0:
        multiplesList.append(counter) 

    counter += 1

sumVal = 0
for x in multiplesList:
    sumVal += x

print("Problem 1: " + str(sumVal))