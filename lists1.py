power_rangers = []
power_rangers.append("Jason")
power_rangers.append("Trini")
power_rangers.append("Zack")
power_rangers.append("Billy")
power_rangers.append("Kimberly")

#print(power_rangers[2])

index = 0

print(len(power_rangers))

# Here is my WHILE loop
# It has a start at index, and finishes at the end of the list
print("------WHILE LOOP------")
while index < len(power_rangers):
    print(power_rangers[index])
    index = index + 1
print("------FOR LOOP------")


# Here is a FOR loop
for ranger in power_rangers:
    print(ranger)


# FOR every SINGLE ITEM, which I am calling "ranger",
# that exists in my COLLECTION OF ITEMS, called "power_rangers" 
# PRINT that SINGLE ITEM'S VALUE
