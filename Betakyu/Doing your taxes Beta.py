def tax(x):
    if isinstance(x, str):
        return "Error 404"
    else:
        return round(x * 1.05, 2)


print(tax(42.6))
