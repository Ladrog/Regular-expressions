import csv


from formatting import join_name, add_new_data_contacts, formatting_phones, group_fio

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


if __name__ == "__main__":
    fio_data = join_name(contacts_list)
    new_contacts_list = add_new_data_contacts(contacts_list, fio_data)
    contacts = formatting_phones(new_contacts_list)


    with open("phonebook.csv", "w", encoding="utf-8") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(group_fio(contacts))
