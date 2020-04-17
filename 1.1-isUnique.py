# first ask the interviewer if the string is ASCII or Unicode string


def is_unique(string):
    if len(string) > 128:
        return False

    letters = dict()
    for letter in string:
        if letter in letters:
            return False
        letters[letter] = True
    return True


if __name__ == "__main__":
    import sys
    print(is_unique('abc'))