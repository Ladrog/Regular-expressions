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


merged_data = {}
def group_fio(contacts: list):
    for item in contacts:
        key = (item[0], item[1])
        if key not in merged_data:
            merged_data[key] = item
        else:
            merged_item = [merged_data[key][0], merged_data[key][1]]
            for i in range(2, len(item)):
                merged_item.append(item[i] if item[i] else merged_data[key][i])
            merged_data[key] = merged_item

    final_data = list(merged_data.values())
    return final_data
