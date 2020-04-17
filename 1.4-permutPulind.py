def permutation_palindrome(string):
    string = 'acc1vv1bbb'
    letters = dict()
    counts = 0
    for ch in string:
        if ch in letters:
            letters[ch] += 1
        else:
            letters[ch] = 1

    for count in letters.values():
        counts += count % 2
        if counts > 1:
            return False
    return True


if __name__ == "__main__":
    import sys
    print(permutation_palindrome(sys.argv[-1]))
