import csv
import re


def read_csv(file_name):
    with open("phonebook_raw.csv", encoding='windows-1251') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
        return contacts_list


def format_fullname(contacts_list):
    name_pattern = r'^([А-ЯЁа-яё]+)\s*(\,?)([А-ЯЁа-яё]+)\s*(\,?)([А-ЯЁа-яё]*)\s*(\,)?(\,?)(\,?)'
    name_repl = r'\1\2\8\3\4\7\5\6'
    contacts_list_replaced = list()
    for contact in contacts_list:
        contact_string = ','.join(contact)
        # print(contact_string)
        contact_replaced = re.sub(name_pattern, name_repl, contact_string)
        contact_list = contact_replaced.split(',')
        contacts_list_replaced.append(contact_list)
        # print(contact_replaced)
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


def delete_duplicates(contacts_list):
    contacts_list_replaced = list()
    for i in contacts_list:
        for j in contacts_list:
            if (i[0] == j[0] and i[1] == j[1]) and i != j:
                if i[2] == '':
                    i[2] = j[2]
                if i[3] == '':
                    i[3] = j[3]
                if i[4] == '':
                    i[4] = j[4]
                if i[5] == '':
                    i[5] = j[5]
                if i[6] == '':
                    i[6] = j[6]
                if len(i) == 8:
                    i.pop()
        if i not in contacts_list_replaced:
            contacts_list_replaced.append(i)
    return contacts_list_replaced


def write_file(contacts_list):
    with open("phonebook.csv", "w", newline='') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(contacts_list)


contacts_list = read_csv('phonebook_raw.csv')
contacts_list = format_fullname(contacts_list)
contacts_list = format_number(contacts_list)
contacts_list = delete_duplicates(contacts_list)
write_file(contacts_list)
