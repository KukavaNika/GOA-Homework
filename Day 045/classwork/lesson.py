#https://www.codewars.com/kata/55902c5eaa8069a5b4000083/train/python

#https://www.codewars.com/kata/5388f0e00b24c5635e000fc6/train/python

#https://www.codewars.com/kata/5dd462a573ee6d0014ce715b/train/python

#https://www.codewars.com/kata/57241e0f440cd279b5000829/train/python

#https://www.codewars.com/kata/5a34b80155519e1a00000009/train/python

#https://www.codewars.com/kata/5761a717780f8950ce001473/train/python


#1)
def split_the_bill(group):
    avg = sum(group.values()) / len(group)
    return {person: round(amount - avg, 2) for person, amount in group.items()}

#2)
def twos_difference(lst):
    lst = sorted(lst)
    return [(x, x + 2) for x in lst if x + 2 in lst]


#3)
def max_element(arr):
    return max(arr) if arr else None


#4)
def sum_mul(n, m):
    return sum(range(n, m, n)) if n > 0 and m > 0 else "INVALID"

#5)
def multiple_of_index(arr):
    return [arr[i] for i in range(len(arr)) if i != 0 and arr[i] % i == 0]


#6)
def bmi(weight, height):
    b = weight / (height ** 2)
    return ("Underweight" if b <= 18.5 else
            "Normal" if b <= 25.0 else
            "Overweight" if b <= 30.0 else
            "Obese")
