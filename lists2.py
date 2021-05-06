# Sum the Numbers
# Create a list of numbers, print their sum.

list_of_numbers = [1,2,3]

#print(sum(list_of_numbers))

total = 0

# Version 1
# This prints the numbers ND the total as it changes
# for number in list_of_numbers:
#    print("The number is now: " + str(number))
#    total = total + number
#    print("The total is now: " + str(total))

# Version 2
# This prints the new total each time
# for number in list_of_numbers:
#    #print("The number is now: " + str(number))
#    total = total + number
#    print("The total is now: " + str(total))

# Version 3
# This prints just the final total
for number in list_of_numbers:
    total = total + number
print("The total is now: " + str(total))