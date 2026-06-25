#Write a Python program to calculate the total cost of rice packets purchased.
#input the price of the rice packets.
rice_packet_price = float(input("Enter the price of the rice packets:"))
#input the number of the rice packets purchased.
number_of_packets = int (input("Enter the number of the rice packets purchased:"))
#calculate the total cost by multiplying the price and the number of packets.
total_cost = rice_packet_price * number_of_packets
#print the total cost.
print("Total cost of the rice packets purchased is :", total_cost)