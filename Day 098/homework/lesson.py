#1) https://www.codewars.com/kata/679e0a54f8d448b508865c3b/train/python

#2) https://www.codewars.com/kata/5fc7caa854783c002196f2cb/train/python

#3) https://www.codewars.com/kata/56f253dd75e340ff670002ac/train/python

#4) https://www.codewars.com/kata/58a66c208b88b2de660000c3/train/python

#5) https://www.codewars.com/kata/552564a82142d701f5001228/train/python

#6) https://www.codewars.com/kata/52dbae61ca039685460001ae/train/python

#7) https://www.codewars.com/kata/526571aae218b8ee490006f4/train/python

#8) https://www.codewars.com/kata/598ee7b6ec6cb90dd6000061/train/python



#1) #ვერ გავაკეთე 


#2)
#ვერ გავაკეთე

#3)
def how_many_times(a, b):
    return b.count(a)

#4)



#5)
def nth_even(n):
    return (n - 1) * 2


#6)
def divisors(n):
    return sum(1 for i in range(1, n+1) if n % i == 0)

#7)
def count_bits(n):
    return bin(n).count("1")

#8)
def gap(num):
    return max(map(len, bin(num)[2:].strip("0").split("1")), default=0)
