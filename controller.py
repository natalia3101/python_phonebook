import view
import model

def run():
    view.greeting()
    while True:
        view.menu()
        answer = input("Answer: ")
        if answer == '1':
            date = model.read_phonebook()
            view.show_phonebook(date)
        elif answer == '2':
            model.add_contact()
        elif answer == '3':
            model.find()
        elif answer == '4':
            break