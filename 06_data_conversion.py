# Converting data  

x = input("Enter a number: ")
print(x , type(x)) # str

y = int(float(x)) # int --> convert to integer
print(y , type(y)) # int

z = float(x) # float --> convert to float
print(z , type(z)) # float

test_01 = "22"
print(test_01 , type(test_01))

test_01 = int(test_01)
print(test_01 , type(test_01))

test_02 = "159.5"
print(test_02 , type(test_02))

test_02 = float(test_02)
print(test_02 , type(test_02))

test_03 = int(test_02)
print(test_03 , type(test_03))

test_04 = float(test_03)
print(test_04 , type(test_04))