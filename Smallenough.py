def small_enough(array, limit):
    for l in array:
        if l > limit:
            return False
    return True

print(small_enough([66, 101], 200))
print(small_enough([78, 117, 110, 99, 104, 117, 107, 115], 100))
print(small_enough([101, 45, 75, 105, 99, 107], 107))
print(small_enough([80, 117, 115, 104, 45, 85, 112, 115], 120))
