def solution(number):
    contador = 0
    for i in range(1, number) :
         if i %5==0 :
             contador += i
         elif i %3==0 :
             contador += i

    return contador


print(f"solucion",solution(10))