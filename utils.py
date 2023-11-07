import copy
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


# TODO: I haven't finished this yet, I'm hoping to, as I think it could give as good an insight as the WF itself.
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


# If you have any optimizations for my "multiple_sort" feel free to add them below.
def multiple_sort(list_1, list_of_lists):
    for list_i in list_of_lists:
        if not list_i.__len__() == list_1.__len__():
            print("you stup*d. can't sort lists with different lengths. dum*a**")
            return
        # Find the maximum number to know number of digits

    # forgot floats existed, casting to integers
    for i in range(0, len(list_1)):
        list_1[i] = int(list_1[i] * 100)
    max1 = max(list_1)

    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number

    # The output array elements that will have sorted arr
    output = copy.deepcopy(list_of_lists)

    for i in range(0, len(output)):
        for j in range(0, len(output[i])):
            output[i][j] = 0

    exp = 1
    while max1 / exp >= 1:
        n = len(list_1)

        # initialize count array as 0
        count = [0] * 10

        # Store count of occurrences in count[]
        for i in range(0, n):
            index = list_1[i] // exp
            count[index % 10] += 1

        # Change count[i] so that count[i] now contains actual
        # position of this digit in output array
        for i in range(1, 10):
            count[i] += count[i - 1]

        # Build the output array

        i = n - 1
        while i >= 0:
            for j in range(0, len(list_of_lists)):
                index = list_1[i] // exp
                output[j][count[index % 10] - 1] = list_of_lists[j][i]
            count[index % 10] -= 1
            i -= 1

        # Copying the output array to arr[],
        # so that arr now contains sorted numbers
        i = 0
        for i in range(0, len(list_1)):
            for j in range(0, len(list_of_lists)):
                list_of_lists[j][i] = output[j][i]
        exp *= 10

    # un-100ify them
    for i in range(0, len(list_1)):
        list_1[i] = float(list_1[i]) / 100

    # This code is contributed by Mohit Kumra
    # Edited by Patrick Gallagher
    # And then altered to make multiple_sort work by Xavier Burt
