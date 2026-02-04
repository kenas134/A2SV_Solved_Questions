def swap_case(s):
    arr = []
    for i in s:
        if i.upper() == i:
            arr.append(i.lower())
        else:
            arr.append(i.upper())
    return "".join(arr)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
