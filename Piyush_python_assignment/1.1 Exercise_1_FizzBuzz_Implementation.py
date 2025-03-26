for i in range (1,101):
    ans: str=""
    if(i%3==0): ans+="Fizz"
    if(i%5==0): ans+="Buzz"
    if ans:
        print(ans)
    else :
        print(i)