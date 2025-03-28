#0)უყურეთ ჩანაწერს თავიდან

#1)მომხმარებელს შემოატანინეთ მისი სახელი და თუ ეს სახელი უდრის თქვენს სახელს, დაბეჭდეთ "Hello" სხვა შემთხვევაში "Bye".

#2)ცვლადში შეინახეთ თქვენი საყვარელი რიცხვი და მომხმარებელს შემოატანინეთ ასევე მისი საყვარელი რიცხვი, თუ თქვენი რიცხვები ემთხვევა მაშინ დაბეჭდეთ "Perfect" თუ მისი რიცხვი მეტია, დაბეჭდეთ "More", სხვა შემთხვევაში "Less".

#3)შექმენით for ციკლი 150ის დიაპაზონში და შეამოწმეთ თითოეული რიცხვი, თუ ეს რიცხვი არის ლუწი, მაშინ დაბეჭდეთ "Luwia" და გვერძე მიაწერეთ რიცხვი (მინიშნება ---> print("Luwia", i) ხოლო თუ იქნება კენტი, დაბეჭდეთ "Kentia" და გვერძე მიუწერეთ ეს რიცხვი.

#4)მომხმარებელს შემოატანინეთ მისი ასაკი და ასევე მისი სახელი, თუ მომხმარებლის სახელი ემთხვევა თქვენს სახელს და ასევე მისი ასაკი ემთხვევა თქვენს სახელს, დაბეჭდეთ "Twins" სხვა შემთხვევაში "Not Twins".

#5)შექმენით ცვლადი სადაც შეინახავთ ორიგინალ აქაუნთის პაროლს, და while ციკლის მეშვეობით მომხმარებელს შეეკითხეთ აქაუნთის პაროლი იქამდე სანამ სწორედ არ გამოიცნობს.

#1)
my_name = "nika"
user_name = input("enter your name: ")
if user_name == my_name:
    print("Hello")
else:
    print("Bye")

#2)
my_favorite_number = 7
user_favorite_number = int(input("enter your fav number: "))
if user_favorite_number == my_favorite_number:
    print("Perfect")
elif user_favorite_number > my_favorite_number:
    print("More")
else:
    print("Less")

#3)
for i in range(1, 151):
    if i % 2 == 0:
        print("Luwia", i)
    else:
        print("Kentia", i)

#4)
my_name = "nika"
my_age = 20
user_name = input("enter your name: ")
user_age = int(input("enter your age: "))
if user_name == my_name and user_age == my_age:
    print("Twins")
else:
    print("Not Twins")

#5)
original_password = "Secret123"
user_password = ""
while user_password != original_password:
    user_password = input("enter your password: ")
    if user_password != original_password:
        print("password inccorect try again!!!.")
    
print("password correct weloceme!")
