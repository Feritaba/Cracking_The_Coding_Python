def replace(str1, str2):
    difference = False
    for ch in range(len(str1)):
        if str1[ch] != str2[ch]:
            if difference:
                return False
            difference = True
    return True


def insert(str1, str2):
    i1 = 0
    i2 = 0
    while i1 < len(str1) and i2 < len(str2):
        if str1[i1] != str2[i2]:
            if i1 != i2:
                return False
            i2 += 1
        else:
            i1 += 1
            i2 += 1
    return True


def one_edit_away(string1, string2):
    string1 = 'pale'
    string2 = 'palee'
    if len(string1) == len(string2):
        return replace(string1, string2)
    elif len(string1) + 1 == len(string2):
        return insert(string1, string2)
    elif len(string1) - 1 == len(string2):
        return insert(string1, string2)
    return False


if __name__ == "__main__":
    import sys
    print(one_edit_away(sys.argv[-1], sys.argv[0]))
