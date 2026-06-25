#Write a Python program to calculate the remaining balance after withdrawal.
#input the current balance in the bank account.
current_balance = float(input("Enter the current balance in the bank account:"))
#input the amount to be withdrawn from the bank account.        
withdrawal_amount = float(input("Enter the amount to be withdrawn from the bank account:"))
#calculate the remaining balance by subtracting the withdrawal amount from the current balance.
remaining_balance = current_balance - withdrawal_amount
#print the remaining balance.
print("Remaining balance in the bank account is :", remaining_balance)