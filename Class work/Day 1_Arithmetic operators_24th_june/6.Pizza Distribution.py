#write a program to find how many slices remain after equal distrinution.
#input the total number of slices.
total_slices = int(input("Enter the total number of slices: "))
#input the number of children to distribute the slices.
num_children = int(input("Enter the number of children: "))
#calculate the number of slices each child gets
slices_per_child = total_slices // num_children
#calculate the number of remaining slices
remaining_slices = total_slices % num_children
#output the results
print("Each child gets", slices_per_child, "slices.")
print("There are", remaining_slices, "slices remaining.")