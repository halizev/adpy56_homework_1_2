import csv
import re


def read_csv(file_name):
    with open("phonebook_raw.csv", encoding='windows-1251') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
        return contacts_list


def format_fullname(contacts_list):
    name_pattern = r'^([А-ЯЁа-яё]+)(\s*)(\,?)([А-ЯЁа-яё]+)(\s*)(\,?)([А-ЯЁа-яё]*)'
    name_repl = r'\1,\4,\7'
    contacts_list_replaced = list()
    for contact in contacts_list:
        contact_string = ','.join(contact)
        contact_replaced = re.sub(name_pattern, name_repl, contact_string)
        contact_list = contact_replaced.split(',')
        contacts_list_replaced.append(contact_list)
        print(contact)
        print(contact_list)
    return contacts_list_replaced


def format_number(contacts_list):
    number_pattern = r'(\+7|8)\s*\(*(\d{3})\)*\s*\-*(\d{3})\s*\-*(\d{2})\s*\-*(\d{2}\s*)\(*(доб*\.)*\s*(\d+)*\)*'
    number_repl = r'+7(\2)\3-\4-\5\6\7'
    contacts_list_replaced = list()
    for contact in contacts_list:
        contact_string = ','.join(contact)
        contact_replaced = re.sub(number_pattern, number_repl, contact_string)
        contact_list = contact_replaced.split(',')
        contacts_list_replaced.append(contact_list)

    return contacts_list_replaced


def write_file(contacts_list):
    with open("phonebook.csv", "w", newline='') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(contacts_list)


contacts_list = read_csv('phonebook_raw.csv')
contacts_list = format_fullname(contacts_list)
contacts_list = format_number(contacts_list)

write_file(contacts_list)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
