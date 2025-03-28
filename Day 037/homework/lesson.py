#1)
class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        return f"Hello, my name is {self.name}."


#2)
def tidy_up_phone_number(numbers):
    return [f'+1{n.lstrip("1+")}' for n in numbers]



#3)
def contamination(text, char):
    return char * len(text) if char else ""
contamination("abc", "z") 
contamination("", "z")   
contamination("hello", "")
contamination("xyz", "1") 

#4)
def is_palindrome(s):
    return s.lower() == s.lower()[::-1]
is_palindrome("racecar")  
is_palindrome("Racecar")   
is_palindrome("hello")     
is_palindrome("madam")   
is_palindrome("MadAm")   

#5)
def number_to_string(num):
    return str(num)
number_to_string(123) 
number_to_string(999)  
number_to_string(-100)  

