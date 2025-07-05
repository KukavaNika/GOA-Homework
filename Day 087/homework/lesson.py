
# შეასრულეთ 5 ცალი 8 kyu, 5 ცალი 7 kyu და 2 ცალი 6 kyu ყველა შესრულებული ამოცანა ჩაინიშნეთ და განვიხილოთ გაკვეთილზე



# 8kyu

#1
def repeat_str(repeat, string):
    return string * repeat


#2
def remove_char(s):
    return s[1:-1]


#3
def positive_sum(arr):
    return sum(x for x in arr if x > 0)

#4
def bool_to_word(boolean):
    return "Yes" if boolean else "No"

#5
def opposite(number):
    return -number


# 7kyu

#1
def getCount(string):
    return sum(1 for char in string if char in 'aeiou')

#2
def is_isogram(string):
    return len(set(string.lower())) == len(string)

#3
def square_digits(num):
    return int(''.join(str(int(d)**2) for d in str(num)))

#4
def high_and_low(numbers):
    nums = list(map(int, numbers.split()))
    return f"{max(nums)} {min(nums)}"

#5
def is_square(n):
    return n >= 0 and int(n**0.5) ** 2 == n



# 6kyu

#1
def duplicate_encode(word):
    word = word.lower()
    return ''.join('(' if word.count(c) == 1 else ')' for c in word)

#2
#ვერ გავაკეთე