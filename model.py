def read_phonebook():
    file = open('file.txt', 'r', encoding = 'utf-8')
    lines = file.readlines()
    book = []
    for line in lines:
        book.append(line)
    file.close()
    return book  




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
    look_for = input("Enter a key word: ").lower()
    lines = read_phonebook()
    count = 0
    for line in lines:
        if look_for in line.lower():
            count += 1
            print(line)
            break
    else:
        print("The record is not found")


# Я не понимаю, почему функция не работает. Мне выдает ошибку "replace() argument 2 must be str, not None"
def change_record():
    to_change = input("Enter a name or number to change: ").lower()
    lines = read_phonebook()
    file = open('file.txt', 'w', encoding='utf-8')
    for i in range(len(lines)):
        if to_change in lines[i].lower():
            lines[i] = lines[i].replace(to_change, add_contact())
            file.write(lines[i])
        else:
            file.write(lines[i])
    file.close()



#Я пытаюсь удалить контакт, но у меня эта функция не работает
def delete_record():
    look_for = input("Enter a key word: ").lower()
    lines = read_phonebook()
    file = open('file.txt', 'w', encoding='utf-8')
    for line in lines:
        if look_for not in line:
            file.write(line)
    file.close()

