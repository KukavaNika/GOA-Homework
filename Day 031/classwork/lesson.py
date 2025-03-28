#code wars
#1)
def solution(string):
    return string[::-1]
print(solution("hello"))
print(solution("world"))

#2)
def number_to_string(num):
    return str(num)
print(number_to_string(123))
print(number_to_string(999))
print(number_to_string(-100))

#3)
def boolean_to_string(b):
    return str(b)
print(boolean_to_string(True))
print(boolean_to_string(False))

#4)
def make_upper_case(s):
    return s.upper()
print(make_upper_case("hello"))
print(make_upper_case("world"))
print(make_upper_case("Python"))

#5)
def bool_to_word(b):
    return "Yes" if b else "No"
print(bool_to_word(True))
print(bool_to_word(False))

#6)
def remove_char(s):
    return s[1:-1]
print(remove_char("hello"))
print(remove_char("world"))
print(remove_char("ab"))



