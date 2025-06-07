#1) https://www.codewars.com/kata/52f3149496de55aded000410/train/python

#2) https://www.codewars.com/kata/52dbae61ca039685460001ae/train/python

#3) https://www.codewars.com/kata/52aeb2f3ad0e952f560005d3/train/python

#4) https://www.codewars.com/kata/5264d2b162488dc400000001/train/python

#5) დამატებით გააკეთეთ 5 ცალი 6kyu ამოცანა


#1)
def digital_root(n):
    while n >= 10:
        n = sum(int(d) for d in str(n))
    return n



#2)
def no_space(x):
    return x.replace(" ", "")


#3)
# ვერ გავიგე


#4)
def spin_words(sentence):
    return ' '.join(word[::-1] if len(word) >= 5 else word for word in sentence.split())

#5)
def find_it(seq):
    for i in seq:
        if seq.count(i) % 2 != 0:
            return i


#6) 6 kyu
 
#1
def camel_case(string):
    return ''.join(word.capitalize() for word in string.split())


#2
def order(sentence):
    return ' '.join(sorted(sentence.split(), key=lambda w: sorted([int(c) for c in w if c.isdigit()])))


#3
def duplicate_encode(word):
    word = word.lower()
    return ''.join('(' if word.count(c) == 1 else ')' for c in word)


#4
#ვერ გავაკეთე


#5
#ვერ გავაკეთე

