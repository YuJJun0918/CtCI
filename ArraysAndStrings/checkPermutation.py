# Given two strings, write a method to decide if one is a permutation of the
# other.

from collections import Counter


# This one uses the Counter() method, which has a general runtime of O(n).
# However, this also has a space complexity of O(n).
def isPerm(word1, word2):

    return Counter(word1) == Counter(word2)


print(isPerm('hi', 'idh'))
