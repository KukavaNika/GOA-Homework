#1) https://www.codewars.com/kata/525f50e3b73515a6db000b83/train/python

#2) https://www.codewars.com/kata/54da5a58ea159efa38000836/train/python

#3) https://www.codewars.com/kata/523f5d21c841566fde000009/train/python

#4) https://www.codewars.com/kata/57a1fd2ce298a731b20006a4/train/python

#5) https://www.codewars.com/kata/6707688c0f597511f6649270/train/python

#6) დამატებით გააკეთეთ 5 ცალი  7 kyu 


#1
def create_string(n):
    return ''.join(['1' if i % 2 == 0 else '0' for i in range(n)])

#2
def find_it(seq):
    for i in seq:
        if seq.count(i) % 2 != 0:
            return i

#3
def array_diff(a, b):
    return [i for i in a if i not in b]

#4
def round_to_next5(n):
    return n if n % 5 == 0 else n + (5 - n % 5)

#5
def remove(string):
    return string[1:-1].split(',') if len(string) > 2 else None

#(6

#1
def goose_filter(birds):
    geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
    return [b for b in birds if b not in geese]

#2
def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')

#3
def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])

#4
def find_short(s):
    return min(len(word) for word in s.split())

#5
#ვერ გავაკეთე