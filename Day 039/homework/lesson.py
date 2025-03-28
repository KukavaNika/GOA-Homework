

#1)
def summation(num):
    return sum(range(1, num + 1))
print(summation(5)) 
print(summation(10)) 

#2)
def number_to_string(n: int) -> str:
    return str(n)
print(number_to_string(123)) 
print(number_to_string(-456)) 

#3)
def repeat_string(n: int, s: str) -> str:
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    return s * n
print(repeat_string(3, "hello")) 
print(repeat_string(0, "test"))   


#4)
def summation(num: int) -> int:
    return sum(range(1, num + 1))
print(summation(5)) 
print(summation(10)) 

#5)
def greet(name: str) -> str:
    return f"Hello, {name} how are you doing today?"
print(greet("Alice")) 
print(greet("Bob"))  

