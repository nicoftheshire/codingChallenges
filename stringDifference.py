# A function that accepts two strings: the first being a string of characters
# and the second being the same characters, but in a different order and with
# one extra character. The function returns that character.

def difference(str1, str2):
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                break
