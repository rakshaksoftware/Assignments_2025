def isaprimeno(n):
    if n<2:
        return False
    elif n==2:
        return True
    else:
        for i in range(2,n):
            if n%i==0:
                return False
    return True

def printprimenos(a,b):
    for i in range(a,b):
        if isaprimeno(i):
            print(i)

x=input("Smaller number")
y=input("Larger number")
printprimenos(x,y+1)        

            
            

            
    

