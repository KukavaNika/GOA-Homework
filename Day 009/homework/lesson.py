#1)მომხმარებელს შემოატანინეთ მისი ასაკი და გაიგეთ რამდენჯერ მოთავსდება რიცხვი 10 მასში

#2)მომხმარებელს შემოატანინეთ მისი სახელი და გაიგეთ უდრის თუ არა ის თქვენს სახელს

#3)მომხმარებელს შემოატანინეთ ორი რიცხვი (num1 და num2) და გაიგეთ რა იქნება ნაშთი, პირველი რიცხვის მეორეზე გაყოფის შემდეგ

#4)მომხმარებელს შემოატანინეთ მისი ასაკი და გაიგეთ არის თუ არა ის ლუწი (იყოფა თუ არა ზუსტად 2ზე) ანუ გვრჩება თუ არა ნაშთი ნული, ორზე გაყოფის შედეგად

#1)
age = int(input("Enter your age: "))
times_in_10 = age // 10
print(f"Your age can fit into 10 {times_in_10} times.")

#2)
user_name = input("Enter your name: ")
if user_name == "Your Name": 
    print("Your name matches mine!")
else:
    print("Your name does not match mine.")

#3)
num1 = int(input("Enter the first number (num1): "))
num2 = int(input("Enter the second number (num2): "))
remainder = num1 % num2
print(f"The remainder when {num1} is divided by {num2} is {remainder}.")

#4)
age = int(input("Enter your age: "))
if age % 2 == 0:
    print(f"Your age {age} is even.")
else:
    print(f"Your age {age} is odd.")

