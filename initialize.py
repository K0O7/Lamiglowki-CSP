from copy import copy

import field


def prepare_field_list(domain, size, starting_condition):
    field_list = []

    for i in range(size):
        field_row = []

        for j in range(size):
            if starting_condition[i*size+j] == 'x':
                temp_field = field.Field(copy(domain))

            else:
                temp_field = field.Field(copy(domain), int(starting_condition[i*size+j]))

            field_row.append(temp_field)

        field_list.append(field_row)

    return field_list


def read_from_file(file_name):
    starting_state = []

    with open(file_name, 'r') as file:
        for line in file:
            starting_state.append(line.strip())

    return starting_state


def parse_starting_state(starting_state):
    new_starting_state = []

    for line in starting_state:
        for i in range(len(line)):
            new_starting_state.append(line[i])

    return new_starting_state


def parse_inequalities(starting_state, size):
    new_starting_state = []

    inequalities = []

    row_index = 0

    row = 0

    for line in starting_state:

        if row_index % 2 == 0:
            column = 0

            for column_index in range((size * 2) - 1):
                if column_index % 2 == 0:
                    new_starting_state.append(line[column_index])

                else:
                    if line[column_index] != '-':
                        inequalities.append((row, column, row, column + 1, line[column_index]))

                    column += 1

            row += 1

        else:
            for column in range(size):
                if line[column] != '-':
                    inequalities.append((row - 1, column, row, column, line[column]))

        row_index += 1

    return inequalities, new_starting_state
