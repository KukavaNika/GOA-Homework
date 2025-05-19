#1) https://www.codewars.com/kata/52efefcbcdf57161d4000091/train/python

#2) https://www.codewars.com/kata/53697be005f803751e0015aa/train/python

#3) https://www.codewars.com/kata/5574835e3e404a0bed00001b/train/python

#4) https://www.codewars.com/kata/51f41fe7e8f176e70d0002b9/train/python

#5) დამატებით გააკეთეთ 5 ცალი 7 kyu




#1)
def count(string):
    result = {}
    for char in string:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result

#2)
#ვერ გავაკეთე


#3)
def incrementer(nums):
    return [(num + i + 1) % 10 for i, num in enumerate(nums)]

#4)
#ვერ გავაკეთე



#5) 7kyu


#1
def is_isogram(string):
    s = string.lower()
    return len(s) == len(set(s))


#2 # გაკეთებული მქონდა
def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])

#3
def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')

