

#https://www.codewars.com/kata/5ac6932b2f317b96980000ca/train/python

#https://www.codewars.com/kata/5aba780a6a176b029800041c/train/python

#https://www.codewars.com/kata/5a8059b1fd577709860000f6/train/python


#2)შეასრულეთ თქვენი არჩეული 3ცალი 8KYUანი ამოცანა
#3)შეასრულეთ თქვენი არჩეული 2ცალი 7KYUანი ამოცანა
#4)შეასრულეთ თქვენი არჩეული 1ცალი 6KYUანი ამოცანა

#1)
def no_odds(values):
    return [x for x in values if x % 2 == 0]

#2)
def no_space(x):
    return x.replace(" ", "")

    
#3)  
def litres(time):             
    return time // 2    
      

#4) 7kuy
def printer_error(s):
    errors = sum(1 for c in s if c > 'm')
    return f"{errors}/{len(s)}"

#5) 7 kuy
def reverse_words(text):
    return ' '.join(word[::-1] for word in text.split(' '))

#6) 6 kyu

def spin_words(sentence):
    return ' '.join(word[::-1] if len(word) >= 5 else word for word in sentence.split())


