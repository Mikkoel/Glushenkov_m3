def ladder(stairs: list[int], final_stairs: int) -> int:
    paid_to_stairs = [stairs[0], stairs[1], stairs[2]]
    for stairs_cost in stairs[3:]:
        added_value = stairs_cost + min(paid_to_stairs[-1],
                                        paid_to_stairs[-2],
                                        paid_to_stairs[-3])
        paid_to_stairs.append(added_value)
    return paid_to_stairs[final_stairs - 1]

print(ladder([0, 5, 2, 1, 2, 4, 3, 6], 8))
