
# https://www.youtube.com/watch?v=tFfugmZvqJw&list=PLn1uch862uBhLHQGCgivcOgbicVo8ngXc&index=1

# Not very efficent but since its small numbers its not that big of a deal

@profile
def calNFib(n: int)-> int:
    if n <= 1:
        return n
    else:
        return calNFib(n-1) + calNFib(n-2) # fib(3) b fib(2) = 1+1
    

print(calNFib(25))

#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181.


# Momoization Fibonnaci - dictionary of allready computed value
# very fast/efficeint

fibsDict = 0
@profile
def calNFib(n: int) -> int:
    if n == 0:
        return 0
    else:
        prevFib = 0
        curFib = 1
        for _ in range(n-1):
            newFib = prevFib + curFib
            prevFib = curFib
            curFib = newFib
    return curFib

print(calNFib(25))
