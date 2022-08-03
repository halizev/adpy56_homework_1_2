import csv
import re

with open("phonebook_raw.csv", encoding='windows-1251') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

# TODO 1: выполните пункты 1-3 ДЗ
    # Преобразовать ФИО
for contact in contacts_list:
    i = 1
    for contact_part in contact[1:2]:
        if contact_part != '':
            contact[0] += ' ' + contact_part
            contact[i] = ''
            i += 1
    contact[0:2] = contact[0].split(' ')
    print(contact)
    # Преобразовать номер
    # Уточнить добавочный
    # Найти дубли

pattern = re.compile("кекw")

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(contacts_list)