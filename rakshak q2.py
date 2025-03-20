def is_prime(p):
    i=2
    done=True
    while(i<p):
        if(p%i==0):
            return False
        i=i+1
    

    return True

def primenumbers():
    a=input("a: ")
    b=input("b: ")
    x=int(a)+1
    list1=[]
    while(x<int(b)):
        if(is_prime(x)):
            list1.append(x)
    print(list1)      
    return list1
primenumbers()