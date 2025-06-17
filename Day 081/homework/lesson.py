#1) https://www.codewars.com/kata/529b418d533b76924600085d/train/python

#2) https://www.codewars.com/kata/526571aae218b8ee490006f4/train/python

#3) https://www.codewars.com/kata/57f8ff867a28db569e000c4a/train/python

#4) https://www.codewars.com/kata/58539230879867a8cd00011c/train/python

#5) დამატებით გააკეთეთ 5 ცალი 7 kyu 


#1)
#ვერ გავაკეთე



#2)
def count_bits(n):
    return bin(n).count('1')



#3)
def solution(string, ending):
    return string.endswith(ending)


#4)
def f(x):
    from math import atan
    return x / (1 + x**2)

#5)
#1
def reverse_words(text):
    return ' '.join(word[::-1] for word in text.split(' '))


#2
def printer_error(s):
    return f"{sum(1 for c in s if c > 'm')}/{len(s)}"

#3
def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))


#4
def find_short(s):
    return min(len(word) for word in s.split())


#5
def is_isogram(string):
    s = string.lower()
    return len(set(s)) == len(s)
