
sumOfSquares = 0

for i in range(101):
    sumOfSquares += (i * i)

squareOfSum = sum(range(101))
squareOfSum = squareOfSum * squareOfSum

print("Problem 6: " + str(squareOfSum - sumOfSquares))