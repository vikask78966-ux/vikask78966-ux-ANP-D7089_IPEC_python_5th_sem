#Write a Python program to calculate the total recharge amount based on the data pack selected.
#input coat per GB.
cost_per_gb = float(input("Enter the cost per GB: "))
#input the number of GBs in the data pack.
num_gbs = int(input("Enter the number of GBs in the data pack: "))
#calculate the total recharge amount.
total_recharge_amount = cost_per_gb * num_gbs
#output the total recharge amount.
print("The total recharge amount for the selected data pack is:", total_recharge_amount)