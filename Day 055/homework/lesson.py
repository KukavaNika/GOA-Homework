#1) შექმენით dictionary სადაც შეინახავთ მინიმუმ 3 key'ს და ასევე შექმენით 2 ცარიელი სია for loop'ის დახმარებით პირველ სიაში დაამატეთ key ხოლო მეორე სიაში კი value ბოლოს კი გამოიტანეთ ერთად. 

#2) მოცემული გაქვთ რაიმე result ცვლადი რომელშიც შეყვანილია სია [10,43,12,11,94,10,55,7,11] თქვენი დავალებაა გააქროთ ყველა დუბლიკატი ლისტიდან „თანმიმდევრობას მნიშვნელობა არაქვს“.

#3) დღევანდელ ახსნილ მეთოდებზე გააკეთეთ მაგალითები თითო მეთოდზე 5 მაგალითი მაინც.

#4) შექმენით ცარიელი dictionary შემდეგ მომხმარებელს შემოატანინეთ ჯერ key  შემდეგ კი value ამის შემდეგ თხოვეთ შეცვალოს ძველი value  და შემოატანინეთ ახალი მნიშვნელობა შემდეგ კი გამოიტანეთ საბოლოო dictionary.

#5) შექმენით სეტის მსგავსი ფუნქცია რომელიც მიიღებს ლისტს და ლისტიდან წაშლის დუბლიკატებს „ფუნქციაში არ გამოიყენოთ სეტი“


#1)
data = {
    "name": "Gio",
    "age": 25,
    "city": "Tbilisi"
}

keys = []
values = []
for key in data:
    keys.append(key)
    values.append(data[key])

print("Keys:", keys)
print("Values:", values)

#2)
result = [10, 43, 12, 11, 94, 10, 55, 7, 11]
unique_result = list(set(result))
print(unique_result)

#3)
my_list = [1, 2, 3]

my_list.append(4)  

my_list.insert(1, 99) 

my_list.remove(2) 

my_list.pop()  

my_list.extend([7, 8]) 

print(my_list)

#4)

user_dict = {}

key = input("key: ")
value = input("value: ")


user_dict[key] = value

new_value = input(f"{key}:")
user_dict[key] = new_value

print( user_dict)

#5)
def remove_duplicates(lst):
    new_list = []
    for item in lst:
        if item not in new_list:
            new_list.append(item)
    return new_list

my_list = [1, 2, 2, 3, 4, 1, 5, 3]
print(remove_duplicates(my_list))

