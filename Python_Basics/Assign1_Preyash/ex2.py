num1=int(input("Enter the first number:\n"))
num2=int(input("Enter the second number:\n"))

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

for i in range(num1,num2+1):
    if is_prime(i):
        print(i)