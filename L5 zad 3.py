def S(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        cia=[1,2,4,8,16,32]
        2*S(n-1)-S(n-2)
        return 2*S(n-1)-S(n-2)



n=int(input("Podaj liczbę: "))
print(S(n))
