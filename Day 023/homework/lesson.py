#0)ჩანაწერს გადახედეთ თავიდან

#1) მომხმარებელს შემოატანინეთ მისი სახელი დიდი ასოებით და შეინახეთ ცვლადში სახელად name და .lower() ფუნქციის მეშვეობით გადააქციეთ ცვლადის მნიშვნელობა  პატარა ასოებად. 

#2) ცვლადში შეინახეთ თქვენი გვარი პატარა ასოებით, შემდეგ .upper() ფუნქციის მეშვეობით გადააქციეთ ცვლადის მნიშვნელობა  დიდ ასოებად.

#3) ცვლადში შეინახეთ სტრინგი პატარა ასოებით, შემდეგ .capitalize() ფუნქციის მეშვეობით გადააქციე პირველი ასო დიდ ასოდ.

#4)ცვლადში შეინახეთ რაიმე სტრინგი,შემდეგ find() ფუნქციის მეშვეობით იპოვეთ რომელ ინდექსზეა კონკრეტული ასო

#5)შექმენით სია სტრინგით და თითოეული სტრინგი გადაიყვანეთ დიდ ასოებად for ციკლის მეშვეობით

#1)
name = input("Enter your name in letters: ")
name = name.lower()
print(name)  

#2)
surname = "gelashvili"
surname = surname.upper()
print(surname) 


#3)
text = "hello world"  
text = text.capitalize()
print(text)  

#4)
sentence = "programming is fun"  
index = sentence.find("g")
print(index)  

#5)
words = ["apple", "banana", "cherry", "grape"]
uppercase_words = [word.upper() for word in words]
print(uppercase_words)  