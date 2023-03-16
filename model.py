def read_phonebook():
    file = open('file.txt', 'r', encoding = 'utf-8')
    lines = file.readlines()
    mat_line = []
    for line in lines:
        mat_line.append(line)
    file.close()
    return mat_line


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
    look_for = input("Enter a key word: ")
    lines = read_phonebook()
    for line in lines:
        if look_for in line:
            print(line)
        else:
            print("The record is not found") #почему выводит The record is not found даже если запись найдена?


def change_record(): #тут что-то надо написать
    return None

def delete_record():  #тут что-то надо написать
    return None