

def merge_sort(new_numbers):
    if len(new_numbers) <= 1:
        return new_numbers
    else:
        midpoint = int(len(new_numbers) / 2)
        sublist_left = merge_sort(new_numbers[:midpoint])
        sublist_right = merge_sort(new_numbers[midpoint:])
        return merge_lists(sublist_left, sublist_right)


def merge_lists(sublist_left, sublist_right):
    result = []
    x, y = 0, 0
    while x < len(sublist_left) and y < len(sublist_right):
        if sublist_left[x] <= sublist_right[y]:
            result.append(sublist_left[x])
            x += 1
        else:
            result.append(sublist_right[y])
            y += 1
    result += sublist_left[x:]
    result += sublist_right[y:]
    return result
