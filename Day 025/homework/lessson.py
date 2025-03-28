#1)შექმენით ცარიელი სია და for ციკლის მეშვეობით ჩაამატეთ ყველა ლუწი რიცხვი 0დან 200მდე, ბოლოს დაბეჭდეთ სია.

#2)შექმენით ცარიელი სია და for ციკლის მეშვოებით მომხმარებელს შეეკითხეთ მისი top 5 საყვარელი სახელი (ანუ ხუთჯერ input).

#3)შექმენით სია 10 ელემენტით და გამოიტანეთ მხოლოდ კენტ ინდექსზე მდგომი ელემენტები.

#4)შექმენით ცვლადი რომელშიც შენახული იქნება სტრინგი შემდეგ კი გაიგეთ ამ სტრინგის სიმბოლოების რაოდენობა.

#5)შექმენით სია შემდგარი 5 ელემენტისგან, მომხმარებელს შემოატანინეთ რიცხვი და სიიდან ამოაგდეთ შემოტანილ რიცხვის ინდექსზე მდგომი ელემენტი.

#6)შექმენით სია და დაბეჭდეთ ამ სიის სიგრძე.

#7)ვისაც არ დაგისრულებიათ საკლასო სამუშაო დაასრულეთ აუცილებლად.

#1)
even_numbers = []
for i in range(0, 201, 2):
    even_numbers.append(i)
print(even_numbers)

favorite_names = []
#2)
for i in range(5):
    name = input(f"enter your {i+1}-fav names: ")  
    favorite_names.append(name)
print(favorite_names)

#3)
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
odd_index_elements = [numbers[i] for i in range(len(numbers)) if i % 2 == 1]
print(odd_index_elements)

#4)
text = "Hello, world!"
length = len(text)
print(f"string length is: {length}") 

#5)
items = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
index_to_remove = int(input("Enter the index (0 to 4) to remove the element from.: "))  
if 0 <= index_to_remove < len(items):
    removed_item = items.pop(index_to_remove)
    print(f"{removed_item} remove by list.")
else:
    print("incorect index!")
print(items)  


