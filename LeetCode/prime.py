
def getPrimes(n):
    primes = ''
    oldN = 0
    #n = n*n+1
    return recurPrimes(primes, n, oldN)

  #  n = n*2+20

def recurPrimes(primes, n, oldN):
    for i in range (oldN+2, n+6):
        for j in range(oldN+2, i+6):
            if i%j == 0:
                break
        else:
            primes = primes+ str(i)
            if len(primes) <= a+5:
                oldN = n
                print("all Primes then lenght")
                print(primes)
                print(len(primes))
                n += 5
                recurPrimes(primes, n, oldN)

             
    print(primes)
    return primes[a:a+5]

a = 3
sol = (getPrimes(a))
print("Should be 23571")
print(sol)

a = 3
#sol = (getPrimes(a))
#print("Shuld be 71114")
print(sol)
#a = 100
#print(getPrimes(a))
a = 200
#print(getPrimes(a))
a = 10000
#print(getPrimes(a))

#print(getPrimes(a*a))
#allPrimes = (getPrimes(a*a)[a:a+5])    
#print(allPrimes)