"""
CON SORT
def descending_order(num):
    nums = list(str(num))
    nums.sort()
    nums.reverse()
    return int("".join(nums))

print(descending_order(1201 ))

"""

def descending_order(num):
    nums = sorted(str(num), reverse = True)
    return int("".join(nums))

print(descending_order(1201 ))