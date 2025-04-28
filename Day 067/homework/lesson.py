#1) https://www.codewars.com/kata/5390bac347d09b7da40006f6/train/python

#2) https://www.codewars.com/kata/55f2b110f61eb01779000053/train/python

#3) https://www.codewars.com/kata/5663f5305102699bad000056/train/python

#4) https://www.codewars.com/kata/58712dfa5c538b6fc7000569/train/python

#5) https://www.codewars.com/kata/58a66c208b88b2de660000c3/train/python

#6) დამატებით გააკეთეთ 10 ცალი 8kyu






#1)
def to_jaden_case(string):
    return ' '.join(word.capitalize() for word in string.split())


#2)
def add(a, b):
    return a + b

#3)
def final_countdown(lst):
    result = []
    for num in lst:
        if num % 2 == 0:
            result.append(num)
    return result

#4)
#ვერ გავაკეთე



#5)
def query_string(S, N):
    for num in range(1, N + 1):
        if bin(num)[2:] not in S:
            return False
    return True


#6)

#1
def digitize(n):
    return list(map(int, str(n)[::-1]))


#2
def even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"


#3
def repeat_str(repeat, string):
    return string * repeat


#4
def remove_char(s):
    return s[1:-1]


#5

def opposite(number):
    return -number

#6
def sum_array(a):
    return sum(a)

#7
def minimum(arr):
    return min(arr)

def maximum(arr):
    return max(arr)

#8
def make_negative(number):
    return -abs(number)


#9
def bool_to_word(b):
    return "Yes" if b else "No"

#10
def double_integer(i):
    return i * 2
