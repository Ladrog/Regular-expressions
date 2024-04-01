import re


def join_name(contacts_list: list):
    fio = []
    for contact in contacts_list[1:]:
        full_name = " ".join(contact[0:3])
        result = full_name.split(' ')
        while len(result) != 3:
            result.remove('')
        fio.append(result)
    return fio


def add_new_data_contacts(contacts: list, fio_list: list):
    new_contacts = []
    for contact, fio_parts in zip(contacts[1:], fio_list):
        del contact[0:3]
        for fio_part in reversed(fio_parts):
            contact.insert(0, fio_part)
        new_contacts.append(contact)
    new_contacts.insert(0, contacts[0])
    return new_contacts


def formatting_phones(contact_list: list):
    pattern = r"\+?(\d{1})\s?\(?(\d{3})\)?[-\s]?(\d{3})[-\s]?(\d{2})[-\s]?(\d{2})\s?(\(?(доб.)\s(\d+)\)?)?"
    format_str = "+7(\\2)\\3-\\4-\\5 \\7\\8"
    for row in contact_list[1:]:
        if len(row) <= 5:
            continue
        phone_number = row[5]
        formatted_phone_number = re.sub(pattern, format_str, phone_number)
        row[5] = formatted_phone_number
    return contact_list


def group_fio(contacts: list):
    grouped_data = {}
    for item in contacts[1:]:
        key = (item[0], item[1])
        if key not in grouped_data:
            grouped_data[key] = item[2:]
        # else:
        #     for el in item[2:]:
        #         if el not in grouped_data[key]:
        #             grouped_data[key].append(el)
    contact_list = [list(key) + value for key, value in grouped_data.items()]
    contact_list.insert(0, contacts[0])
    return contact_list
