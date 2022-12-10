def read_k() -> int:
    k = int(input('Enter k '))
    print("\n")
    if k < 1 or k > 5:
        print("Wrong k")
        raise Exception
    return k


def read_field() -> list:
    print("Enter elements of field's lines one by one ")
    field = []
    for i in range(0, 4):
        s = input()
        if len(s) != 4:
            print("Wrong length")
            raise Exception
        else:
            for j in s:
                if j != '.':
                    field.append(int(j))
    return field


def sleight_of_hand(k: int, field: list) -> int:
    k = k * 2
    unique = set(field)
    unique_dict = dict.fromkeys(unique, 0)
    for i in field:
        for j in unique_dict.keys():
            if i == j:
                unique_dict[j] += 1
    res = 0
    for j in unique_dict.keys():
        if unique_dict[j] < k:
            res += 1
    return res


def print_result(result: int):
    print(result)


def main():
    k = read_k()
    field = read_field()
    result = sleight_of_hand(k, field)
    print_result(result)


if __name__ == "__main__":
    main()
