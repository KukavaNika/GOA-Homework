#1)შექმენით while loop რომელიც გამოიტანს "hello world!" სანამ არ გაუტოლდება 20'ს

#2)მომხმარებელს შემოატანინეთ სია და for loop ის საშუალებით გამოიტანეთ ყველა ელემენტი

#3)დაწერეთ მსგავსებები და განსხვავებები set, dictionary, tuple ზე 

#4)რას ნიშნავს immutable, mutable

#5)რას ეწოდება კონკატენაცია.

#6)რას ნიშნავს დეკლარირება.

#7)and და or ოპერატორებზე გააკეთეთ 5-5 მაგალითი 

#8)დამატებით გააკეთეთ 5 ცალი 8 kyu და 3 ცალი 7 kyu'ს codewars



#1)
count = 0
while count < 20:
    print("hello world!")
    count += 1

#2)
user_input = input("Enter a list of items: ")
items = user_input.split(",")

print("Your list:")
for item in items:
    print(item.strip())

#3)
#set - 
#tuple - 
#divtionary - 



#4)
a = "Hello"
b = "World"
print(a + " " + b) 

#5)
x = 10      
name = "John"  

#6)
# and
print(True and True)      
print(True and False)     
print(5 > 3 and 3 > 1)     
print(10 == 10 and 5 < 2)  
print("a" in "abc" and "z" in "xyz")
 
# or 
print(True or False)       
print(False or False)     
print(5 > 3 or 3 < 1)      
print(10 == 5 or 2 == 2)  
print("x" in "xyz" or "z" in "abc")  


#7)
#codewars - 8kyu

#1 
def is_even(n):
    return n % 2 == 0

#2
def make_negative(number):
    return -abs(number)

#3
def remove_char(s):
    return s[1:-1]

#4
def square_sum(numbers):
    return sum(x**2 for x in numbers)

#5
def number_to_string(num):
    return str(num)

 
#8) 
#codewars - 7kyu

#1
def maskify(cc):
    return '#'*(len(cc)-4) + cc[-4:] if len(cc) > 4 else cc

#2
def row_sum_odd_numbers(n):
    return n ** 3

#3
def find_short(s):
    return min(len(word) for word in s.split())






