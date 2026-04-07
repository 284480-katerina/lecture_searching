import os
import json
# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    with open(file_name, "r") as file_obj:
        data = json.load(file_obj)
    file_path = os.path.join(cwd_path, file_name)

    if field not in data:
        return None

    return data[field]

def linear_search(sequence, number):
    positions = []
    count = 0

    for i in range(len(sequence)):
        if sequence[i] == number:
            positions.append(i)
            count += 1

    return {
        "positions": positions,
        "count": count
    }

def binary_search(number_list, number):

    leva = 0
    prava = len(number_list) - 1

    while leva <= prava:

        prostredek = (leva + prava) // 2

        if number_list[prostredek] == number:
            return prostredek
        elif number_list[prostredek] < number:
            leva = prostredek + 1
        else:
            prava = prostredek - 1

    return None




def main():
    sequential_data = read_data("sequential.json", "ordered_numbers")
    print(sequential_data)

    number = 14

    linear_function = linear_search(sequential_data, number)
    print(linear_function)

    result = binary_search(sequential_data, number)
    print(result)



if __name__ == '__main__':
    main()