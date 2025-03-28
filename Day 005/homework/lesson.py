#1)მომხმარებელს შემოატანინეთ float სახის რიცხვი და შემდეგ ეგ რიცხვი გაყავით floor division-ის დახმარებით რომ იყოს integer და არა float

#2)მოხმარებელს შემოატანინეთ თავის სახელი,გვარი,ასაკი,ჰობბი და ბალანსი შემდეგ ეს ყველაფერი დაბეჭდეთ print-ის საშუალებით

#3)გააკეთეთ 5 5-ი მაგალითი %-ზე და floor division-ზე //

#4)მოხმარებელს შემოატანინეთ რიცხვი და მაგ რიცხვს გამოაკელით 20 და გაამრავლეთ 3 ზე

#5)მოხმარებელს შემოატანინეთ რიცხვები ანუ num,num1,num2...და ასე შემდეგ და საბოლოოდ გამოითვალეთ მაგ რიცხების საშუალო არითმეტიკული
#მაგალიტად: 
#2, 2, 2 = 2 + 2 + 2 = 6 / 3 = 2 ანუ რიცხვების ჯამი გავყოთ რაოდენობაზე(მინიმუმ 3 რიცხვის ცვლადი გქონდეთ შექმნილი

#1)
num = float(input("enter your number: "))
result = num //1
print("floor division ",result)

#2)
firstname = input("enter your name: ")
lastname = input("enter your lastname: ")
age = input("enter your age: ")
hobbi = input("enter your hobbi: ") 
balance = float(input(" name = {nika} lastname = {kukava} age = {16} hobbie = {paint} balance = {100}"))

#3)
# მაგალითი %
a = 10
b = 3
print(f"10 % 3 = {a % b}") 

# მაგალითი %
a = 15
b = 4
print(f"15 % 4 = {a % b}")

# მაგალითი %
a = 20
b = 6
print(f"20 % 6 = {a % b}")

# მაგალითი floor division //
a = 10
b = 3
print(f"10 // 3 = {a // b}")

# მაგალით floor division //
a = 17
b = 4
print(f"17 // 4 = {a // b}")

#4)
num = float (input("enter your num: "))
result = (num - 20) * 3
print(f"result:")

#5)
numbers = input("enter nums: ").split(",")
numbers = [float(num) for num in numbers]
average = sum(numbers) / len(numbers) 
print(f"(average): ")
