def pin(pins: list[int]) -> int:
    pins.sort()
    pins_len = []
    for i in range(len(pins) + 1):

        pins_len.append(pins[i] + pins[i + 1])



print(pin([30, 5, 12, 21, 20, 14]))