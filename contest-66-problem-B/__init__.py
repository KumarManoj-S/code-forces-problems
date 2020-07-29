# Initial code
def get_max_sections_old(array):
    is_increasing = True
    max = 0
    cur_max = 0
    prev = 0
    for i in array:
        if is_increasing:
            if prev <= i:
                cur_max += 1
            else:
                cur_max += 1
                is_increasing = False
        else:
            if prev >= i:
                cur_max += 1
            else:
                is_increasing = True
                cur_max = 2
        prev = i
        if cur_max > max:
            max = cur_max

    return max


# Refactored code
def get_max_sections(array):
    is_increasing = True
    max = 0
    cur_max = 0
    prev = 0
    for i in array:
        if is_increasing:
            if prev > i:
                is_increasing = False
        else:
            if prev < i:
                is_increasing = True
                cur_max = 1
        cur_max += 1
        prev = i
        if cur_max > max:
            max = cur_max

    return max


def calculate_max_sections(array):
    a = get_max_sections(array)
    b = get_max_sections(array[::-1])

    return a if a > b else b


# n = input()
# array = input()
# array = list(map(lambda x: int(x), array.split(' ')))
# print(calculate_max_sections(array))

assert calculate_max_sections([1, 2, 1, 1, 1, 3, 3, 4]) == 6
assert calculate_max_sections([1, 2, 1, 2, 1]) == 3
assert calculate_max_sections([2]) == 1
assert calculate_max_sections([1, 2, 3, 4, 5, 4, 3, 2, 1]) == 9
assert calculate_max_sections([4, 3, 2, 1, 1, 2, 3, 4]) == 5
assert calculate_max_sections([6, 5, 6, 5, 6]) == 3

