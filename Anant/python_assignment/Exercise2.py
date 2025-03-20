s =int(input("Enter smaller number "))
l=int(input("Enter smaller number "))
i=s
for i in range(s,l+1):
    for j in range(2,i):
        if(i%j==0):
            break
        print(i)
        break
