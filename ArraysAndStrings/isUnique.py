# Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures?

def isUnique(word):  # This uses a hash table

    if len(word) > 128:  # There are 128 chars, you cannot have a unique set if word length > 128
        return False

    table = {}
    for letter in word:

        if letter not in table:
            table[letter] = 1

        else:
            return False

    return True


def isUniqueWithoutDataStruct(word):  # We will use a bit vector

    if len(word) > 128:
        return False

    boolArr = [False for i in range(129)]

    for i in range(len(word)):

        val = ord(word[i])

        if boolArr[val]:
            return False

        else:
            boolArr[val] = True

    return True


print(isUnique('hello!'))
print(isUniqueWithoutDataStruct('hello'))
