#1)https://www.codewars.com/kata/58649884a1659ed6cb000072/train/python

#2)https://www.codewars.com/kata/5513795bd3fafb56c200049e/train/python

#3)https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3/train/python

#4)https://www.codewars.com/kata/576bb71bbbcf0951d5000044/train/python

#5)https://www.codewars.com/kata/55225023e1be1ec8bc000390/train/python

#1)
def update_light(current):
    if current == "green":
        return "yellow"
    elif current == "yellow":
        return "red"
    elif current == "red":
        return "green"


#2)
def count_by(x, n):
    return [x * i for i in range(1, n + 1)]

#3)
def abbrev_name(name):
    first, last = name.upper().split()
    return f"{first[0]}.{last[0]}"

#4)
#ვერ გავაკეთე

#5)
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
