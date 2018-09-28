# coding: utf-8
import csv
from collections import OrderedDict

file_output = 'sorted.csv'  # file two write sorted messages to
file_input = 'unsorted.csv'  # file to read messages from
fields = ['local_ID','Description','en_US','ru_RU','es_ES','pt_BR','fr_FR','ar_AR','he_IL','id_ID','tr_TR','th_TH','it_IT','de_DE','ja_JP','ko_KR','nl_NL','vi_VN','pl_PL','uk_UA']
strings_list = []
combined_list = []
dict_reader = csv.DictReader(open(file_input), dialect='excel-tab')
id_list = []



def remove_empty_keys(input_dict, keys_list):
    for x in keys_list:
        if input_dict[x] == '':
            input_dict.pop(x)


def read_all_rows(reader, full_list):
    for row in reader:
        remove_empty_keys(row, fields)
        full_list.append(dict(row))
        #print(dict(row))


def write_indexes(full_list, indexes_list):
    for row in full_list:
        indexes_list.append(row['local_ID'])


def indices(lst, element):
    result = []
    offset = -1
    while True:
        try:
            offset = lst.index(element, offset+1)
        except ValueError:
            return result
        result.append(offset)


read_all_rows(dict_reader, strings_list)
write_indexes(strings_list, id_list)



counter = 0
for index in id_list:
    duplicates = indices(id_list, index)
    #print(duplicates)
    merged = {**strings_list[duplicates[0]]}
    #print(merged)
    for x in duplicates:
        merged = {**merged, **strings_list[duplicates[counter]]}
        #print(merged)
        counter = counter + 1
    combined_list.append(merged)
    counter = 0


def write_to_csv(str_lst, output, dlct='excel-tab'):
    with open(output, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields, dialect=dlct)
        writer.writeheader()
        writer.writerows(str_lst)

write_to_csv(combined_list, file_output)