#Register Sheldon 

num_milk = 0
num_eggs = 0
num_bread = 0
left_over_dimes = 0
left_over_nickels = 0
left_over_pennies = 0
left_over_quarters = 0
left_over_dollars = 0

num_milk = int(input("How many milk gallons did you buy? " ))
num_eggs = int(input("How many cartons of eggs did you buy? "))
num_bread = int(input("How many loaves of bread did you buy? "))

milk_price = 3.89 * num_milk
egg_price = 1.54 * num_eggs
bread_price = 2.76 * num_bread
overall_price = (bread_price + egg_price + milk_price)*1.06
overall_price = round(overall_price, 2)

print ("Your bill is $" + str(overall_price) +" U.S. Dollars.")
bill_paying_with = int(input("How much cash will you be paying with? "))
change = bill_paying_with - overall_price
print ("Your change will be: " + str(change))

dollar_value = 1
if change - dollar_value >= 0:
    dollars = int(change / 1)
    print ("There will be " +  str(dollars) + " dollar(s).")
    left_over_dollars = change %1
    print left_over_dollars
else :
    dollars = int(change / 1)
    print ("There will be no dollars")
    left_over_dollars = change %1
    print left_over_dollars
    
quarter_value = 0.25
if left_over_dollars - quarter_value >= 0:
    quarters = int(left_over_dollars / 0.25)
    print ("There will be " +  str(quarters) + " quarter(s).")
    left_over_quarters = left_over_dollars %.25
    print left_over_quarters
else :
    quarters = int(left_over_quarters / 0.25)
    print ("There will be no quarters")
    left_over_quarters = left_over_dollars %.25
    print left_over_quarters
    
dime_value = 0.10
if left_over_quarters - dime_value >= 0:
    dimes = int(left_over_quarters / 0.10)
    print ("There will be " +  str(dimes) + " dime(s).")
    left_over_dimes = left_over_quarters %.10
    print left_over_dimes
else :
    dimes = int(left_over_dimes / 0.10)
    print ("There will be no dimes")
    left_over_dimes = left_over_quarters %.10
    print left_over_dimes
    
nickel_value = 0.05
if  left_over_dimes - nickel_value >= 0:
    nickels = int(left_over_dimes / 0.05)
    print ("There will be " +  str(nickels) + " nickel(s).")
    left_over_nickels = left_over_dimes %.05
    print left_over_nickels
else :
    nickels = int(left_over_nickels / 0.05)
    print ("There will be no nickels")
    left_over_nickels = left_over_dimes %.05
    print left_over_nickels
    
penny_value = 0.01
if left_over_nickels - penny_value >= 0:
    pennies = int(left_over_nickels / 0.01)
    print ("There will be " +  str(pennies) + " pennie(s).")
    left_over_pennies = left_over_nickels %.01
    print left_over_pennies
else :
    print "There will be no pennies"
    print left_over_pennies

