#Write a Python program to calculate how much each participant should pay.
#input the taotal event coast.
total_event_cost = float(input("Enter the total event cost: "))
#input the number of participants.
num_participants = int(input("Enter the number of participants: "))
#calculate the amount each participant should pay.
amount_per_participant = total_event_cost / num_participants
#output the amount each participant should pay.
print("Each participant should pay:", amount_per_participant)   