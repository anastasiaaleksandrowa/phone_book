# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных

#функция для добавления, измения и удаления контакта
phone_book = {}
def add_contact (last_name, first_name, middle_name, phone_number):
    contact_id= len(phone_book)+1
    phone_book[contact_id]={'last_name': last_name, 'first_name': first_name, 'middle_name': middle_name, 'phone_number': phone_number}
def update_contact (contact_id, last_name, first_name, middle_name, phone_number):
    if contact_id in phone_book:
        phone_book[contact_id]= {'last_name': last_name, 'first_name': first_name, 'middle_name': middle_name, 'phone_number': phone_number}
    else:
        print("контакт не найден")
def delete_contact(contact_id):
    if contact_id in phone_book:
        del phone_book[contact_id]
    else:
         print("контакт не найден")
# функция поиска контакта по имени 
def search_contact(search_key):
    for contact_id, contact_info in phone_book.items():
        if search_key.lower() in contact_info ['last_name'].lower() or search_key.lower() in contact_info ['first_name'].lower():
            print (f"ID: {contact_id}")
            print (f"Фамилия: {contact_info['last_name']}")
            print (f"имя: {contact_info['first_name']}")
            print (f"отчество: {contact_info['middle_name']}")
            print (f"номер телефона: {contact_info['phone_number']}")