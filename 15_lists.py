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
        print(f"{item} is a mathematics course.")
    else :
        print(f"{item} is a number.")

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

# lists and methods
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

list_2.remove(22) # delete first 22 in list_2
print(list_2)

print("____________________________")

list_2.clear() # emty the list
print(list_2)

print("____________________________")

################################################### not in github
list_3 = [1,9,2,8,3,7,4,6,5,5]
print(f"list_3 : {list_3}")

print("____________________________")

index_of_first_5 = list_3.index(5) # returns the index of first 5 in list
print(f"the index of first 5 : {index_of_first_5}")

print("____________________________")

count_of_5 = list_3.count(5) # returns count of 5 in list
print(f"count of 5 : {count_of_5}")

print("____________________________")

print(f"list_3 = {list_3}")
list_3.reverse() # reverse the order of the list (then put it in the same list)
print(f"reverse of list_3 : {list_3}")

print("____________________________")

list_4 = [1,9,2,8,3,7,4,6,5,5]
print(f"list_4 : {list_4}")
list_4.sort() # sort the order of the list (then put it in the same list)
print(f"sort_list_4 : {list_4}")

print("____________________________")

# "str".join(iterable) 
list_5 = ["a","b","c","d","e","f","g","h"]
print(f"list_5 : {list_5}")
print("_".join(list_5))

print(f"example with strings : {" ".join("Parnian")}")

print("____________________________")

# list slicing --> List_Name[start(index) : stop(index) : step]
list_6 = [1,2,3,4,5,6,7,8,9,10]
slice_1 = list_6[1:5] # returns members with index 1 to 4
print(f"slice_1 : {slice_1}")

slice_2 = list_6[5:] # returns member with index 5 and after that
print(f"slice_2 : {slice_2}")

slice_3 = list_6[:5] # returns member with index 4 and before that
print(f"slice_3 : {slice_3}")

slice_4 = list_6[1:11:2] 
print(f"slice_4 : {slice_4}")

slice_5 = list_6[:] # returns a list with same members but not the same list
print(f"slice_5 : {slice_5}")
print(f"slice_5 == list_6 : {slice_5 == list_6}") # same members
print(f"slice_5 is list_6 : {slice_5 is list_6}") # different list

slice_6 = list_6[-5:] # negative index as start returns from the index till last_index
print(f"slice_6 : {slice_6}")

slice_7 = list_6[:-5] # negative index as stop returns from index_0 till the index
print(f"slice_7 : {slice_7}")

slice_8 = list_6[::3]
print(f"slice_8 : {slice_8}")

slice_9 = list_6[::-1]
print(f"slice_9 : {slice_9}")

print("____________________________")

# list comprehension
numbers = [1,2,3,4,5,6,7,8,9,10]
doubled_numbers_1 = []
for num in numbers :
    doubled_numbers_1.append(num * 2)

print(f"doubled-numbers_1 : {doubled_numbers_1}")

doubled_numbers_2 = [num * 2 for num in numbers]
print(f"doubled_numbers_2 : {doubled_numbers_2}")

even_numbers = [num for num in numbers if num % 2 == 0]
print(f"even_numbers : {even_numbers}")

odd_numbers = [num for num in numbers if num % 2 == 1]
print(f"odd_numbers : {odd_numbers}")

new_list = [num * 2 if num % 2 == 1 else num * 4 for num in numbers]
print(f"new_list : {new_list}")

my_name = "Parnian"
characters_list = [char for char in my_name]
print(f"characters_list : {characters_list}")

print("____________________________")

# nested lists : [[,],[,],[,]]
list_of_lists = [[1,2,3],[4,5,6],[7,8,9]]
print(list_of_lists[1])
print(list_of_lists[1][1])

print("____________________________")

for list in list_of_lists :
    print(list)
    for num in list :
        print(num)

print("____________________________")

example_list = [[num * 3 for num in list] for list in list_of_lists]
print(f"example_list : {example_list}")

print("____________________________")

generated_list_1 = [[num for num in range(1,5)] for num in range(1,4)]
print(f"generated_list_1 : {generated_list_1}")

print("____________________________")

generated_list_2 = [[num * 2 if num % 2 == 0 else num * 3 for num in range(1,5)] for number in range(1,4)]
print(f"generated_list_2 : {generated_list_2}")