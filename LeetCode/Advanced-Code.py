
# HEAPS

# # https://www.youtube.com/watch?v=wGSQ486Y4sc
# import heapq

# data = [10, 20, 43, 1, 2, 65, 17, 44, 2, 3, 1]

# print(data[:])

# print(data)

# heapq.heapify(data)

# print(data)

# print(heapq.heappop(data)) # Best to keep heap structure safe 
# #print(data.pop(6)) # Does not keep Heap in placey

# print(heapq.heappush(data,44))


# Collections Counter 
# https://www.youtube.com/watch?v=cgDRugJzBfM&t=373s

# from collections import Counter

# c = Counter(A=4, B=2, C=1, D=-1)
# print(c)

# d = ['a', 'b', 'b', 'c']

# e = Counter(A=8, B=2, C=3, D=2)
# print(e)

# c.subtract(d) # subtract list d from c
# c.update(d) # add d to c

# #c.clear() # wipe it all
# print(c)

# print(c+e) 
# print(c-e)

# print(c & e) # Intersection of counters - minimum same elements in obht

# print(c | e) # Max of counters - max of each element


# Collections NamedTuple
# https://www.youtube.com/watch?v=GKgpvriuQY8&t=37s

# NAMED TUPLS ASSIGN MENAING TO EACH POSITION IN A TUPLE AND ALLOW FOR MORE READABLE SELF-DOCUMETNING CODE. THEY CAN BE USED WHEREVER REGULAT TUPLES ARE USED AND THEY ADD THE ABILITY TO ACCESS FIELDS BY NAME INSTEAD OF POSITION INDEx

# import collections
# from collections import namedtuple

# point = namedtuple('JOINT', 'x y z hh')
# point = namedtuple('KOOK', ['x','y','l'])

# print(point._fields) # ('x', 'y', 'l')
# newP = point(3,4,5) # Point(x=3, y=4, l=5)
# print(newP._replace(y=99)) # Templaryary replace since its a tuple

# print(newP)

# p2 = point._make(['a', 'b', 'c'])
# print(p2)



# Collections deque (says: deck)
# https://www.youtube.com/watch?v=m3JgSV1Obn8
# Is similar to list but faster at addign in front or end
# import collections
# from collections import deque

# d = deque("T$St")
# d.append('4')
# d.append(3)
# d.appendleft(5)
# print(d)

# d.pop() # remove last element
# d.popleft() # remove first element]]

# d.extend('abc')
# d.extend([1,2,9,'88'])
# d.extendleft('HEY') # add h to front then e then y so looks like y, e, h, .. 
# print(d)

# d.rotate(-1) # rotate to teh right or left if negative

# d = deque("T$St", maxlen=5)
# print(d.maxlen)
# print(d)

# d.extend('jaha')

# print(d)
# print(type(d))

# d.clear()


# optionoal parameters
# https://www.youtube.com/watch?v=0VdzZQdaZ28&list=PLzMcBGfZo4-nhWva-6OVh1yKWHBs4o_tv&index=1&t=85s


# class allCars(object):
# 	def __init__(self, name, make, year):
# 		self.name = name
# 		self.make = make
# 		self.year = year
# 	def display(self, showAll=False):
# 		if showAll:
# 			print(self.name, self.make, self.year)
# 		else:
# 			print("No showAll")


# car1 = allCars('Bula', 'Tesla', '2023')

# car1.display(True)
# car1.display(True)


# Static and Class Methods 
# https://www.youtube.com/watch?v=pUGyU-hxw5E&list=PLzMcBGfZo4-nhWva-6OVh1yKWHBs4o_tv&index=2

# class person(object):
# 	population = 50
# 	def __init__(self, name, age):
# 		self.age = age
# 		self.name = name

# 	@classmethod
# 	def getPopulation(clas):
# 		return clas.population

# 	@staticmethod
# 	def isAdult(age):
# 		return age >= 18

# 	def display(self):
# 		print(self.name, ' is ', self.age, 'years old')


# newPerson = person('tim', 13)

# print(person.getPopulation())

# print(person.isAdult(newPerson.age))
# print(person.isAdult(33)) 







