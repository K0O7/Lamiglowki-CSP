import random
import Constraints
from copy import copy


def backtracking_search(index_x, index_y, field_list, solution_list, inequalities,domein_heur, value_heur, state_checked):
    if not field_list[index_x][index_y].is_set():
        if value_heur:
            random.shuffle(field_list[index_x][index_y].d)
        for i in range(len(field_list[index_x][index_y].d)):
            state_checked += 1
            new_field_list = []

            field_list[index_x][index_y].set(field_list[index_x][index_y].d[i])

            for row in field_list:
                new_row = []

                for obj in row:
                    new_row.append(copy(obj))

                new_field_list.append(new_row)

            if inequalities is None:

                if Constraints.constraint_for_binary(field_list):
                    #wybieranie nowego x i y
                    if domein_heur:
                        if all_set(field_list):
                            solution_list.append(field_list)

                            return solution_list, state_checked
                        x, y = select_next_field(field_list)
                        _, state_checked = backtracking_search(x, y, new_field_list, solution_list, inequalities,domein_heur,value_heur,state_checked)

                    else:
                        if index_x == len(field_list) - 1 and index_y == len(field_list) - 1:
                            solution_list.append(field_list)

                            return solution_list, state_checked

                        if (index_y + 1) % len(field_list) == 0:
                            _, state_checked = backtracking_search(index_x + 1, 0, new_field_list, solution_list, inequalities,domein_heur,value_heur,state_checked)

                        else:
                            _, state_checked = backtracking_search(index_x, index_y + 1, new_field_list, solution_list, inequalities,domein_heur,value_heur,state_checked)

            else:
                if Constraints.constraint_for_futoshiki(field_list, inequalities):

                    # wybieranie nowego x i y
                    if domein_heur:
                        if all_set(field_list):
                            solution_list.append(field_list)

                            return solution_list, state_checked
                        x, y = select_next_field(field_list)
                        _, state_checked = backtracking_search(x, y, new_field_list, solution_list, inequalities,domein_heur,value_heur, state_checked)
                    else:
                        if index_x == len(field_list) - 1 and index_y == len(field_list) - 1:
                            solution_list.append(field_list)

                            return solution_list, state_checked

                        if (index_y + 1) % len(field_list) == 0:
                            _, state_checked = backtracking_search(index_x + 1, 0, new_field_list, solution_list, inequalities,domein_heur,value_heur, state_checked)

                        else:
                            _, state_checked = backtracking_search(index_x, index_y + 1, new_field_list, solution_list, inequalities,domein_heur,value_heur, state_checked)

    else:

        # wybieranie nowego x i y
        if domein_heur:
            if all_set(field_list):
                solution_list.append(field_list)

                return solution_list, state_checked
            x, y = select_next_field(field_list)
            _, state_checked = backtracking_search(x, y, field_list, solution_list, inequalities,domein_heur,value_heur, state_checked)

        else:
            if index_x == len(field_list) - 1 and index_y == len(field_list) - 1:
                solution_list.append(field_list)

                return solution_list, state_checked

            if (index_y + 1) % len(field_list) == 0:
                _, state_checked = backtracking_search(index_x + 1, 0, field_list, solution_list, inequalities,domein_heur,value_heur, state_checked)

            else:
                _, state_checked = backtracking_search(index_x, index_y + 1, field_list, solution_list, inequalities,domein_heur,value_heur, state_checked)

    return solution_list, state_checked


