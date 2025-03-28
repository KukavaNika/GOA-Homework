#1)შემოიტანეთ თქვენი ოჯახის წევრების ასაკი და დაუპრინტეთ თუ რამდენი წლისები იქნებიან 25 წლის შემდეგ(გამოიყენეთ int ფუნქცია).
#2)მომხმარებელს შემოატანინეთ მისი სახელი და type ფუნქციის საშუალებით გაიგეთ რა ტიპის მონაცემია შემოტანილი მნიშვნელობა.
#3)მომხმარებელს შემოატანინეთ მისი ასაკი და შემდეგ გადააქციეთ სტრინგად
#4)კომენტარებით ახსენით რას აკეთებს str(),int() და float() ფუნქციები.

#1)
fatherage = int(input("Enter father's age: "))
motherage = int(input("Enter mother's age: "))
print("Father's age in 25 years:", fatherage + 25)
print("Mother's age in 25 years:", motherage + 25)

#2)
user_name = input("Enter your name: ")
print("The type of the entered value is:", type(user_name))

#3)
user_age = int(input("Enter your age: "))
user_age_str = str(user_age)
print("Your age as a string:", user_age_str)

#4)
# str() -  გარდაქმნის მნიშვნელობას სტრიქონად
# int() - გარდაქმნის მნიშვნელობას მთელ რიცხვად
# float() - მნიშვნელობას გარდაქმნის float-ად ანუ ათწილადად 
