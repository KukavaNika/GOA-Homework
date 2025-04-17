#1)https://www.codewars.com/kata/5963c18ecb97be020b0000a2/train/python

#2)https://www.codewars.com/kata/59dd3ccdded72fc78b000b25/train/python

#3)https://www.codewars.com/kata/55c28f7304e3eaebef0000da/train/python

#4)https://www.codewars.com/kata/526c7363236867513f0005ca/train/python

#5)https://www.codewars.com/kata/582dafb611d576b745000b74/train/python



#1)
def sum_even_numbers(seq):
    return sum(num for num in seq if num % 2 == 0)


#2)
def golf_score_calculator(par, score):
    return sum(int(s) - int(p) for p, s in zip(par, score))


#3)
def add_length(str_):
    return [f"{word} {len(word)}" for word in str_.split()]

#4)
def string_to_number(s):
    return int(s)

#5)
import re

def sum_of_integers_in_string(s):
    return sum(int(num) for num in re.findall(r'\d+', s))