def foreward_looking(index_x, index_y, field_list, solution_list, inequalities, domein_heur, value_heur, state_checked):
    if not field_list[index_x][index_y].is_set():
        # set backup domains
        if value_heur:
            random.shuffle(field_list[index_x][index_y].d)

        for row in field_list:
            for obj in row:
                obj.set_bd()

        for i in range(len(field_list[index_x][index_y].d)):
            state_checked += 1
            new_field_list = []

            field_list[index_x][index_y].set(field_list[index_x][index_y].d[i])

            for row in field_list:
                new_row = []

                for obj in row:
                    new_row.append(copy(obj))

                new_field_list.append(new_row)

            if inequalities is None:

                if Constraints.update_binary_domains(index_x, index_y, field_list):
                    # wybieram nowe x, y
                    if domein_heur:
                        if all_set(field_list):
                            solution_list.append(field_list)

                            return solution_list, state_checked

                        x, y = select_next_field(field_list)
                        _, state_checked = foreward_looking(x, y, new_field_list, solution_list, inequalities,domein_heur,value_heur, state_checked)
                    else:
                        if index_x == len(field_list) - 1 and index_y == len(field_list) - 1:
                            solution_list.append(field_list)

                            return solution_list, state_checked

                        if (index_y + 1) % len(field_list) == 0:
                            _, state_checked = foreward_looking(index_x + 1, 0, new_field_list, solution_list, inequalities, domein_heur, value_heur, state_checked)

                        else:
                            _, state_checked = foreward_looking(index_x, index_y + 1, new_field_list, solution_list, inequalities, domein_heur, value_heur, state_checked)

            else:
                if Constraints.update_futoshiki_domains(index_x, index_y, field_list, inequalities):
                    # wybieram nowe x, y
                    if domein_heur:
                        if all_set(field_list):
                            solution_list.append(field_list)

                            return solution_list, state_checked

                        x, y = select_next_field(field_list)
                        _, state_checked = foreward_looking(x, y, new_field_list, solution_list, inequalities, domein_heur, value_heur, state_checked)
                    else:
                        if index_x == len(field_list) - 1 and index_y == len(field_list) - 1:
                            solution_list.append(field_list)
                            # print(len(solution_list))

                            return solution_list, state_checked

                        if (index_y + 1) % len(field_list) == 0:
                            _, state_checked = foreward_looking(index_x + 1, 0, new_field_list, solution_list, inequalities, domein_heur, value_heur, state_checked)

                        else:
                            _, state_checked = foreward_looking(index_x, index_y + 1, new_field_list, solution_list, inequalities, domein_heur, value_heur, state_checked)

            # restore domains
            for row in field_list:
                for obj in row:
                    obj.restore_domain()

    else:
        if inequalities is None:

            if Constraints.update_binary_domains(index_x, index_y, field_list):
                # wybieram nowe x, y
                if domein_heur:
                    if all_set(field_list):
                        solution_list.append(field_list)

                        return solution_list, state_checked

                    x, y = select_next_field(field_list)
                    _, state_checked = foreward_looking(x, y, field_list, solution_list, inequalities, domein_heur, value_heur, state_checked)
                else:
                    if index_x == len(field_list) - 1 and index_y == len(field_list) - 1:
                        solution_list.append(field_list)
                        # print(len(solution_list))
                        # print(solution_list)
                        return solution_list, state_checked

                    if (index_y + 1) % len(field_list) == 0:
                        _, state_checked = foreward_looking(index_x + 1, 0, field_list, solution_list, inequalities, domein_heur, value_heur, state_checked)

                    else:
                        _, state_checked = foreward_looking(index_x, index_y + 1, field_list, solution_list, inequalities, domein_heur, value_heur, state_checked)

        else:
            if Constraints.update_futoshiki_domains(index_x, index_y, field_list, inequalities):
                # wybieram nowe x, y
                if domein_heur:
                    if all_set(field_list):
                        solution_list.append(field_list)

                        return solution_list, state_checked

                    x, y = select_next_field(field_list)
                    _, state_checked = foreward_looking(x, y, field_list, solution_list, inequalities, domein_heur, value_heur, state_checked)
                else:
                    if index_x == len(field_list) - 1 and index_y == len(field_list) - 1:
                        solution_list.append(field_list)

                        return solution_list, state_checked

                    if (index_y + 1) % len(field_list) == 0:
                        _, state_checked = foreward_looking(index_x + 1, 0, field_list, solution_list, inequalities, domein_heur, value_heur, state_checked)

                    else:
                        _, state_checked = foreward_looking(index_x, index_y + 1, field_list, solution_list, inequalities, domein_heur, value_heur, state_checked)

    return solution_list, state_checked

def select_next_field(field_list):
    position_list = []
    for i in range(len(field_list)):
        for j in range(len(field_list)):
            if not field_list[i][j].is_set():
                position_list.append((i, j, len(field_list[i][j].d)))
    position_list.sort(key=lambda x: x[2])
    # print(position_list)
    return position_list[0][0], position_list[0][1]


def all_set(field_list):
    for i in range(len(field_list)):
        for j in range(len(field_list)):
            if not field_list[i][j].is_set():
                return False
    return True