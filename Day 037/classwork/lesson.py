
#1)
def to_camel_case(text):
    words = text.replace("-", " ").replace("_", " ").split()
    return words[0] + "".join(word.capitalize() for word in words[1:]) if words else ""

#2)
["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
