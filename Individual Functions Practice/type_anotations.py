# Some basic type annotations
#
# Note that type annotations are not enforced by the interpreter.
# The code
# 	a: int = 5
# 	a = "hello"
# is valid Python.

# The typing module is built-in and contains some extra types that
# can be used for annotations
from typing import Union, Optional, List, Tuple

a: int = 6 # A variable annotated as int

# This denotes a variable that will hold ints and floats over 
# the course of its usage.
two_types: Union[int, float] = 5.6
  
# This variable could hold str or it could be None. This is
# effectively the same as typing opt as Union[str, None].
opt: Optional[str] = None
  
# This is a function with type annotations; it takes two
# int parameters and returns bool.
def annotated_func(x: int, y: int) -> bool:
  return x > y

# You can also annotate a certain data structure and the type of
# data you intend it to contain.
l: List[int] = [1, 2, 3, 4]

t: Tuple[chr] = (1, "b", "c")
print(t)
t: Tuple[str] = (1, 'b', 'c', 'd')
print(l)
print(t)
# In Python 3.9+, list[<TYPE>] and tuple[<TYPE>] can be used
# instead. They're aliases for typing.List and typing.Tuple.


#chr() takes as input an int , and returns a single character str . The returned str is just like any other str in Python, and similarly is not a specific encoding using bytes .Apr 24, 2018