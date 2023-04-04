import numpy as np
def dym(i,j):
    a = np.ones((i,j))
    h=0
    for h in range(i):
        if i>0 and j==0:
            a[i,j]=0
            i=i+1
        elif i==0 and j>0:
            a[i,j]=1
            i=i+1
        else:
            a[i,j]=(dym(i-1,j)+dym(i,j-1))/2
    print(a)
#j=int(input("Podaj j: "))
#i=int(input("Podaj i: "))
i=5
j=5
print(dym(i,j))
