# Strings in Python

text = "test"
name = "Parnian"

# Concatenation
full_text = "Hello" + " " + name
print(full_text)

# f-string
print(f"Hello {name}")

word = "Python"

# length
length = len(word)
print(length)

# Indexing
print(word[0]) # index starts from 0
print(word[1])
print(word[2])
print(word[-1]) # last character of the string 

# strings as input 
word = input("Enter everything you want : ") # input always returns string
print(type(word)) # String class