from collections import Counter

# My initial attempt:
# Time complexity: O(n)
# Space complexity: O(n)


def palinPerm(word):

    if len(word) < 2:
        return True

    count = Counter(word)
    odd_count = 0

    for key in count:
        if count[key] % 2 == 1:
            odd_count += 1

            if odd_count > 1:
                return False

    return True


def palinPermTrue(word):

    if len(word) < 2:
        return True

    # Create bit vector of size 26, one for each lowercase letter
    bit_vec = [0] * 26

    for ch in word:

        # ^= is the XOR operator. 1 is set to 0, and 0 is set to 1.
        bit_vec[ord(ch) - ord('a')] ^= 1

    odd_count = 0
    for bit in bit_vec:
        if bit:
            odd_count += 1

        if odd_count > 1:
            return False

    return True


print(palinPerm('asdss'))
print(palinPerm('asdsa'))
