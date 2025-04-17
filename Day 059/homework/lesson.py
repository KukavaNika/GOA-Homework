#1)https://www.codewars.com/kata/559590633066759614000063/train/python
#2)https://www.codewars.com/kata/526c7363236867513f0005ca/train/python
#3)https://www.codewars.com/kata/526c7363236867513f0005ca/train/python
#4)https://www.codewars.com/kata/5300901726d12b80e8000498/train/python
#5)https://www.codewars.com/kata/58a66c208b88b2de660000c3/train/python



#1)
def min_max(lst):
    return [min(lst), max(lst)]

#2)
def string_to_array(s):
    return s.split(" ")

#3)
 # ვერ გავაკეთე

#4)
class Block:
    def __init__(self, data):
        self.width = data[0]
        self.length = data[1]
        self.height = data[2]

    def get_width(self):
        return self.width

    def get_length(self):
        return self.length

    def get_height(self):
        return self.height

    def get_volume(self):
        return self.width * self.length * self.height

    def get_surface_area(self):
        w, l, h = self.width, self.length, self.height
        return 2 * (w * l + l * h + h * w)


#5)
def reverse_alternate(string):
    words = string.strip().split()
    for i in range(len(words)):
        if i % 2 == 1:
            words[i] = words[i][::-1]
    return ' '.join(words)
