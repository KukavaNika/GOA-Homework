

# 1) აუცილებლად გააკეთეთ ეს codewars:
#https://www.codewars.com/kata/5fc7caa854783c002196f2cb/train/python

#2) ამის გარდა შეასრულეთ 5 ცალი 7 kyu და 5 ცალი 6 kyu ამოცანა თითოეულ ამოცანას კომენტარის სახით დაუწერეთ განმარტება თქვენივე სიტყვებით (გაუგებარი ამოცანები ჩაინიშნეთ და განვიხილავთ გაკვეთილზე) 


#1
def all_even_digits(n: int) -> bool:
    return all(int(d) % 2 == 0 for d in str(abs(n)))

#2)

#1
def square_digits(num: int) -> int:
    return int("".join(str(int(d)**2) for d in str(num)))

#2
def DNA_strand(dna: str) -> str:
    pair = {"A": "T", "T": "A", "C": "G", "G": "C"}
    return "".join(pair[ch] for ch in dna)

#3
def descending_order(num: int) -> int:
    return int("".join(sorted(str(num), reverse=True)))

#4
def get_middle(s: str) -> str:
    mid = len(s) // 2
    return s[mid-1:mid+1] if len(s) % 2 == 0 else s[mid]

#6kyu
#1
def find_uniq(arr: list) -> float:
    a, b = set(arr)
    return a if arr.count(a) == 1 else b

#2
def persistence(n: int) -> int:
    count = 0
    while n >= 10:
        prod = 1
        for d in str(n):
            prod *= int(d)
        n = prod
        count += 1
    return count

