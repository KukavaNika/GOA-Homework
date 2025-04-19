#1) https://www.codewars.com/kata/53dbd5315a3c69eed20002dd/train/python

#2) https://www.codewars.com/kata/5390bac347d09b7da40006f6/train/python

#3) https://www.codewars.com/kata/558fc85d8fd1938afb000014/train/python

#4) https://www.codewars.com/kata/56606694ec01347ce800001b/train/python

#5) https://www.codewars.com/kata/5656b6906de340bd1b0000ac/train/python

#6) დამატებით შეასრულეთ თქვენთვის სასურველი 5 ცალი 7kyu 



#1)
def filter_list(l):
    return [character for character in l if type(character) != str]


#2)
def to_jaden_case(string):
    return ' '.join(word.capitalize() for word in string.split())

#3)
def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])


#4)
def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

#5)
def longest(s1, s2):
    return ''.join(sorted(set(s1 + s2)))


#6)
 
#1
def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))


#2
def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')


#3
def find_short(s):
    return min(len(word) for word in s.split())

#4
def reverse_words(text):
    return ' '.join(word[::-1] for word in text.split(' '))

#5
def is_square(n):
    return n >= 0 and int(n**0.5) ** 2 == n
