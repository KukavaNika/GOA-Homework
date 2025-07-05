

#1) შეასრულეთ 5 ცალი 8 kyu  5 ცალი 7 kyu ყველა შესრულებული ამოცანა ჩაინიშნეთ და განვიხილოთ გაკვეთილზე

# 8kyu

#1
def number_to_string(num):
    return str(num)

#2
def solution(string):
    return string[::-1]

#3
def multiply(a, b):
    return a * b

#4
def even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"

#5
def make_negative(number):
    return -abs(number)


# 7kyu

#1
def descending_order(num):
    return int(''.join(sorted(str(num), reverse=True)))

#2
def find_short(s):
    return min(len(word) for word in s.split())

#3
def is_square(n):
    return n >= 0 and int(n ** 0.5) ** 2 == n

#4
def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])
