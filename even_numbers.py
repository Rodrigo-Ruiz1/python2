list_of_numbers = [1,2,3,4,6,8,7,9,11,10]
print(list_of_numbers)

print("==============================\nThe even numbers are: ")
for number in list_of_numbers:
    if (number % 2) == 0:
        print(number)