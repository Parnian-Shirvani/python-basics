# lists : can have anything as a member

list_1 = ["Algebra" , "Geometry" , "Analysis" , "Linear Algebra" , "Statistics" , "Number Theory" , "Game Theory" , 1 , 2 , 3 ]
list_2 = [1.59 , 22 , "Parnian" , [1 , 2 , 3] , 3 == 4 , 22 , True]
print(f"list_1 : {list_1}")
print(f"list_2 : {list_2}")

print("____________________________")

# indexing
print(list_1[0]) # first member
print(list_1[2]) # index = 2 --> third member
print(list_1[-1]) # last member
print(list_1[-2]) # negative index

print("____________________________")

# length of a list (built-in function)
length_list_1 = len(list_1)
print(f"length of list_1 : {length_list_1}")

length_list_2 = len(list_2)
print(f"length of list_2 : {length_list_2}")

print("____________________________")

# lists and for loop
for i in range(length_list_1) :
    if type(list_1[i]) == str :
        print(f"{list_1[i]} is a mathematics course.")
    else :
        print(f"{list_1[i]} is a number.")

print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ ")

for item in list_1 :
    if isinstance(item, str) :
        print(f"{list_1[i]} is a mathematics course.")
    else :
        print(f"{list_1[i]} is a number.")

print("____________________________")

# lists and while loop
index = 0 
while index < length_list_1 :
    if type(list_1[index]) == str :
        print(f"{list_1[index]} is a mathematics course.")
    else :
        print(f"{list_1[index]} is a number.")
    index += 1 

print("____________________________")

# lists and built-in functions
print(f"list_1 : {list_1}")

print("____________________________")

list_1.append("Optimization") # add only one member to the list
print(list_1)

print("____________________________")

list_1.extend(["Cryptography" , "Code Theory"]) # add a list of members to the list
print(list_1)

print("____________________________")

list_1.insert(4 , "Probability") # add a member in every place you want
print(list_1)

print("____________________________")

print(f"list_2 : {list_2}")

print("____________________________")

pop_mem = list_2.pop() # delete the last member 
print(f"pop_mem : {pop_mem}")
print(list_2)

print("____________________________")

list_2.pop(4) # delete the member with index 4
print(list_2)

print("____________________________")

list_2.remove(22) # delet first 22 in list_2
print(list_2)

print("____________________________")

list_2.clear() # emty the list
print(list_2)