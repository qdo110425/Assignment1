# Name: Quyen Do
# OSU Email: doq@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Python Fundamentals Review
# Due Date:
# Description:


from static_array import StaticArray
arr = StaticArray

# ------------------- PROBLEM 1 - MIN_MAX -----------------------------------


def min_max(arr):
    """
    Represents function that receives an array of integers and returns a tuple with two values -
    the minimum and maximum values of the input array
    """
    if not arr or arr.length() == 0:
        return None     # handle empty array if necessary

    min_value = max_value = arr[0]
    for index in range(1, arr.length()):
        num = arr[index]    # arr is a list of integers
        if num < min_value:
            min_value = num
        elif num > max_value:
            max_value = num

    return min_value, max_value


print('\n# min_max example 3')
test_cases = ([3, 3, 3],[-10, -30, -5, 0, -10], [25, 50, 0, 10])
for case in test_cases:
    arr = StaticArray(len(case))
    for i, value in enumerate(case):
        arr[i] = value
    print(arr)
    result = min_max(arr)
    if result:
        print(f'Min: {result[0]: 3}, Max: {result[1]}')
    else:
        print('min_max() not yet implemented')

# ------------------- PROBLEM 2 - FIZZ_BUZZ ---------------------------------


def fizz_buzz(arr):
    """
    Represents a function that receives a StaticArray of integers and returns a new StaticArray object
with the content of the original array:
    """
    new_array = StaticArray(arr.length())

    for i in range(arr.length()):
        num = arr[i]

        if num % 3 == 0 and num % 5 == 0:  # both a multiple of 3 of 5, new array will be the string ‘fizzbuzz’
            new_array[i] = 'fizzbuzz'
        elif num % 3 == 0:  # if divisible by 3, the new array will be the string ‘fizz’
            new_array[i] = 'fizz'
        elif num % 5 == 0:  # if divisible by 3, the new array will be the string ‘fizz’
            new_array[i] = 'buzz'
        else:
            new_array[i] = num

    return new_array


source = [_ for _ in range(-5, 20, 4)]
arr = StaticArray(len(source))
for i, value in enumerate(source):
    arr[i] = value
print(fizz_buzz(arr))
print(arr)


# ------------------- PROBLEM 3 - REVERSE -----------------------------------

def reverse(arr):
    """
    Represents a function that receives a StaticArray and reverses the order of the elements in the
array
    """
    start, end = 0, arr.length() - 1  # initialize 2 pointers, one at the beginning and one at the end
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]  # swap elements are the start and end of pointers
        # move pointers towards the center
        start += 1
        end -= 1


source = [_ for _ in range(-20, 20, 7)]
arr = StaticArray(len(source))
for i, value in enumerate(source):
    arr.set(i, value)
print(arr)
reverse(arr)
print(arr)
reverse(arr)
print(arr)

# ------------------- PROBLEM 4 - ROTATE ------------------------------------


def rotate(arr, steps):
    """
    Represents a function that receives two parameters - a StaticArray and an integer value (steps). The function
    will create and return a new StaticArray, which contains all of the elements from the original array, but their
    position has shifted right or left steps number of times
    """
    length = arr.length()
    effective_steps = steps % length
    rotated_array = arr[-effective_steps:] + arr[:-effective_steps]
    return rotated_array

source = [_ for _ in range(-20, 20, 7)]
arr = StaticArray(len(source))
for i, value in enumerate(source):
    arr.set(i, value)
print(arr)
for steps in [1, 2, 0, -1, -2, 28, -100, 2**28, -2**31]:
    space = ""if steps >= 0 else ""
    print(f'{rotate(arr, steps)} {space}{steps}')
print(arr)

# ------------------- PROBLEM 5 - SA_RANGE ----------------------------------

def sa_range(start, end):
    """
    TODO: Write this implementation
    """
    #if start > end:
        #return arr([])

    #consecutive_integers = [i for i in range(start, end + 1)]

    #return arr(consecutive_integers)

    pass

# ------------------- PROBLEM 6 - IS_SORTED ---------------------------------

def is_sorted(arr):
    """
    TODO: Write this implementation
    """
    #if arr.length() <= 1:
        #return 1

    #ascending = descending = True
    #for i in range(1, arr.length()):
        #if arr[i - 1] < arr[i]:
            #descending = False
        #elif arr[i - 1] > arr[i]:
            #ascending = False

    #if ascending:
        #return 1
    #if descending:
        #return -1
    #else:
        #return 0

    pass



# ------------------- PROBLEM 7 - FIND_MODE -----------------------------------

def find_mode(arr: StaticArray) -> tuple[object, int]:
    """
    TODO: Write this implementation
    """
    pass

# ------------------- PROBLEM 8 - REMOVE_DUPLICATES -------------------------

def remove_duplicates(arr: StaticArray) -> StaticArray:
    """
    TODO: Write this implementation
    """
    pass

# ------------------- PROBLEM 9 - COUNT_SORT --------------------------------

def count_sort(arr: StaticArray) -> StaticArray:
    """
    TODO: Write this implementation
    """
    pass

