def is_triangle(a, b, c):
    triangle = (a,b,c)
    triangle = sorted(triangle)
    print (triangle)
    if (triangle[0] < triangle[1]+triangle[2]) and triangle[0] > triangle[2] - triangle [1]:
        return True
    else:
        return False


print(is_triangle (1,2,2))