import view
import model
import os

def run():
    os.system('cls' if os.name == 'nt' else 'clear')
    view.greeting()
    while True:
        view.menu()
        answer = input("Option: ")
        if answer == '1':
            view.show_phonebook()
        elif answer == '2':
            model.add_contact()
        elif answer == '3':
            model.find()
        elif answer == '4':
            model.change_record()
        elif answer == '5':
            model.delete_record()
        elif answer == '6':
            break