# ------------------- PROBLEM 10 - SORTED SQUARES ---------------------------

def sorted_squares(arr: StaticArray) -> StaticArray:
    """
    TODO: Write this implementation
    """
    pass

# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print('\n# min_max example 1')
    arr = StaticArray(5)
    for i, value in enumerate([7, 8, 6, -5, 4]):
        arr[i] = value
    print(arr)
    result = min_max(arr)
    if result:
        print(f"Min: {result[0]: 3}, Max: {result[1]}")
    else:
        print("min_max() not yet implemented")

    print('\n# min_max example 2')
    arr = StaticArray(1)
    arr[0] = 100
    print(arr)
    result = min_max(arr)
    if result:
        print(f"Min: {result[0]}, Max: {result[1]}")
    else:
        print("min_max() not yet implemented")

    print('\n# min_max example 3')
    test_cases = (
        [3, 3, 3],
        [-10, -30, -5, 0, -10],
        [25, 50, 0, 10],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        result = min_max(arr)
        if result:
            print(f"Min: {result[0]: 3}, Max: {result[1]}")
        else:
            print("min_max() not yet implemented")

    print('\n# fizz_buzz example 1')
    source = [_ for _ in range(-5, 20, 4)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(fizz_buzz(arr))
    print(arr)

    print('\n# reverse example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    reverse(arr)
    print(arr)
    reverse(arr)
    print(arr)

    print('\n# rotate example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    for steps in [1, 2, 0, -1, -2, 28, -100, 2 ** 28, -2 ** 31]:
        space = " " if steps >= 0 else ""
        print(f"{rotate(arr, steps)} {space}{steps}")
    print(arr)

    print('\n# rotate example 2')
    array_size = 1_000_000
    source = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(f'Started rotating large array of {array_size} elements')
    rotate(arr, 3 ** 14)
    rotate(arr, -3 ** 15)
    print(f'Finished rotating large array of {array_size} elements')

    print('\n# sa_range example 1')
    cases = [
        (1, 3), (-1, 2), (0, 0), (0, -3),
        (-95, -89), (-89, -95)]
    for start, end in cases:
        print(f"Start: {start: 4}, End: {end: 4}, {sa_range(start, end)}")

    print('\n# is_sorted example 1')
    test_cases = (
        [-100, -8, 0, 2, 3, 10, 20, 100],
        ['A', 'B', 'Z', 'a', 'z'],
        ['Z', 'T', 'K', 'A', '5'],
        [1, 3, -10, 20, -30, 0],
        [-10, 0, 0, 10, 20, 30],
        [100, 90, 0, -90, -200],
        ['apple']
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        result = is_sorted(arr)
        space = "  " if result and result >= 0 else " "
        print(f"Result:{space}{result}, {arr}")

    print('\n# find_mode example 1')
    test_cases = (
        [1, 20, 30, 40, 500, 500, 500],
        [2, 2, 2, 2, 1, 1, 1, 1],
        ["zebra", "sloth", "otter", "otter", "moose", "koala"],
        ["Albania", "Belgium", "Chile", "Denmark", "Egypt", "Fiji"]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value

        result = find_mode(arr)
        if result:
            print(f"{arr}\nMode: {result[0]}, Frequency: {result[1]}\n")
        else:
            print("find_mode() not yet implemented\n")

    print('# remove_duplicates example 1')
    test_cases = (
        [1], [1, 2], [1, 1, 2], [1, 20, 30, 40, 500, 500, 500],
        [5, 5, 5, 4, 4, 3, 2, 1, 1], [1, 1, 1, 1, 2, 2, 2, 2]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        print(remove_duplicates(arr))
    print(arr)

    print('\n# count_sort example 1')
    test_cases = (
        [1, 2, 4, 3, 5], [5, 4, 3, 2, 1], [0, -5, -3, -4, -2, -1, 0],
        [-3, -2, -1, 0, 1, 2, 3], [1, 2, 3, 4, 3, 2, 1, 5, 5, 2, 3, 1],
        [10100, 10721, 10320, 10998], [-100320, -100450, -100999, -100001],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(f"Before: {arr}")
        result = count_sort(arr)
        print(f"After : {result}")

    print('\n# count_sort example 2')
    array_size = 5_000_000
    min_val = random.randint(-1_000_000_000, 1_000_000_000 - 998)
    max_val = min_val + 998
    case = [random.randint(min_val, max_val) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(case):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = count_sort(arr)
    print(f'Finished sorting large array of {array_size} elements')

    print('\n# sorted_squares example 1')
    test_cases = (
        [1, 2, 3, 4, 5],
        [-5, -4, -3, -2, -1, 0],
        [-3, -2, -2, 0, 1, 2, 3],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(sorted(case)):
            arr[i] = value
        print(arr)
        result = sorted_squares(arr)
        print(result)

    print('\n# sorted_squares example 2')
    array_size = 5_000_000
    case = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(sorted(case)):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = sorted_squares(arr)
    print(f'Finished sorting large array of {array_size} elements')
