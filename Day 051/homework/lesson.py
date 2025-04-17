#
#```
#1)გადახედეთ ამ რესურსებს:
#https://www.w3schools.com/python/python_tuples.asp
#https://www.w3schools.com/python/python_tuples_access.asp
#https://www.w3schools.com/python/python_tuples_update.asp
#https://www.w3schools.com/python/python_tuples_unpack.asp
#https://www.w3schools.com/python/python_tuples_loop.asp

#2) შემენით tuple, რომელშიც შეინახავთ საყიდლების სიას და მოახდინეთ მათი unpacking (დაშლა),რათა მიანიჭოთ თითოეული ელემენტი ცალკეულ ცვლადებს და დაბეჭდეთ ეს ცვლადები.

#3) შექმენით tuple და შეინახეთ Fast food პროდუქტები. შემდეგ შეცვალეთ ეს tuple და მათში ჩაამატეთ ჯანსაღი საკვები პროდუქტები.

#4) კომენტარის სახით ახსენით, თუ რა ფუნქციას ასრულებს Asterisk და როგორ აღინიშნება ის.

#5) მოცემულია შემდეგნაირი tuple:

#months = ("January", "February", "March", "April", "May")
#(first, second, third, fourth*)= months

#რას გამოიტანს მოცემული კოდი?
#print(first)
#print(second)
#print(third)
#print(fourth)


#1)

shopping = ("bread", "milk", "cheese", "eggs", )

bread, milk, cheese, eggs = shopping


print(bread)
print(milk)
print(cheese)
print(eggs)

#2)

fast_food = ("ბურგერი", "კარტოფილი", "პიცა")

updated_food = fast_food + ("ავოკადო", "სალათი", "გრეჩიხა")

print(updated_food)


#3)
# Asterisk (*)
# გამოიყენება მრავალი ელემენტის ჩასატევად ერთ ცვლადში.
# მაგალითად:
a, *b, c = (1, 2, 3, 4, 5)
# აქ:
# a = 1
# b = [2, 3, 4]
# c = 5


#5)
months = ("January", "February", "March", "April", "May")
(first, second, third, *fourth) = months

print(first) 
print(second)  
print(third)  
print(fourth)  
