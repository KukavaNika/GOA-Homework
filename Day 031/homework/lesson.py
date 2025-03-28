#code wars
#1)
def greet():
    return "Hello World!"
print(greet())

#2)
def opposite(number):
    return -number

#3)
def make_negative(number):
    return -abs(number)

#4)
def positive_sum(arr):
    return sum(x for x in arr if x > 0)

#5)
def repeat_str(n, s):
    result = ""
    for _ in range(n):
        result += s
    return result

#6)
def find_smallest_int(arr):
    smallest = arr[0]
    for num in arr:
        if num < smallest:
            smallest = num
    return smallest


#7)
find_smallest_int([34, 15, 88, 2])
find_smallest_int([34, -345, -1, 100])
find_smallest_int([5, 10, 3])

def find_smallest_int(arr):
    smallest = arr[0]
    for num in arr:
        if num < smallest:
            smallest = num
    return smallest

#8)
#replace
def no_space(x):
    return x.replace(" ", "")


#using join function
def no_space(x):
    return "".join(char for char in x if char != " ")

