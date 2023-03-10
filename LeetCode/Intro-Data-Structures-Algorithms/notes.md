# Intor to Data Strucutes and Algo's

[Link: Udacity Site](https://learn.udacity.com/courses/ud513/lessons/a7bd2ec6-dec4-4f3a-8282-9d452d0cb693/concepts/b646f4e9-dc62-48dd-a058-2cdd1f35df4f)

## Lesson 1

### Big O

#### Time Efficency 

- Notation 0(n) - n being some algebraic notation.
- example:

``` func decode(input):
        create outputstring
        for each letter in input
            get new_letter from letter local in cipher
            add new_leeter to put
        retunr output
```

- O(2n + 2) or O(3n + 2) or O(29n + 2)
- So we Drop teh constants and just keep O(n)
- 10 lines of code > O(2 * 10 + 2) == 22 * Time of each line
 - Hard to know exactly how much code will run 
 - - with C you might have more code but less Work since its low level
- - with Python - Less code but more Work since its High level
- - [Link: Effiencies Wikipeaia](https://en.wikipedia.org/wiki/Time_complexity#Table_of_common_time_complexities)
- Efficensy is talked usually in Worse case (Going through all 26 Letters) but can also use Best/Average case. 

#### Space Efficency 

[Link to Cod 1-11 Efficency Practice](1-11-Efficency-Practice.py)

[Link: BIg O Cheat Cheat](https://www.bigocheatsheet.com/)

---

## Lesson 2

### Collections

- Data structures are extensions of collections

#### Arrays

- List's with a few added rules
- some langauges only allow single data types other langauges allow multi data type sin a single array
- each array has an index starting with 0 

[Link: time complexity](https://wiki.python.org/moin/TimeComplexity)

- Python has an interesting data stucture called a "list" that is much more than a mere list. In fact, a Python list actually encompasses the functionality of almost every list-based data structure in this lesson.

- Behind the scenes a Python list is built as an array. Even though you can do many operations on a Python list with just one line of code, there's a lot of code built in to the Python language running to make that operation possible.

- For example, inserting into a list is easy (happens in constant time). However, inserting into an array is O(n), since you may need to shift elements to make space for the one you're inserting, or even copy everything to a new array if you run out of space. Thus, inserting into a Python list is actually O(n), while operations that search for an element at a particular spot are O(1). You can see the runtime of other list operations here.

- Python is a "higher level" programming language, so you can accomplish a task with little code. However, there's a lot of code built into the infrastructure in this way that causes your code to actually run much more slowly than you'd think. Keep this in the back of your mind when using Python. You likely won't need to know the details of how Python works behind the scenes in a programming interview, but you'll seem very impressive if you do!

#### Linked List

- Extension of an array but not an array
- Adding/Remvoing is a lot easier vs Array
- Higher level lagauges might not have a distinction
![Linnked istes](./Assets/linked-lists.png)
- Adding new item is just changing the next pointer
- - But get the value of of x0123 before adding onet here
- Doubly Linked lists
- has prior and next links

