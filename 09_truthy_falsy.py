# truthiness and falsiness

if 1 :
    print("1 is true")
else :
    print("1 is false")

if 0 :
    print("0 is true")
else :
    print("0 is false")

print("__________________")

# False
print(bool("")) # empty strings
print(bool([])) # empty lists
print(bool(None))

print("__________________")

# True
print(bool("Pari"))
print(bool([1,2,3]))
print(bool(4)) # any number except 0 -> True

print("__________________")

test = []
if test :
    print("List is not empty.")
else :
    print("List is empty.")

print("__________________")