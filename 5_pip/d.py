def vertical(dual_list: list[list[int]]) -> list[list[int]]:
    for i in range(len(dual_list)):
        dual_list[i] = dual_list[i][::-1]
    return dual_list


def hotrizontal(dual_list: list[list[int]]) -> list[list[int]]:
    dual_list = dual_list[::-1]
    return dual_list

print(vertical([[1,2], [3,4]]))

print(hotrizontal([[1,2], [3,4]]))

