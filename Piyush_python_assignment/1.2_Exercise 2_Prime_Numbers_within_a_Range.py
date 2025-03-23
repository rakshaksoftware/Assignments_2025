def Primegenerator(a: int,b: int)-> list[int]:
    '''a Python function that takes two integers as input and returns a list of all prime numbers
between those two numbers (inclusive)'''
    nos=list()
    if a>b:
        a,b=b,a
    if a<2:
        a=2
    if b<2:
        return nos
    
    for i in range(a,b+1):
        isprime: bool=True
        j: int =2
        while j*j<=i:
            if(i%j==0):
                isprime=False
            j+=1
        if isprime:
            nos.append(i)
    return nos

a,b=map(int,input("Please enter the nos:").split())
ans=Primegenerator(a,b)
for number in ans:
    print(number)

