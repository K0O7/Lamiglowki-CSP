def all_rows_distinct(field_list):
    for i in range(len(field_list)):  # index of row to check
        for j in range(i + 1, len(field_list)):  # range of rows to check against
            counter = 0

            for k in range(len(field_list)):  # element of both rows to compare
                if field_list[i][k].is_set() and field_list[j][k].is_set():
                    if field_list[i][k].c == field_list[j][k].c:
                        counter += 1

            if counter == len(field_list):
                return False

    return True


def all_columns_distinct(field_list):
    for i in range(len(field_list)):  # index of row to check
        for j in range(i + 1, len(field_list)):  # range of rows to check against
            counter = 0

            for k in range(len(field_list)):  # element of both rows to compare

                if field_list[k][i].is_set() and field_list[k][j].is_set():
                    if field_list[k][i].c == field_list[k][j].c:
                        counter += 1

            if counter == len(field_list):
                return False

    return True


def not_three_in_row(field_list):
    for i in range(len(field_list)):
        same_in_row = 0

        are_two_in_row = False

        for j in range(1, len(field_list)):
            if field_list[i][j].is_set() and field_list[i][j - 1].is_set() and field_list[i][j].c == \
                    field_list[i][j - 1].c:
                same_in_row += 1

                if same_in_row >= 2:
                    are_two_in_row = True

            else:
                same_in_row = 0

        if are_two_in_row:
            return False

    for i in range(len(field_list)):
        same_in_col = 0

        are_two_in_col = False

        for j in range(1, len(field_list)):
            if field_list[j - 1][i].is_set() and field_list[j][i].is_set() and field_list[j - 1][i].c == \
                    field_list[j][i].c:
                same_in_col += 1

                if same_in_col >= 2:
                    are_two_in_col = True

            else:
                same_in_col = 0

        if are_two_in_col:
            return False

    return True


def same_num_of_each(field_list):
    for i in range(len(field_list)):
        all_set = True

        number_of_zeros = 0

        number_of_ones = 0

        for j in range(len(field_list)):
            if not field_list[i][j].is_set():
                all_set = False

                break

            else:
                if field_list[i][j].c == 0:
                    number_of_zeros += 1

                else:
                    number_of_ones += 1

        if all_set and number_of_zeros != number_of_ones:
            return False

    for i in range(len(field_list)):
        all_set = True

        number_of_zeros = 0

        number_of_ones = 0

        for j in range(len(field_list)):
            if not field_list[j][i].is_set():
                all_set = False

                break

            else:
                if field_list[j][i].c == 0:
                    number_of_zeros += 1

                else:
                    number_of_ones += 1

        if all_set and number_of_zeros != number_of_ones:
            return False

    return True


def constraint_for_binary(field_list):
    return all_rows_distinct(field_list) and all_columns_distinct(field_list) and not_three_in_row(
        field_list) and same_num_of_each(field_list)


def futoshiki_check_inequalities(field_list, inequalities_list):
    for tuple in inequalities_list:
        if field_list[tuple[0]][tuple[1]].is_set() and field_list[tuple[2]][tuple[3]].is_set():
            if tuple[4] == '>':
                if not field_list[tuple[0]][tuple[1]].c > field_list[tuple[2]][tuple[3]].c:
                    return False

            else:
                if not field_list[tuple[0]][tuple[1]].c < field_list[tuple[2]][tuple[3]].c:
                    return False

    return True


def fields_in_rows_distinct(field_list):
    for i in range(len(field_list)):
        row = []

        for j in range(len(field_list)):
            if field_list[i][j].is_set():
                row.append(field_list[i][j].c)

        if len(set(row)) != len(row):
            return False

    return True


def fields_in_columns_distinct(field_list):
    for i in range(len(field_list)):
        column = []

        for j in range(len(field_list)):
            if field_list[j][i].is_set():
                column.append(field_list[j][i].c)

        if len(set(column)) != len(column):
            return False

    return True


def constraint_for_futoshiki(field_list, inequalities_list):
    return futoshiki_check_inequalities(field_list, inequalities_list) and fields_in_rows_distinct(
        field_list) and fields_in_columns_distinct(field_list)


# ------------------------------------------------------------------------------------------------------------------------


def all_rows_distinct_domain(field_list, x, y):
    if y == len(field_list) - 2 and x - 1 >= 0:
        for r in range(1, x + 1):
            count_same = 0
            for i in range(len(field_list)):
                if field_list[x][i].c == field_list[x - r][i].c and field_list[x][i].is_set() and field_list[x - r][i].is_set():
                    count_same += 1
            if count_same == len(field_list) - 1 and field_list[x - r][y + 1].c in field_list[x][y + 1].d:
                field_list[x][y + 1].d.remove(field_list[x - r][y + 1].c)
            if not field_list[x][y + 1].d:
                return False
    return True


def all_columns_distinct_domain(field_list, x, y):
    if x == len(field_list) - 2 and y - 1 >= 0:
        for r in range(1, y + 1):
            count_same = 0
            for i in range(len(field_list)):
                if field_list[i][y].c == field_list[i][y - r].c and field_list[i][y].is_set() and field_list[i][y - r].is_set():
                    count_same += 1
            if count_same == len(field_list) - 1 and field_list[x + 1][y - r].c in field_list[x + 1][y].d:
                field_list[x + 1][y].d.remove(field_list[x + 1][y - r].c)
            if not field_list[x + 1][y].d:
                return False
    return True


