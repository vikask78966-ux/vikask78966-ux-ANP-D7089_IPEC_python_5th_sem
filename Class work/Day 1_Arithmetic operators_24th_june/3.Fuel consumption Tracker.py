#Write a Python program to find the average mileage of a car.
#input the total distance travelled by the car in kilometers.
total_distance = float(input("Enter the total distance travelled by the car in kilometers:"))
#input the total fuel consumed by the car in liters.
total_fuel_consumed = float(input("Enter the total fuel consumed by the car in liters:"))
#calculate the average mileage by dividing the total distance by the total fuel consumed.
average_mileage = total_distance / total_fuel_consumed
#print the average mileage.
print("Average mileage of the car is :", average_mileage, "km/l")