def nearest_zero(s: list) -> str:
    ind = []
    for i, x in enumerate(s):
        if x == '0':
            ind.append(i)

    result = []
    for i, x in enumerate(s):
        if x != '0':
            dif = []
            for n in ind:
                res = n - i
                if res < 0:
                    res = -res
                dif.append(res)
            if bool(dif) is True:
                result.append(min(dif))
            else:
                result.append(0)
        else:
            result.append(0)

    return ' '.join(map(str, result))


def main():
    s = input('Enter elements of a list separated by space ')
    print("\n")
    s = s.split()
    result = nearest_zero(s)
    print(result)


if __name__ == "__main__":
    main()
