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


def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    pass


if __name__ == '__main__':
    main()