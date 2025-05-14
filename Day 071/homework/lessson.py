#1) https://www.codewars.com/kata/5266876b8f4bf2da9b000362/train/python

#2) https://www.codewars.com/kata/525f50e3b73515a6db000b83/train/python

#3) https://www.codewars.com/kata/54da5a58ea159efa38000836/train/python

#4) https://www.codewars.com/kata/5abd66a5ccfd1130b30000a9/train/python

#5) https://www.codewars.com/kata/556196a6091a7e7f58000018/train/python

#6) დამატებით გააკეთეთ 5 ცალი 7 kyu



#1)
#ვერ გავაკეთე


#2)
#ვერ გავაკეთე


#3)

def find_it(seq):
    for i in seq:
        if seq.count(i) % 2 != 0:
            return i


#4)
def is_valid_walk(walk):
    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')



#5)
def duplicate_count(text):
    return len([c for c in set(text.lower()) if text.lower().count(c) > 1])


#6)
#1
def accum(s):
    return '-'.join((c * (i + 1)).capitalize() for i, c in enumerate(s))

#2
def descending_order(num):
    return int(''.join(sorted(str(num), reverse=True)))

#3
def find_short(s):
    return min(len(word) for word in s.split())


#4
def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])


#5
def is_square(n):
    return n >= 0 and (n ** 0.5).is_integer()




