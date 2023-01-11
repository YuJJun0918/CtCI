a = 'abdd'
b = 'abcd'


def oneAway(a, b):

    if a == b:
        return True

    return ins(a, b) or replace(a, b)


def ins(a, b):
    if abs(len(a) - len(b)) != 1:
        return False

    if len(a) > len(b):
        return b in a

    else:
        return a in b


def replace(a, b):
    if len(a) != len(b):
        return False

    diff_count = 0

    for i in range(len(a)):
        if a[i] != b[i]:
            diff_count += 1

        if diff_count > 1:
            return False

    return True


print(oneAway(a, b))
