

def duplicate_count(text):
    text = text.lower()
    S = set (list(text))
    counter = 0
    for a in S:
        if text.count(a) > 1:
          counter += 1

    return counter

print(duplicate_count("abcdeaB"))

"""
#ESTA FUNCION 
    L=[]
    for i in text:
        L.append(text.count(i))
    return max(L)


print(duplicate_count("f"))


text ="holaa"
A=(2,4,1,2)
L=[]
for i in text:
    print(i)
    L.append(text.count(i) )
    print(L)
print(max(L))
"""