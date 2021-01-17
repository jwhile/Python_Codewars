def sum_digits(number):
    solution = 0
    convert_str = str(abs(number))
    convert_list = list(convert_str)
    for i in convert_list:
        solution += int(i)
    return solution

print(sum_digits(153))