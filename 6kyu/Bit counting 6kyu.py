def count_bits(n):
    count = 0
    while (n>0):
        if n%2:
            count +=1
        n //=2

    return count


print(count_bits(9))


#def countBits(n):
#   return bin(n).count("1")