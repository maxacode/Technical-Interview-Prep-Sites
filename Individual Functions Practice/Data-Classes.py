from audioop import add
from dataclasses import dataclass, field
import random
import string


def generate_id() -> str:
    return "".join(random.choices(string.ascii_uppercase, k=8))

def gen_full_name(name = None, address = None) -> str:
    return f"{name} {address}"
    
#@dataclass(Frozen=True) # once you use this, you can't change the values of the fields anymore (Frozen=True) 
# @dataclass(kw_only=True) # Force someone to supply all the arguments with the keywords ex: name = 'john' not just 'john'
@dataclass(slots = True) # Use this if you want to use the __slots__ attribute - this will make the class smaller and faster (slots = True) 
class Person:
    name: str
    address: str
    # full_name: str = field(default_factory=gen_full_name)
    full_name: str = field(default_factory=str)
    active: bool = field(init=False, default_factory=bool)
    email: list[str] = field(default_factory=list)
    id: str = field(init=False, default_factory=generate_id)
    _search_string: str = field(init=False, repr=False)

    def __post_init__(self) -> None:
        self._search_string = f"{self.name} {self.address}"
        self.full_name = f"{self.name} {self.address}"

    # def __init__(self, name, address):
    #     self.name = name
    #     self.address = address
    #     self.full_name = f"{self.name} {self.address}"




p1 = Person(name= "John",address= "123 Main St.")
print(p1)

print()

# dataclasses stores the data in a Dict like object so we can access it like a dictionary and we can also access the data like a dictionary using the keys and values methods like bellow:
#@ print(p1.__dict__["active"])

print(p1.__dir__())