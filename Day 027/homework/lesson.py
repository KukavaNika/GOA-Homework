#1)შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა ორი რიცხვი შემდეგ კი გამოიტანეთ ამ რიცხვების ჯამი.

#2)შექმენით ფუნქცია რომელსაც გადაეცემა არგუმენტად რიცხვი შემდეგ კი მან უნდა დაგვიბრუნოს ლუწია ეს რიცხვი თუ კენტი.

#3)შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა რიცხვი შემდეგ კი მან უნდა დაგვიბრუნოს ეს რიცხვი დადებითია თუ უარყოფითი.

#4)შექმენით ფუნქცია, რომელსაც არგუმენტად გადაეცემა სახელი და დაბეჭდავს მისთვის მიესალმებას (მაგალითად: "Hello Giorgi"). გამოძახეთ ეს ფუნქცია 2-ჯერ და გადაეცით სხვადასხვა სახელი.

#5)შექმენით ფუნქცია, რომელიც იღებს ორ სტრინგს და მოახდინეთ კონკატენაცია.

#1)
def sum_numbers(a, b):
    return a + b
result = sum_numbers(5, 7)
print(result)


#2)
def even_or_odd(n):
    return "luwia" if n % 2 == 0 else "kentia"
print(even_or_odd(10))  
print(even_or_odd(7)) 

#3)
def positive_or_negative(n):
    if n > 0:
        return "dadebiti"
    elif n < 0:
        return "uaryopiti"
    else:
        return "nulis tolia"
print(positive_or_negative(5))   
print(positive_or_negative(-3)) 
print(positive_or_negative(0))  

#4)
def greet(name):
    print(f"Hello {name}")
greet("Giorgi")
greet("Mariam")

#5)
def concatenate_strings(str1, str2):
    return str1 + str2
result = concatenate_strings("Hello, ", "world!")
print(result) 




