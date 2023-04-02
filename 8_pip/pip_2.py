def pin(pins: list[int]) -> int:
    sorted(pins)
    pin_len = []
    intic = 0
    for i in range(1, len(pins) + 1):
        pin_len.append(pins[i] - pins[i - 1])
        if intic > 1:
            min(pin_len[i], pin_len[i-1])
        intic += 1
    sum_pin_len = sum(pin_len)
    return sum_pin_len


print(pin([3, 8, 10, 11, 15, 17]))