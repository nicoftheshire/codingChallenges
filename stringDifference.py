# A function that accepts two strings: the first being a string of characters
# and the second being the same characters, but in a different order and with
# one extra character. The function returns that character.

def difference(str1, str2):
    i = 0
    j = 0
    while i < len(str2):
        while j < len(str1):
            if not (str2[i] == str1[j]):
                if j == (len(str1) - 1):
                    return str2[i]
                j += 1
                break
            else:
                i += 1
                j = 0
                break

def main():
    res = difference('eueiieo', 'iieoedue')
    print(res)

main()
