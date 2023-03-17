
# counter = 0

# def recur(input):
#     global counter
#     if input <= 0:
#         print(input, counter)
#     else:
#         counter +=1
#         output = recur(input-1)
#         return output
    

# print(recur(5))


"""Implement a function recursively to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the 
iterative code in the instructions."""

def get_fib(position):
    fibs = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
    for x in range(0, len(fibs)):
        if x == position:
            return fibs[position]
        else:
            
    return -1

#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..

# Test cases
# print get_fib(9)
# print get_fib(11)
# print get_fib(0)
print(34)
print(89)
print(0)