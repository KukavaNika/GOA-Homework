#1)უყურეთ ჩანაწერს ხელმეორედ (აუცილებლად!)

#2)შექმენით 8 ცვლადი სადაც შეინახავთ ყველა შესაძლო ლოგიკური ოპერატორის მაგალითს (4 ცალი or / 4 ცალი and)

#3)მომხმარებელს შემოატანინეთ მისი სახელი, შემოატანინეთ მისი ასაკი, ასევე სიმაღლე და შეამოწმეთ თუ მომხმარებლის ასაკი მეტია 18 და მისი სახელი უდრის თქვენს სახელს და ასევე მისი სიმაღლე მეტია 1.80-ზე

#4)ახსენით თითოეული ალგორითმის გამოსახვის გზა (flowchart / pseudocode / natural language)

#5)კომენტარის სახით ახსენით რა არის ალგორითმი და მოიყვანეთ რეალური ცხოვრების 3 მაგალითი

#1
or_example_1 = True or False
or_example_2 = False or True
or_example_3 = False or False
or_example_4 = True or True


and_example_1 = True and False
and_example_2 = False and False
and_example_3 = False and True
and_example_4 = True and True

print(or_example_1)
print(or_example_2)
print(or_example_2)
print(or_example_2)

print(and_example_1)
print(and_example_1)
print(and_example_1)
print(and_example_1)

#2
myname = "nika"
user_name = (input("enter your name: "))
user_age =  int(input("enter your age: "))
user_height = int(input("enter your height :"))
if user_age  > 18 and user_name == myname and user_height > 1.80 :
    print("registration complete")
else:
    print("registration feild!!!")

#4
#flowchat წარმოადგენს ვიზუალურ მეთოდს, რომლითაც აღწერილია ალგორითმის ნაბიჯები სიმბოლოებისა და ისტერიკული  ხაზების გამოყენებით.
#pseudocode წარმოადგენს ალგორითმის აღწერის საშუალებას.
#natural language ბუნებრივი ენა წარმოადგენს ალგორითმის აღწერას ადამიანურ ენაზე, რაც ყველაზე გასაგებია აუდიტორიისთვის.

#5
#ალგორითმი არის პროცედურა ან ინსტრუქციის სერია, რომელიც განკუთვნილია კონკრეტული პრობლემის გადასაჭრელად. 
#ეს პროცედურა მოიცავს კონკრეტულ ნაბიჯებს, რომლებიც უზრუნველყოფს მიზნის მიღწევას. 
# მაგ : 
#1. გახსენი GPS აპლიკაცია.
#2. შეიყვანე დაწყების და დანიშნულების ადგილები.
#3. აპლიკაცია აწარმოებს გზის რუკას.
#4. ადევნე თვალყური გზის რუკას და მიადევნე თვალი მითითებული მიმართულებით.
#5. ყოველ ნაბიჯზე დაინახავ გამოჩნდება შეტყობინებები (როგორც კი მარცხნივ ან მარჯვნივ მობრუნება).
#6. და ბოლოს შნი მიზანი მიღწეული იქნება .