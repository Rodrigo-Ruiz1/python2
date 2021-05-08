meal = {
    "entree": "pesto chicken",
    "drink": "fizzy water",
    "dessert": "ice cream"
}

#print(meal["dessert"]);
#print("Tonight I will have %s for dinner, with %s for dessert" % (meal["entree"], meal["dessert"]))

# If the key "dessert" is found in the dictionary meal
# THEN, print the first statement
# If NOT, THEN print the second statement
#if "dessert" in meal:
#    print("Of COURSE Sean had dessert!! He had %s." % (meal['dessert']))
#else:
#    print("Sean did NOT have dessert, and now he is sad.")

print(meal)
#add a NEW key called "appetizer", with the value "bacon"
meal["appetizer"] = "bacon"
# Update the key "drink", with the value "sweet tea"
meal["drink"] = "sweet tea"
#Delete an entry by referencing its key
del meal["dessert"]
print(meal)