
def pin(pins: list[int]) -> int:
    pins.sort()
    pins_len = [pins[0] + pins[1]]
    nets = round(len(pins) / 2)
    pin_nets = 1
    pin_net = [1, 0]
    i = 1
    end = nets - 1
    while nets != pin_nets and pin_net[-1] != 1:
        much = (pins[i + 1] - pins[i])
        mini = (pins[i] - pins[i - 1])
        if pin_net[i] != 0 and much > mini:
            pins_len.append(pins[i - 1] - pins[i])
            pin_nets += 1
            pin_net[i] = 1
        elif pin_net[i] != 0 and much <= mini:
            pins_len.append((pins[i] - pins[i - 1]) + pins_len[i])
            pin_nets += 1
            pin_net[i] = 1
        i += 1
        pin_net.append(0)
    return pins_len[-1]


print(pin([20, 5, 12, 21, 20, 14]))
