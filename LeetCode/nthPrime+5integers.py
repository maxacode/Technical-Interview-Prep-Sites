def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def nth_prime(n):
    prime_count = 0
    i = 2
    while True:
        if is_prime(i):
            prime_count += 1
            if prime_count == n:
                return i
        i += 1

n = int(input("Enter the value of N: "))
nth_prime_number = nth_prime(n)
print(f"The {n}th prime number is {nth_prime_number}")
print("The next 5 integers are:")
for i in range(1, 6):
    print(nth_prime_number + i)



#grepper python lambda function
#Description: A lambda function is a small, anonymous function defined using the lambda keyword. It can take any number of arguments but can only have one expression.
#Example: square = lambda x: x * x
#end grepper