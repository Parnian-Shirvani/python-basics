# for loop and range()

# range()
num = range(10) # start : 0 , stop : 10 , last number : 9
numList1 = list(num) # [0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9]
print(f"numList1 is {numList1}")

numList2 = list(range(1,10,2)) # start : 1 , stop : 10 , step : 2 
print(f"numList2 is {numList2}") # [1 , 3 , 5, 7 , 9]

print("______________________________")

# for loop

for number in range(10) :
    print(number)

for item in range(10) :
    print("*" * item)
