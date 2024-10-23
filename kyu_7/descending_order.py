def descending_order(num):
    sorted_numbers = ''.join(sorted(str(num), reverse = True))
    sorted_int = int(sorted_numbers)
    return sorted_int

print(descending_order(8735468892))