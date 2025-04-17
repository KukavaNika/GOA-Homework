#1)https://www.codewars.com/kata/53dbd5315a3c69eed20002dd/train/python

#2)https://www.codewars.com/kata/55908aad6620c066bc00002a/train/python

#3)https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9/train/python

#4)https://www.codewars.com/kata/55b42574ff091733d900002f/train/python

#5)https://www.codewars.com/kata/5656b6906de340bd1b0000ac/train/python

#6)დამატებით თქვენით შეასრულეთ 5 ცალი 8kyu dა 3 ცალი 7kyu


#1)
def filter_list(l):
    return [i for i in l if isinstance(i, int)]

#2)
def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')

#3)
def find_short(s):
    return min(len(word) for word in s.split())

#4)
def friend(x):
    return [name for name in x if len(name) == 4]

#5)
def duplicate_encode(word):
    word = word.lower()
    return ''.join(['(' if word.count(c) == 1 else ')' for c in word])


#დამატებითები 8kyu

#6)
 #1
def bool_to_word(b):
    return "Yes" if b else "No"

#2
def solution(string):
    return string[::-1]

#3
def positive_sum(arr):
    return sum(x for x in arr if x > 0)

#4
def even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"

#5
def count_positives_sum_negatives(arr):
    if not arr:
        return []
    return [sum(1 for x in arr if x > 0), sum(x for x in arr if x < 0)]

# 7kyu
#6
def accum(s):
    return '-'.join(c.upper() + c.lower()*i for i, c in enumerate(s))

#7
def is_square(n):
    return n >= 0 and int(n**0.5) ** 2 == n

#8
def descending_order(num):
    return int(''.join(sorted(str(num), reverse=True)))
