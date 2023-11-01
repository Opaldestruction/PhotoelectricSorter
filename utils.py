import math


def duplicate_averager(x_list, y_list, material_name, row, saved_mat_name, num_duplicates):
    try:
        i = x_list.index(material_name)
    except ValueError:
        x_list.insert(x_list.__len__(), material_name)
        y_list.insert(y_list.__len__(), row.WF)
        if not (saved_mat_name == ''):
            y_list[x_list.index(saved_mat_name)] /= num_duplicates
            saved_mat_name = ''
            num_duplicates = 1
    else:
        if saved_mat_name == material_name:
            y_list[i] += row.WF
            num_duplicates += 1
        elif saved_mat_name == '':
            saved_mat_name = material_name
        else:
            y_list[x_list.index(saved_mat_name)] /= num_duplicates
            saved_mat_name = ''
            num_duplicates = 1


def duplicate_stderr(x_list, y_list, err_list, material_name, row, saved_mat_name, num_duplicates):
    err = 0
    temp = 0
    try:
        something = 'something'  # i = temp_list.index(material_name)
    except ValueError:
        # temp_list.insert(temp_list.__len__(), material_name)
        if not (saved_mat_name == ''):
            err_list[x_list.index(saved_mat_name)] = math.sqrt(err / num_duplicates)
            saved_mat_name = ''
            num_duplicates = 1
    else:
        if saved_mat_name == material_name:
            temp += row.WF  # xi
            temp -= y_list[x_list.index(material_name)]  # mu
            err += math.pow(temp, 2)
            num_duplicates += 1
        elif saved_mat_name == '':
            saved_mat_name = material_name
        else:
            err_list[x_list.index(saved_mat_name)] = math.sqrt(err / num_duplicates)
            saved_mat_name = ''
            num_duplicates = 1
    print(err_list)
