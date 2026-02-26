# while loop 

num = 1 
while num < 11 : 
    print(num)
    num += 1 

# sum of numbers from 1 to 10  
num = 1 
Sum = 0
while num < 10 + 1 :
    Sum = Sum + num 
    num += 1 
print(f"Sum = {Sum}")

# product of numbers from 1 to 10
num = 1
Product = 1 
while num < 10 + 1 :
    Product = Product * num 
    num += 1 
print(f"Product = {Product}")

# break : stop the code 
num = 1 
while num < 10 + 1 :
    print(num)
    num += 1 
    if num == 6 :
        break  

# difference is in the last number 

num = 1 
while num < 10 + 1 :
    print(num)
    if num == 6 :
        break
    num += 1  