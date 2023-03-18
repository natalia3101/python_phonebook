def greeting():
    print("Welcome to our phonebook!")

def menu():
    print("The phonebook\n********************\n**Choose an option**\n 1. Open the phonebook\n 2. Add a record\n 3. Search\n 4. Change a record\n 5. Delete a record\n 6. Close the program\n")

    
def show_phonebook():
    file = open('file.txt', 'r')
    print('\n********************\n')
    for line in file:
        print(line)
    file.close
    print('\n********************\n')

