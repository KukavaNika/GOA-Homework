#https://www.codewars.com/kata/586f6741c66d18c22800010a/train/python
#https://www.codewars.com/kata/53dbd5315a3c69eed20002dd/train/python
#https://www.codewars.com/kata/5390bac347d09b7da40006f6/train/python
#https://www.codewars.com/kata/57eaeb9578748ff92a000009/train/python
#https://www.codewars.com/kata/5a2be17aee1aaefe2a000151/train/python
#https://www.codewars.com/kata/51c8991dee245d7ddf00000e/train/python
#https://www.codewars.com/kata/5966e33c4e686b508700002d/train/python


#1)
def triple_trouble(one, two, three):
    return ''.join(a + b + c for a, b, c in zip(one, two, three))


#2)
def filter_list(l):
    return [x for x in l if isinstance(x, int)]


#3)
class str:
    def toJadenCase(self):
        return ' '.join(word.capitalize() for word in self.split())

#4)
def sort_by_length(arr):
    return sorted(arr, key=len)

#5)
def positive_sum(arr):
    return sum(x for x in arr if x > 0)

#6)
def reverse_words(s):
    return ' '.join(s.split()[::-1])

#7)
def multiply(n):
    return n * (5 ** len(str(abs(n))))

