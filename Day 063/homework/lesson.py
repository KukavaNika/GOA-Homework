#1) https://www.codewars.com/kata/54ba84be607a92aa900000f1/train/python

#2) https://www.codewars.com/kata/5390bac347d09b7da40006f6/train/python

#3) https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/train/python

#4) https://www.codewars.com/kata/55f8a9c06c018a0d6e000132/train/python

#5) https://www.codewars.com/kata/55fd2d567d94ac3bc9000064/train/python

#6) დამატებით გააკეთეთ 5 ცალი 7kyu codewars.

#1)
def is_isogram(string):
    string = string.lower()
    return len(string) == len(set(string))

#2)
def to_jaden_case(string):
    return ' '.join(word.capitalize() for word in string.split())

#3)
def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))

#4)
def validate_pin(pin):
    return pin.isdigit() and len(pin) in (4, 6)

#5)
def row_sum(n):
    return n * (n + 1) // 2

#6) 7kyu

#1
def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])


#2
def reverse_words(text):
    return ' '.join(word[::-1] for word in text.split(' '))

#3
def get_count(sentence):
    return sum(1 for c in sentence if c in 'aeiou')

#4
import math
def find_next_square(sq):
    root = math.isqrt(sq)
    return (root + 1) ** 2 if root * root == sq else -1

#5
def printer_error(s):
    errors = sum(1 for c in s if c > 'm')
    return f"{errors}/{len(s)}"
