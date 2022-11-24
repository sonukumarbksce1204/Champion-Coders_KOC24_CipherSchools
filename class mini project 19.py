n=int(input("Enter the Number:"))
c=n
j=1
while c:
    f=0
    for i in range(1,j+1):
        if j%i==0:
            f+=1
    if f==2:
        s=str(j)
        p=s[::-1]
        if s==p:
            print(j)
            c-=1
    j+=1
