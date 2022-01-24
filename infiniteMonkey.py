import random as rand

def generateString(strlen):
    digits = 'abcdefghijklmnopqrstuvwxyz '
    result = ''

    for i in range(strlen):
        result += digits[rand.randrange(27)]
        
    return result

def score(str, targetString):
    similar  = 0
    for i in range(len(str)):
        if (str[i] == targetString[i]):
            similar += 1

    score = similar / len(str)
    return score

def main():

    finalScore = 0
    finalString = ''
    for i in range(1000):
        targetString = 'a computer science portal for geeks'
        genString = generateString(len(targetString))
        newScore = score(genString, targetString)
        if (newScore > finalScore):
            finalScore = newScore
            finalString = genString

    print('Target: ' + targetString + '\n')
    print('Result: ' + finalString + '\n')
    print('Score: ' + str(finalScore))

main()