def not_three_in_row_domain(field_list, x, y):
    value = field_list[x][y].c
    if y - 1 >= 0:
        if field_list[x][y - 1].c == value:
            if y + 1 < len(field_list):
                if value in field_list[x][y + 1].d:
                    field_list[x][y + 1].d.remove(value)
                if not field_list[x][y + 1].d:
                    return False
            if y - 2 >= 0:  #
                if value in field_list[x][y - 2].d and not field_list[x][y - 2].is_set():
                    field_list[x][y - 2].d.remove(value)
                if not field_list[x][y - 2].d and not field_list[x][y - 2].is_set():
                    return False

    if y + 2 < len(field_list):
        if field_list[x][y + 2].c == value:
            if value in field_list[x][y + 1].d:
                field_list[x][y + 1].d.remove(value)
            if not field_list[x][y + 1].d:
                return False

    if x - 1 >= 0:
        if field_list[x - 1][y].c == value:
            if x + 1 < len(field_list):
                if value in field_list[x + 1][y].d:
                    field_list[x + 1][y].d.remove(value)
                if not field_list[x + 1][y].d:
                    return False
            if x - 2 >= 0:
                if value in field_list[x - 2][y].d and not field_list[x - 2][y].is_set():
                    field_list[x - 2][y].d.remove(value)
                if not field_list[x - 2][y].d and not field_list[x - 2][y].is_set():
                    return False

    if x + 2 < len(field_list):
        if field_list[x + 2][y].c == value:
            if value in field_list[x + 1][y].d:
                field_list[x + 1][y].d.remove(value)
            if not field_list[x + 1][y].d:
                return False
    return True


def same_num_of_each_domain(field_list, x, y):
    value = field_list[x][y].c
    num_in_col = 0
    num_in_row = 0
    for i in range(len(field_list)):
        if field_list[i][y].c == value:
            num_in_col += 1

        if field_list[x][i].c == value:
            num_in_row += 1

    for i in range(len(field_list)):
        if num_in_col == len(field_list) / 2 and not field_list[i][y].is_set() and value in field_list[i][y].d:
            field_list[i][y].d.remove(value)
            if not field_list[i][y].d:
                return False

        if num_in_row == len(field_list) / 2 and not field_list[x][i].is_set() and value in field_list[x][i].d:
            field_list[x][i].d.remove(value)
            if not field_list[i][y].d:
                return False

    return True


def update_binary_domains(x, y, field_list):
    return all_rows_distinct_domain(field_list, x, y) and all_columns_distinct_domain(field_list, x,
                                                                                      y) and not_three_in_row_domain(
        field_list, x, y) and same_num_of_each_domain(field_list, x, y)


def futoshiki_check_initial_inequalities_domain(field_list, inequalities_list):
    for tuple in inequalities_list:
        if not field_list[tuple[0]][tuple[1]].is_set() and not field_list[tuple[2]][tuple[3]].is_set():
            if tuple[4] == '>':
                field_list[tuple[0]][tuple[1]].remove_min_domain()
                field_list[tuple[2]][tuple[3]].remove_max_domain()
            else:
                field_list[tuple[0]][tuple[1]].remove_max_domain()
                field_list[tuple[2]][tuple[3]].remove_min_domain()


def futoshiki_check_inequalities_domain(field_list, inequalities_list):
    for tuple in inequalities_list:
        if field_list[tuple[0]][tuple[1]].is_set() and not field_list[tuple[2]][tuple[3]].is_set():
            value = field_list[tuple[0]][tuple[1]].c
            if tuple[4] == '>':
                field_list[tuple[2]][tuple[3]].remove_greater_then(value)
            else:
                field_list[tuple[2]][tuple[3]].remove_lower_then(value)

            if not field_list[tuple[2]][tuple[3]].d:
                return False

        if not field_list[tuple[0]][tuple[1]].is_set() and field_list[tuple[2]][tuple[3]].is_set():
            value = field_list[tuple[2]][tuple[3]].c
            if tuple[4] == '>':
                field_list[tuple[0]][tuple[1]].remove_lower_then(value)
            else:
                field_list[tuple[0]][tuple[1]].remove_greater_then(value)

            if not field_list[tuple[0]][tuple[1]].d:
                return False
    return True


def fields_in_rows_distinct_domain(field_list, x, y):
    value = field_list[x][y].c
    for i in range(len(field_list)):
        if not field_list[x][i].is_set():
            if value in field_list[x][i].d:
                field_list[x][i].d.remove(value)
            if not field_list[x][i].d:
                return False
    return True


def fields_in_columns_distinct_domain(field_list, x, y):
    value = field_list[x][y].c
    for i in range(len(field_list)):
        if not field_list[i][y].is_set():
            if value in field_list[i][y].d:
                field_list[i][y].d.remove(value)
            if not field_list[i][y].d:
                return False
    return True


def update_futoshiki_domains(x, y, field_list, inequalities_list):
    return futoshiki_check_inequalities_domain(field_list, inequalities_list) \
           and fields_in_rows_distinct_domain(field_list, x, y) \
           and fields_in_columns_distinct_domain(field_list, x, y)


def update_futoshiki_domains_initial(field_list, inequalities_list):
    futoshiki_check_initial_inequalities_domain(field_list, inequalities_list)
    for i in range(len(field_list)):
        for j in range(len(field_list)):
            fields_in_rows_distinct_domain(field_list, i, j)
            fields_in_columns_distinct_domain(field_list, i, j)
