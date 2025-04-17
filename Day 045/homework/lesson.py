#https://www.codewars.com/kata/55902c5eaa8069a5b4000083/train/python

#https://www.codewars.com/kata/5388f0e00b24c5635e000fc6/train/python

#https://www.codewars.com/kata/5dd462a573ee6d0014ce715b/train/python

#https://www.codewars.com/kata/57241e0f440cd279b5000829/train/python

#https://www.codewars.com/kata/5a34b80155519e1a00000009/train/python

#https://www.codewars.com/kata/5761a717780f8950ce001473/train/python


#1)
def rectangles(n, m):
    return (n * (n + 1) * m * (m + 1)) // 4


#2)
def to_camel_case(text):
    parts = text.replace('-', '_').split('_')
    return parts[0] + ''.join(p.capitalize() for p in parts[1:]) if parts else ''


#3)
def domain_name(url):
    url = url.replace("http://", "").replace("https://", "").replace("www.", "")
    return url.split('.')[0]


#4)
def fourth_bit(n):
    return (n >> 3) & 1

#5)
def multiplication_table(n):
    return [[(i + 1) * (j + 1) for j in range(n)] for i in range(n)]


#6)
def set_alarm(employed, vacation):
    return employed and not vacation

