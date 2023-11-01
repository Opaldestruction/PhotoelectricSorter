def duplicate_averager(x_list, y_list, material_name, row):
    saved_mat_name = ''
    num_duplicates = 1
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
