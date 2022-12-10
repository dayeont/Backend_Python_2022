def read_data() -> list:
    s = input('Enter elements of a list separated by space ')
    print("\n")
    s = s.split()
    return s


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


def print_result(result: str):
    print(result)


def main():
    s = read_data()
    result = nearest_zero(s)
    print_result(result)


if __name__ == "__main__":
    main()
