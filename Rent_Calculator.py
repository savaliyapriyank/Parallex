# rent calculator in python : 

## Inputs we need from the user
# Total rent
# Total food ordered for snacking
# Electricity units spend
# Charge per unit 
# Persons living in room/flat

## Output
# Total amount you've to pay is :

Rent = int(input("Total Rent = "))
Food = int(input("Total food ordered for snacking = "))
Units = int(input("Electricity units spend = "))
Unit_charge = int(input("Charge per unit = "))
Person = int(input("Persons living in room/flat = "))

Final_unit_char = Units * Unit_charge
Output = (Rent + Food + Final_unit_char) // Person

print("Total amount you've to pay is : " , Output)