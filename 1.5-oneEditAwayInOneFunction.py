def insert(str1, str2):
    i1 = 0
    i2 = 0
    dif = False
    while i1 < len(str1) and i2 < len(str2):
        if str1[i1] != str2[i2]:
            if dif:
                return False
            dif = True
            if len(str1) > len(str2):
                i1 += 1
            elif len(str1) < len(str2):
                i2 += 1
            else:
                i1 += 1
                i2 += 1
        else:
            i1 += 1
            i2 += 1
    return True


def one_edit_away(string1, string2):
    string1 = 'bali'
    string2 = 'baalii'
    if len(string1) - len(string2) > 1 or len(string2) - len(string1) > 1:
        return False
    else:
        return insert(string1, string2)


if __name__ == "__main__":
    import sys
    print(one_edit_away(sys.argv[-1], sys.argv[0]))
