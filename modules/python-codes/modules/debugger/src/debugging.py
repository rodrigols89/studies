# debugging.py

hello: str = "Hello, World!"

msg: str = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
"""

x: int = 10
y: int = 20

def the_sum(x: int, y: int) -> int:
    z: int = x + y
    w: int = x + y + z
    n: int = x + y + z + w
    return n

op = the_sum(x, y)

name: str = "John"

age: int = 30

dic: dict = {"name": name, "age": age}

list1 = [1, 2, 3, 4, 5]

list2 = [6, 7, 8, 9, 10]

list3 = list1 + list2

print(list3)
