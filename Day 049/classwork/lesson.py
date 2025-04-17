#1)https://www.codewars.com/kata/57fb09ef2b5314a8a90001ed/train/python

#2)https://www.codewars.com/kata/565f5825379664a26b00007c/train/python

#3)https://www.codewars.com/kata/57a1ae8c7cb1f31e4e000130/train/python

#4)https://www.codewars.com/kata/58dbdccee5ee8fa2f9000058/train/python

#5)https://www.codewars.com/kata/55a996e0e8520afab9000055/train/python



#1)
def replace_exclamation(s):
    return ''.join('!' if c.lower() in 'aeiou' else c for c in s)

#2)
def is_flush(cards):
    return len(set(card[-1] for card in cards)) == 1

#3)
def is_even(n): 
    return n % 2 == 0

#4)
def multiple(m, n):
    return ((n + m - 1) // m) * m

#5)
def amount_of_pages(summary):
    pages = 0
    digits = 0
    while digits < summary:
        pages += 1
        digits += len(str(pages))
    return pages
