list_of_numbers = [-2,-1,1,2,3,4,5,6,7,8,9]
print(list_of_numbers)

smallest = 1

for number in list_of_numbers:
    if number < smallest:
        smallest = number
print("========================\nThe smallest number is ")
print(smallest)