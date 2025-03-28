#for loop
#1)გამოიტანეთ რიცხვები 0-დან 10-ის ჩათვლით
#2)გამოიტანეთ რიცხვები 50-დან 150-მდე
#3)გამოიტანეთ მხოლოდ ლუწი რიცხვები 200-დან 500-მდე
#4)გამოიტანეთ კენტი რიცხვები 0-დან 50-მდე
#5)მომხმარებელს შემოატანინეთ მისი გვარი და გამოიტანეთ ამ გვარის თითოეული ასო ცალცალკე
#6)კომენტარის სახით ახსენით როდის ვიყენებთ For Loop-ს

#1)
for number in range(0, 11):
    print(number)


#2)
for number in range(50, 151):
    print(number)

#3)
for number in range(200, 501):
    print(number)

#4)
for number in range(1, 51, 2 ):
    print(number)


#5)
last_name = input("enter your lastname: ")
for letter in last_name:
    print(letter)

#6)
#for ციკლი გამოიყენება მაშინ, როდესაც ჩვენ უნდა გავიგოთ კოლექცია, როგორიცაა სია, ტუპლი, სტრიქონი, დიაპაზონი, ან სხვა iterable ტიპები.


# while loop
#1)გამოიტანეთ რიცხვები 10-დან 15-მდე
#2)გამოიტანეთ რიცხვები 50-დან 0-მდე
#3)კომენტარის სახით ახსენით რა არის counter ცვლადი და როდის ვიყენებთ While Loop-ს
#4)გამოიტანეთ მხოლოდ ლუწი რიცხვები 10-დან 70-მდე
#5)გამოიტანეთ კენტი რიცხვები 25-დან 55-მდე


#1)
number = 10
while number <= 15:
    print(number)
    number += 1
#2)
number = 50
while number >= 0:
    print(number)
    number -= 1

#3)
# counter ცვლადი არის ცვლადი, რომელსაც იყენებენ რიცხვების დათვლაში ან ციკლის გამეორებებში.
#ვიყენებთ while loop-ს მაშინ, როდესაც არ ვიცით წინასწარ რამდენი iterations (ბრუნვა) იქნება საჭირო.

#4)
number = 10
while number <= 70:
    if number % 2 == 0:
        print(number)
    number += 1

#5)
number = 25
while number <= 55:
    if number % 2 != 0:
        print(number)
    number += 1

