def bouncing_ball(h, bounce, window):
    if h <= 0:
        return -1
    elif bounce <= 0 or bounce >= 1 :
        return -1
    elif window <= 0 or window >= h:
        return -1


    exp = 1 #always seen at least 1 time, falling down first time
    newbounce = h * bounce
    while newbounce > window:
        exp +=2 #if enter the condition, it will see 2 times more, one up one down.
        newbounce = newbounce*bounce
    return exp

print(bouncing_ball(3, 0.5, -3))
print(bouncing_ball(3, 0.66, 1.5))
print(bouncing_ball(30, 0.66, 1.5))
print(bouncing_ball(30, 0.75, 1.5))
