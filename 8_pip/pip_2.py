def pin(pins: list[int]) -> int:
    sorted(pins)
    pin_len = []
    for i in range(1, len(pins) + 1):
        pin_len.append(pins[i] - pins[i - 1])
