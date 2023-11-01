from enum import Enum
from typing import Callable

def shortest_employee_name(employees: list[str]) -> str:
    """
    Args:
        employees: List of employee names.

    Returns:
        The shortest employee name.
    """
    shortest_length = len(employees[0])
    shortest_name = ""

    for e in employees:
        if len(e) <= shortest_length:
            shortest_length = len(e)
            shortest_name = e

    return shortest_name

def longest_employee_name(employees: list[str]) -> str:
    """
    Args:
        employees: List of employee names.

    Returns:
        The longest employee name.
    """
    longest_length = 0
    longest_name = ""

    for e in employees:
        if len(e) > longest_length:
            longest_length = len(e)
            longest_name = e
            
    return longest_name

def sort_name_on_length(employees: list[str]) -> tuple[str]:
    """
    Returns:
        A tuple containing `employees` sorted from longest to shortest and shortest to longest (in that order.)
    """
    asc = employees.copy()
    desc = employees.copy()
    asc.sort(key=len)
    desc.sort(key=len, reverse=True)
    return (desc, asc)

class Order(Enum):
    ASCENDING = "ascending"
    DESCENDING = "descending"

def sort_strings(string_list: list[str], order: Order, key) -> list[str]:
    sorted: list[str] = string_list.copy()
    sorted.sort(key=key, reverse=order == Order.DESCENDING)
    return sorted

def insert_into_sorted(new_employee: str, employees: list[str]) -> list[str]:
    """
    Args:
        employees: Names of emloyees sorted into ascending order based on name length.
    
    Returns:
        Sorted list of `employees` with the new `employee` inserted at the correct position.
    """
    new_list = []
    left_off_at: int = -1

    for i in range(len(employees)):
        if len(employees[i]) > len(new_employee):
            new_list.append(new_employee)
            left_off_at = i
            break
        new_list.append(employees[i])

    for i in range(left_off_at + 1, len(employees)):
        new_list.append(employees[i])

    return new_list

def sort(items: list[object], less_than: Callable[[object, object], bool] = lambda left, right: left < right, ascending: bool = True) -> list:
    """
    Sorts items according to the function provided.

    Args:
        items: The items to be sorted.
        less_than: Used to compare items. Should return `True` if the item on the left comes before the item on the right.
        ascending: `True` = sorts the `items` in ascending order (items with lower values at the start); `False` = sort the `items` in descending order (items with higher values at the start).

    Returns:
        The sorted `items`.
    """

    # Base case.

    if len(items) == 1:
        return items

    # Split.

    mid = len(items) // 2
    left = sort(items.copy()[:mid], less_than, ascending)
    right = sort(items.copy()[mid:], less_than, ascending)

    # Merge and sort until one of left/right has been fully merged in.

    l = 0
    r = 0
    result = []

    while (l < len(left)) and (r < len(right)):
        if (less_than(left[l], right[r]) and ascending) or ((not less_than(left[l], right[r])) and (not ascending)):
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1

    # Add remaining items.

    while l < len(left):
        result.append(left[l])
        l += 1
    
    while r < len(right):
        result.append(right[r])
        r += 1

    # Return result.

    return result

#==============#
# MAIN PROGRAM #
#==============#

employees = ['Li', 'John','Hannah','Alaa','Georgia']

# TESTING

shortest = shortest_employee_name(employees)
longest = longest_employee_name(employees)
employees_desc, employees_asc = sort_name_on_length(employees)
#sorted = sort_strings(employees, Order.ASCENDING, key=len)
sorted = sort(employees, lambda l, r: len(l) < len(r), False)
with_new_name = insert_into_sorted("Paul", employees_asc)

print(f"""Shortest employee name: {shortest}
Longest employee name: {longest}
Employee names sorted on length (ascending): {employees_asc}
Employee names sorted on length (descending): {employees_desc}
Employee names sorted on length (ascending): {sorted}
List after adding employee: {with_new_name}
""")