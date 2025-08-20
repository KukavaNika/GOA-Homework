


#7kyu
#1
def getCount(input_str):
    vowels = "aeiou"
    count = 0
    for char in input_str:
        if char in vowels:
            count += 1
    return count

#6kyu
#2
def find_odd(arr):
    result = 0
    for num in arr:
        result ^= num  
    return result

#7kyu
#3
def descending_order(num):
    return int("".join(sorted(str(num), reverse=True)))

#6kyu
#4
def spin_words(sentence):
    words = sentence.split()
    result = [
        word[::-1] if len(word) >= 5 else word
        for word in words
    ]
    return " ".join(result)


# მეტი ვერ ვქენი