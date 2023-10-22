def check_element_present(search_params: (list[object], object)) -> bool:
    return search_params[0].__contains__(search_params[1])

def remove_duplicates(values: list) -> list:
    return list(set(values))

def common_elements(list1: list, list2: list) -> list:
    return list(set(list1).intersection(list2))

def my_numbers(values: list[int]) -> list[tuple[int, bool]]:
    tuple_list = []
    for v in values:
        if (v % 2) == 0:
            parity = "even"
        else:
            parity = "odd"
        tuple_list.append((v, parity))
    return tuple_list

def descending(low: int, high: int) -> list[int]:
    result = []
    for i in range(high, low - 1, -1):
        result.append(i)
    return result

#Tests:
print(check_element_present(([1,2,3,4,5],0)))
print(remove_duplicates([1,2,1,1,1,1,3,4]))
print(common_elements([1,2,3,4], [3,4,5,6]))
print(my_numbers([3,6,1,12]))
print(descending(2, 4))