
def isPalindrome(x):
    val = str(x)
    if val == val[::-1]:
        return True
    else: 
        return False

possiblePalindromes = []
for val1 in range(999, 99, -1):
    for val2 in range(999, 99, -1):
        possiblePalindromes.append(val1 * val2)

answer = 0
possiblePalindromes.sort()
for i in range(len(possiblePalindromes) - 1, 0, -1):
    if isPalindrome(possiblePalindromes[i]):
        answer = possiblePalindromes[i]
        break

print("Problem 4: " + str(answer))
