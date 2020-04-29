def compression(arr):
    result = list()
    i = 0
    while i < len(arr):
        current = arr[i]
        num = 0
        while i < len(arr) and current == arr[i]:
            num += 1
            i += 1
        result.append(current)
        result.append(num)

    return result


print(''.join(str(i) for i in compression('aaaaba')))
