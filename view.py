from tabulate import tabulate

def greeting():
    print("Welcome to our app!")

def menu():
    print("The phonebook\n********************\n**Choose an option**\n 1. Open the phonebook\n 2. Add a record\n 3. Search\n 4. Change a record\n 5. Delete a record\n 6. Close the program\n")



def show_phonebook(data):
    if data:
        print(
            tabulate(
            data,
            headers = 'keys'
            ),
            ende = '\n\n'
        )
    else:
        raise ValueError("The phone book is empty or does not exist") #что-то не работает