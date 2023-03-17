"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        #4print(self.value)
        

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        

    def append(self, new_element):
        print("start Append")
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def length(self):
        print("Start Lenght")
        cur = self.head
        total = 0
        while cur.next != None:
            total +=1
            cur = cur.next
        return total

    def get_position(self, position):
        print("Get Postion")
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
      #  print(self.length())
        if position >= self.length():
            print("Index out of range")
            return None
        count = 0
        cur = self.head
        while True:
            cur = cur.next
            if count == position: return cur.value
            count +=1

        return None
    
    def insert(self, new_element, position):
        print("start insert")
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        new = Element(new_element)
        itr = self.head
        count = 1
        while itr:
            if itr == position:
                itr.next = new
                new.next = itr.next
                break
            itr = itr.next
            count +=1 
        pass
    
    
    def delete(self, value):
        """Delete the first node with a given value."""
        print("Starting Delte")
        if value >= self.length():
            print("Error index out of RANGE")
            return "EROR"
        curIndex = 0
        cur = self.head
        while True:
            last = cur
            cur = cur.next
            if curIndex == value:
                last = cur.next
                return self.display()
            curIndex +=1
        return "Del Error"
        
    def addEnd(self,value):
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = Element(value)

    def addStart(self, value):
        cur = self.head
        newStart = Element(value)
        self.head = newStart
        newStart.next = cur

    def display(self):
        print('Starting Display')
        if self.head is None:
            print("List Empty")
        else:
            elems = []
            n = self.head
            while n is not None:
                elems.append(n.value)
                n = n.next
        print(elems)
        # cur = self.head
        # elems = []
        # while cur.next != None:
        #     cur = cur.next
        #     elems.append(cur.value)
        # print(elems)

# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)


# Start setting up a LinkedList
ll = LinkedList(e1)

ll.display()

ll.append(e2)
ll.append(e3)
#ll.append(e4)

ll.display()
ll.addEnd(9)
ll.display()
ll.addStart(6)
ll.display()
ll.insert(833,3)
ll.display()
#ll.length()

#ll.display()
# Test get_position
# # Should print 3
# print(ll.head.next.next.value)
#  # Should also print 3
# print(ll.get_position(3))

# # # Test insert
# ll.insert(e4,3)
# # Should print 4 now
# print(ll.get_position(3))

# # Test delete
#print(ll.delete(1))
# # Should print 2 now
# print(ll.get_position(1).value)
# # Should print 4 now
# print(ll.get_position(2).value)
# # Should print 3 now
# print(ll.get_position(3).value)
