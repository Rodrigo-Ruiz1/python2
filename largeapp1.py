# create Dictionary
phonebook = {
    "Melissa": "584-394-5857",
    "Alice": "703-493-1834",
    "Bob": "857-384-1234",
}

# Loop will continue until user chooses to quit
while True:

# Show user the prompts
    print("Electronic Phone Book\n===========\n1. Look up an entry\n2. Set an entry\n3. Delete an entry\n4. List all entries\n5. Quit\n===========")

    user_input = int(input())
 

    # Executing correct prompt
    if user_input == 1:
        phonebook_name = input("What is the name you would like to look up? ")
        if phonebook_name in phonebook:
            print("Found entry for " + phonebook_name + ": " + phonebook[phonebook_name])
        else:
            print("That name does not exist in the phonebook")
    elif user_input == 2:
        phonebook_new_entry = input("What is the new entry name? ")
        phonebook_new_number = input("What is the new phone number? ")
        phonebook[phonebook_new_entry] = phonebook_new_number
        print("Entry was added")
    elif user_input ==3:
        delete_entry = input("What is the name you would like to remove? ")
        if delete_entry in phonebook:
            del phonebook[delete_entry]
            print("%s was removed from the phonebook" % (delete_entry))
        else:
            print("That name does not exist in the phonebook")
    elif user_input == 4:
        print(phonebook)
    elif user_input == 5:
        quit()
    else:
        print("Please enter a valid number")
    