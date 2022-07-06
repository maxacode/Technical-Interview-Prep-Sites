#fucntion with input of array of integers.. If 3 elements exist that equal to 0 if they do return all them


import random,time 

#random integers.
randInt = []

#Generating random 1000 number in the range below. 
while True:
    for x in range(0,40):
        randInt.append(random.randrange(-1000,1000, 1))
    break

#All the random numbers generated 
print(f"\n \n All the random numbers generated: \n \n {randInt}\n \n")

randInt = list(set(randInt))

#How man unuqire number 
print(f"How many Unique random Numbers: {len(randInt)}")


#Timer to pause to see above printsd
time.sleep(5)

print()

#Start of function
def sumOf3Integers():
    counter = 0

    #First loop to run for all integers
    for integerInrandInt in range(0,len(randInt)):
        firstInt = randInt[integerInrandInt]

        #Second loop to run 
        for integerInrandInt in range(1,len(randInt)):
            secondInt = randInt[integerInrandInt]

            #Checking if number is the same as the first, if so 'continue' which goes to the next iteration
            if firstInt == secondInt:
                continue
                
            #Third loop
            for integerInrandInt in range(2,len(randInt)):
                thirdInt = randInt[integerInrandInt]
                if thirdInt == secondInt or thirdInt == firstInt:
                    continue

                #Adding all 3 numbers to see if they equal to 0 and printing them
                if firstInt+secondInt+thirdInt == 0:
                    print(f"{firstInt}  |  {secondInt}  |  {thirdInt}\n")
                    counter += 1

    print(f"How Many answers: {counter}")
   
sumOf3Integers()