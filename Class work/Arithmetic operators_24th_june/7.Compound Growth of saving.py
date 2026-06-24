#Write a Python program to calculate the value of money after a certain number of years assuming it doubles every year.
#input the initial amount of money (principal)
intial_amount = float(input("Enter the initial amount of money: "))
#input the number of years
Number_of_years = int(input("Enter the number of years: "))
#calculate the final amount after the specified number of years
final_amount = intial_amount * (2 ** Number_of_years)
#output the final amount
print("The value of money after", Number_of_years, "years is:", final_amount)