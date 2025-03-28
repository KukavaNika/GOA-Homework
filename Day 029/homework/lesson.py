#1)შექმენით ფუნქცია რომელსაც გადაეცემა ორი რიცხვი შემდეგ დააბრუნეთ მათი ნამრავლი return ის გამოყენებით 
#2)ახსენით რაც დღეს გავიარეთ (isalnum,isdigit,islower,isnumeric,isupper,count) მეთოდები თითოეული რას აკეთებს.
#3)ასევე ახსენით რას აკეთებს min და max ჩაშენებული ფუნქციები
#4)გადახედეთ ჩანაწერს აუცილებლად თავიდან 

#1)
def multiply_numbers(a, b):
    return a * b
result = multiply_numbers(4, 5)
print(result)

#2)
#isalnum() ამოწმებს, არის თუ არა სტრიქონი მხოლოდ ასოებისა და ციფრებისგან (სპეციალური სიმბოლოების ან ინტერვალის გარეშე).
text = "Hello123"
print(text.isalnum()) 
text2 = "Hello 123!"
print(text2.isalnum())
 
#isdigit() ამოწმებს, შეიცავს თუ არა სტრიქონი მხოლოდ ციფრებს (0-9).
num = "12345"
print(num.isdigit())
num2 = "123abc"
print(num2.isdigit())

#islower () ამოწმებს, არის თუ არა სტრიქონში ყველა ასო პატარა.
text = "hello"
print(text.islower())
text2 = "Hello"
print(text2.islower())

#isnumeric () მსგავსია isdigit(), მაგრამ ასევე ცნობს სხვა ციფრულ სიმბოლოებს (როგორიცაა წილადები, ზედნაწერები და რომაული ციფრები).
num = "12345"
print(num.isnumeric())

num2 = "⅓" 
print(num2.isnumeric()) 

num3 = "123abc"
print(num3.isnumeric())

#isupper () ამოწმებს, არის თუ არა სტრიქონში ყველა ასო დიდი.
text = "HELLO"
print(text.isupper())

text2 = "Hello"
print(text2.isupper())

#count (ქვესტრიქონი) ითვლის რამდენჯერ გამოჩნდება კონკრეტული ქვესტრიქონი სტრიქონში.
sentence = "banana apple banana grape"
print(sentence.count("banana"))



#3)
 # min() აბრუნებს უმცირეს მნიშვნელობას სიიდან ან რიცხვების ნაკრებიდან.
numbers = [4, 7, 1, 9, 3]
print(min(numbers))


 # max() აბრუნებს უდიდეს მნიშვნელობას სიიდან ან რიცხვების ნაკრებიდან.
numbers = [4, 7, 1, 9, 3]
print(max(numbers))

# სტრინგების მაგალითი:
words = ["apple", "banana", "cherry"]
print(min(words))  # გამოიძახებს პირველს
print(max(words)) # გამოიძახებს ბოლოს


