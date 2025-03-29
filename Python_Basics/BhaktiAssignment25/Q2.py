a=int(input())
b=int(input())

for i in range(a,b+1):
    flag=0
    for p in range(2,i):
        if(i%p==0):
            flag=1
            break
    if flag==0:
        print(i)
        
