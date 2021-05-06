#list_of_numbers = [1,2,3,4]

#largest = 1

#for number in list_of_numbers:
#    if largest > number:
#        print("The largest number is: " + str(largest))
#    largest = largest + 1





new_list_of_numbers = [3,2,1]

largest = 0

for num in new_list_of_numbers:
    # print("The current number is: " + str(num))
    # print("The current LARGEST number is: " + str(largest))
    # If the CURRENT NUMBER is greater than the CURRENT LARGEST
    # Assign the value of CURRENT NUMBER to LARGEST
    if num > largest:
        largest = num
print(largest)