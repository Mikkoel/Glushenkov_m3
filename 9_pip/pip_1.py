from math import inf
def pin(pins: list[int]) -> int:
    pins.sort()
    pins_min = [inf, pins[1] - pins[0]]
    for i in range(2, len(pins)):
        pins_min.append(min(pins_min[i-2], pins_min[i - 1]) + (pins[i] - pins[i - 1]))
    return pins_min[-1]


print(pin([20, 5, 12, 21, 20, 14]))