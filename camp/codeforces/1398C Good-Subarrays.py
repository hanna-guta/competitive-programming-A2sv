for _ in range(int(input())):
    n = int(input())
    a = input()

    hash_map = {0: 1}
    res = 0
    summ = 0

    for i in range(n):
        summ += int(a[i])

        comp = summ - i - 1

        if comp not in hash_map:
            hash_map[comp] = 0

        hash_map[comp] += 1
        res += hash_map[comp] - 1

    print(res)
