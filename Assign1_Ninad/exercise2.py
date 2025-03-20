# Exercise 2: Prime Numbers within a Range
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_numbers(start, end):
    return [num for num in range(start, end + 1) if is_prime(num)]

start=int(input("Enter start value: "))
end=int(input("Enter end value: "))
print(prime_numbers(start, end))