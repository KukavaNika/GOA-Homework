#1)
def double_integer(i):
    return i * 2

#2)
def friend(x):
    return [name for name in x if len(name) == 4]

#3)
from functools import reduce

def grow(arr):
    return reduce(lambda x, y: x * y, arr)

#4)
def find_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

#5)
def combine_names(first, last):
    return f"{first} {last}"

#6)
def build_string(*args):
    return "I like " + ", ".join(args) + "!"

#7)
def remove_char(s):
    return s[1:-1]

#8)
def sum_cubes(n):
    return sum(i ** 3 for i in range(1, n + 1))

#9)
def modify_list():
    my_list = [10, 20, 30, 40, 50]
    del my_list[2]  
    my_list.insert(0, 99)  

print(modify_list())  

#10)
def power(base, exponent):
    return base ** exponent

print(power(2, 3))  
print(power(5, 2))  

#11)
def check_list_length(lst):
    return "List length is even" if len(lst) % 2 == 0 else "List length is odd"

print(check_list_length([1, 2, 3, 4]))
print(check_list_length([1, 2, 3]))

