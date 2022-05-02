#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    for i in range(len(my_list)):
        if idx < 0:
            return my_list
        elif idx > len(my_list):
            return my_list
        else:
            ls = my_list.copy()
            ls[idx] = element
    return ls
