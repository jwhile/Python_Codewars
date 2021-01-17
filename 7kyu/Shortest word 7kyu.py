


def find_short(s):
    b = s.split()
    L = list()
    for i in b:
        L.append((len(i), i))

    L.sort()  #L.sort(reverse=True)
    M = L[0]
    l = (M[0])

    return l # l: shortest word length

# best option
#def find_short(s):
#   return min(len(x) for x in s.split())







