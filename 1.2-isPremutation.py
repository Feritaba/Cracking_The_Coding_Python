def check_permutation(s1, s2):
    s1 = ' Aab'
    s2 = 'baA '
    if len(s1) != len(s2):
        return False
# check if the two strings have identical character counts
    perm_dict = dict()
    for char in s1:
        if char in perm_dict:
            perm_dict[char] += 1
        else:
            perm_dict[char] = 1

    for char in s2:
        if char in perm_dict:
            perm_dict[char] -= 1

    for char in perm_dict:
        if perm_dict[char] != 0:
            return False

    return True


if __name__ == "__main__":
    import sys
    print(check_permutation(sys.argv[-1], sys.argv[0]))