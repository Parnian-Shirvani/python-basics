# Kilometer to Mile converter

kilometers = float(input("Enter kilometers: "))
miles = kilometers / 1.60934 # 1 mile = 1.60934 km
miles = round(miles , 2)
print(f"{kilometers} kms = {miles} miles")