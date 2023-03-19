def grass_hopper(prise: list[int], n: int) -> int:
    prise_min = [prise[0], prise[1] + prise[0]]
    for i in range(2, len(prise)):
        prise_min.append(min(prise_min[i - 1], prise_min[i - 2]) + prise[i])
    return prise_min[-1]


print(grass_hopper([0, 5, 9, 2, 4, 1, 6, 5], 7))