# counting_sheeps... codewars code
def count_sheeps(sheep):
    counter = 0
    for i in sheep:
        if i:  # Same as if i == TRUE
            counter += 1
    return counter


# example
array1 = [True, True, True, False,
          True, True, True, True,
          True, False, True, False,
          True, False, False, True,
          True, True, True, True,
          False, False, True, True]

print(count_sheeps(array1))

# best solution
print(array1.count(True))
print(array1.count(False))
