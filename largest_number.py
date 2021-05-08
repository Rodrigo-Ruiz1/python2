list_of_numbers = [3,2,1,100,9]
print(list_of_numbers)

largest = 0

for num in list_of_numbers:
    # print("The current number is: " + str(num))
    # print("The current LARGEST number is: " + str(largest))
    # If the CURRENT NUMBER is greater than the CURRENT LARGEST
    # Assign the value of CURRENT NUMBER to LARGEST
    if num > largest:
        largest = num
print("=====================\nThe largest number is ")
print(largest)