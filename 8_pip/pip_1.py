def grass_jumper(final: int) -> int:
    steps = [1, 1]
    for i in range(2, final + 1):
        steps.append(steps[i-2] + steps[i-1])
    return steps[final]

print(grass_jumper(6))

def grass_jumper(final: int) -> int:
    steps = [1, 1, 2]
    for i in range(3, final + 1):
        steps.append(steps[i-2] + steps[i-1] + steps[i-3])
    return steps[final]

print(grass_jumper(6))

def grass_jumper_and_stones(final: int, stones: list[int]) -> int:
    steps = [1, 1]
    for i in range(2, final + 1):
        steps.append((steps[i-2] + steps[i-1]) * (i not in stones))
    return steps[final]

print(grass_jumper_and_stones(6, [3, 5]))