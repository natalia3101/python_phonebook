def read_phonebook():
    with open('file_name.txt', 'r', encoding = 'utf-8') as file:
        pass

    return None #тут что-то надо написать



def add_contact():
    first_name = input("First name: ")
    family_name = input("Family name: ")
    phone_num = input("Phone number: ")
    file = open('file.txt', 'a')
    file.write(first_name + ' ')
    file.write(family_name + ' ')
    file.write(phone_num + '\n')
    file.close()

def find():
    look_for = input("Enter a key word to look for: ")
    file = open('file.txt', 'r')
    file.close() #тут что-то надо написать


def change_record(): #тут что-то надо написать
    return None

def delete_record():  #тут что-то надо написать
    return None