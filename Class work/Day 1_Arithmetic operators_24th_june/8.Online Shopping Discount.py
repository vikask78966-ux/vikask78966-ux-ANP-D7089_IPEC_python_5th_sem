#Write a Python program to calculate the final payable amount after applying the discount.
#input the product price.
product_price = float(input("Enter the product price: "))
#input the Discount Amount
discount_amount = float(input("Enter the discount amount: "))
#calculate the final payable amount after applying the discount.

final_payable_amount = product_price - discount_amount
#output the final payable amount
print("The final payable amount after applying the discount is:", final_payable_amount)