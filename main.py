import time
import matplotlib.pyplot as pyl
import Constraints
# import field
import initialize
import solving


def start_searching(file_name, is_binary=True, is_backtracing = True, choose_field_by_domain = False, choose_random_val = False):
    starting_state = initialize.read_from_file(file_name)

    # print("initial state: ")
    #
    # for line in starting_state:
    #     print(line)
    #
    # print()

    if is_binary:
        domain = [0, 1]

        size = int(len(starting_state))

        starting_state = initialize.parse_starting_state(starting_state)

        inequalities = None

    else:
        size = int(len(starting_state) / 2) + 1

        domain = list(range(1, size + 1))

        inequalities, starting_state = initialize.parse_inequalities(starting_state, size)

    field_list = initialize.prepare_field_list(domain, size, starting_state)

    state_checked = 0

    start_time = time.time()
    if is_backtracing:
        all_solutions, state_checked = solving.backtracking_search(0, 0, field_list, [], inequalities, choose_field_by_domain, choose_random_val, state_checked)
    else:
        if is_binary:
            for i in range(len(field_list)):
                for j in range(len(field_list)):
                    Constraints.update_binary_domains(i, j, field_list)
        else:
            Constraints.update_futoshiki_domains_initial(field_list, inequalities)

        all_solutions, state_checked = solving.foreward_looking(0, 0, field_list, [], inequalities, choose_field_by_domain, choose_random_val, state_checked)
    total_time = time.time() - start_time
    # print("time of execution: " + str(total_time))
    # print("checked nodes: "+str(state_checked))
    # print("number of solutions: " + str(len(all_solutions)))
    return total_time, state_checked
    # print("solutions")
    #
    # for solution in all_solutions:
    #     for line in solution:
    #         print(line)
    #
    #     print()


if __name__ == '__main__':
    # print("binary_6x6")
    # start_searching("binary_6x6", is_binary=True, is_backtracing = True, choose_field_by_domain = False, choose_random_val = False)
    #
    # print("\nbinary_8x8")
    # start_searching("binary_8x8", choose_field_by_domain=False, choose_random_val=False)
    # #
    # print("\nbinary_10x10")
    # start_searching("binary_10x10", is_backtracing=True, choose_field_by_domain=True, choose_random_val=True)
    # #
    # print("\nfutoshiki_4x4")
    # start_searching("futoshiki_4x4", False, is_backtracing=True, choose_field_by_domain=True, choose_random_val=True)
    # #
    # print("\nfutoshiki_5x5")
    # start_searching("futoshiki_5x5", False,True,True)
    # #
    # print("\nfutoshiki_6x6")
    # start_searching("futoshiki_6x6", False, is_backtracing=False, choose_field_by_domain=True, choose_random_val=True)

    bin_6x6_time_true_false_false = []
    bin_6x6_checkd_true_false_false = []
    bin_8x8_time_true_false_false = []
    bin_8x8_checkd_true_false_false = []
    bin_10x10_time_true_false_false = []
    bin_10x10_checkd_true_false_false = []
    fuk_4x4_time_true_false_false = []
    fuk_4x4_checkd_true_false_false = []
    fuk_5x5_time_true_false_false = []
    fuk_5x5_checkd_true_false_false = []
    fuk_6x6_time_true_false_false = []
    fuk_6x6_checkd_true_false_false = []

    bin_6x6_time_true_false_true = []
    bin_6x6_checkd_true_false_true = []
    bin_8x8_time_true_false_true = []
    bin_8x8_checkd_true_false_true = []
    bin_10x10_time_true_false_true = []
    bin_10x10_checkd_true_false_true = []
    fuk_4x4_time_true_false_true = []
    fuk_4x4_checkd_true_false_true = []
    fuk_5x5_time_true_false_true = []
    fuk_5x5_checkd_true_false_true = []
    fuk_6x6_time_true_false_true = []
    fuk_6x6_checkd_true_false_true = []

    bin_6x6_time_true_true_false = []
    bin_6x6_checkd_true_true_false = []
    bin_8x8_time_true_true_false = []
    bin_8x8_checkd_true_true_false = []
    bin_10x10_time_true_true_false = []
    bin_10x10_checkd_true_true_false = []
    fuk_4x4_time_true_true_false = []
    fuk_4x4_checkd_true_true_false = []
    fuk_5x5_time_true_true_false = []
    fuk_5x5_checkd_true_true_false = []
    fuk_6x6_time_true_true_false = []
    fuk_6x6_checkd_true_true_false = []

    bin_6x6_time_true_true_true = []
    bin_6x6_checkd_true_true_true = []
    bin_8x8_time_true_true_true = []
    bin_8x8_checkd_true_true_true = []
    bin_10x10_time_true_true_true = []
    bin_10x10_checkd_true_true_true = []
    fuk_4x4_time_true_true_true = []
    fuk_4x4_checkd_true_true_true = []
    fuk_5x5_time_true_true_true = []
    fuk_5x5_checkd_true_true_true = []
    fuk_6x6_time_true_true_true = []
    fuk_6x6_checkd_true_true_true = []

    bin_6x6_time_false_false_false = []
    bin_6x6_checkd_false_false_false = []
    bin_8x8_time_false_false_false = []
    bin_8x8_checkd_false_false_false = []
    bin_10x10_time_false_false_false = []
    bin_10x10_checkd_false_false_false = []
    fuk_4x4_time_false_false_false = []
    fuk_4x4_checkd_false_false_false = []
    fuk_5x5_time_false_false_false = []
    fuk_5x5_checkd_false_false_false = []
    fuk_6x6_time_false_false_false = []
    fuk_6x6_checkd_false_false_false = []

    bin_6x6_time_false_false_true = []
    bin_6x6_checkd_false_false_true = []
    bin_8x8_time_false_false_true = []
    bin_8x8_checkd_false_false_true = []
    bin_10x10_time_false_false_true = []
    bin_10x10_checkd_false_false_true = []
    fuk_4x4_time_false_false_true = []
    fuk_4x4_checkd_false_false_true = []
    fuk_5x5_time_false_false_true = []
    fuk_5x5_checkd_false_false_true = []
    fuk_6x6_time_false_false_true = []
    fuk_6x6_checkd_false_false_true = []

    bin_6x6_time_false_true_false = []
    bin_6x6_checkd_false_true_false = []
    bin_8x8_time_false_true_false = []
    bin_8x8_checkd_false_true_false = []
    bin_10x10_time_false_true_false = []
    bin_10x10_checkd_false_true_false = []
    fuk_4x4_time_false_true_false = []
    fuk_4x4_checkd_false_true_false = []
    fuk_5x5_time_false_true_false = []
    fuk_5x5_checkd_false_true_false = []
    fuk_6x6_time_false_true_false = []
    fuk_6x6_checkd_false_true_false = []

    bin_6x6_time_false_true_true = []
    bin_6x6_checkd_false_true_true = []
    bin_8x8_time_false_true_true = []
    bin_8x8_checkd_false_true_true = []
    bin_10x10_time_false_true_true = []
    bin_10x10_checkd_false_true_true = []
    fuk_4x4_time_false_true_true = []
    fuk_4x4_checkd_false_true_true = []
    fuk_5x5_time_false_true_true = []
    fuk_5x5_checkd_false_true_true = []
    fuk_6x6_time_false_true_true = []
    fuk_6x6_checkd_false_true_true = []

    is_bt = True
    for _ in range(2): # is backtracking
        is_var_heu = False
        for _ in range(2): # var heuristic
            is_val_heu = False
            for _ in range(2): # val heuristic

                bin_6x6_time = []
                bin_6x6_checkd = []
                bin_8x8_time = []
                bin_8x8_checkd = []
                bin_10x10_time = []
                bin_10x10_checkd = []
                fuk_4x4_time = []
                fuk_4x4_checkd = []
                fuk_5x5_time = []
                fuk_5x5_checkd = []
                fuk_6x6_time = []
                fuk_6x6_checkd = []

                print("testing: \tbacktracing: "+str(is_bt) +"\tvariable heuristic: "+str(is_var_heu)+"\tvalue heuristic: "+str(is_val_heu))
                for _ in range(2): #ilość testów dla jednego ustawienia
                    temp_time = 0
                    temp_states = 0

                    temp_time, temp_states = start_searching("binary_6x6", is_binary=True, is_backtracing=is_bt, choose_field_by_domain=is_var_heu, choose_random_val=is_val_heu)
                    bin_6x6_time.append(temp_time)
                    bin_6x6_checkd.append(temp_states)

                    temp_time, temp_states =start_searching("binary_8x8", is_binary=True, is_backtracing=is_bt, choose_field_by_domain=is_var_heu, choose_random_val=is_val_heu)
                    bin_8x8_time.append(temp_time)
                    bin_8x8_checkd.append(temp_states)

                    temp_time, temp_states =start_searching("binary_10x10", is_binary=True, is_backtracing=is_bt, choose_field_by_domain=is_var_heu, choose_random_val=is_val_heu)
                    bin_10x10_time.append(temp_time)
                    bin_10x10_checkd.append(temp_states)

                    temp_time, temp_states =start_searching("futoshiki_4x4", is_binary=False, is_backtracing=is_bt, choose_field_by_domain=is_var_heu, choose_random_val=is_val_heu)
                    fuk_4x4_time.append(temp_time)
                    fuk_4x4_checkd.append(temp_states)

                    temp_time, temp_states =start_searching("futoshiki_5x5", is_binary=False, is_backtracing=is_bt, choose_field_by_domain=is_var_heu, choose_random_val=is_val_heu)
                    fuk_5x5_time.append(temp_time)
                    fuk_5x5_checkd.append(temp_states)

                    temp_time, temp_states =start_searching("futoshiki_6x6", is_binary=False, is_backtracing=is_bt, choose_field_by_domain=is_var_heu, choose_random_val=is_val_heu)
                    fuk_6x6_time.append(temp_time)
                    fuk_6x6_checkd.append(temp_states)
                if is_bt and not is_var_heu and not is_val_heu:
                    bin_6x6_time_true_false_false = bin_6x6_time
                    bin_6x6_checkd_true_false_false = bin_6x6_checkd
                    bin_8x8_time_true_false_false = bin_8x8_time
                    bin_8x8_checkd_true_false_false = bin_8x8_checkd
                    bin_10x10_time_true_false_false = bin_10x10_time
                    bin_10x10_checkd_true_false_false = bin_10x10_checkd
                    fuk_4x4_time_true_false_false = fuk_4x4_time
                    fuk_4x4_checkd_true_false_false = fuk_4x4_checkd
                    fuk_5x5_time_true_false_false = fuk_5x5_time
                    fuk_5x5_checkd_true_false_false = fuk_5x5_checkd
                    fuk_6x6_time_true_false_false = fuk_6x6_time
                    fuk_6x6_checkd_true_false_false = fuk_6x6_checkd

                if is_bt and not is_var_heu and is_val_heu:
                    bin_6x6_time_true_false_true = bin_6x6_time
                    bin_6x6_checkd_true_false_true = bin_6x6_checkd
                    bin_8x8_time_true_false_true = bin_8x8_time
                    bin_8x8_checkd_true_false_true = bin_8x8_checkd
                    bin_10x10_time_true_false_true = bin_10x10_time
                    bin_10x10_checkd_true_false_true = bin_10x10_checkd
                    fuk_4x4_time_true_false_true = fuk_4x4_time
                    fuk_4x4_checkd_true_false_true = fuk_4x4_checkd
                    fuk_5x5_time_true_false_true = fuk_5x5_time
                    fuk_5x5_checkd_true_false_true = fuk_5x5_checkd
                    fuk_6x6_time_true_false_true = fuk_6x6_time
                    fuk_6x6_checkd_true_false_true = fuk_6x6_checkd

                if is_bt and is_var_heu and not is_val_heu:
                    bin_6x6_time_true_true_false = bin_6x6_time
                    bin_6x6_checkd_true_true_false = bin_6x6_checkd
                    bin_8x8_time_true_true_false = bin_8x8_time
                    bin_8x8_checkd_true_true_false = bin_8x8_checkd
                    bin_10x10_time_true_true_false = bin_10x10_time
                    bin_10x10_checkd_true_true_false = bin_10x10_checkd
                    fuk_4x4_time_true_true_false = fuk_4x4_time
                    fuk_4x4_checkd_true_true_false = fuk_4x4_checkd
                    fuk_5x5_time_true_true_false = fuk_5x5_time
                    fuk_5x5_checkd_true_true_false = fuk_5x5_checkd
                    fuk_6x6_time_true_true_false = fuk_6x6_time
                    fuk_6x6_checkd_true_true_false = fuk_6x6_checkd

                if is_bt and is_var_heu and is_val_heu:
                    bin_6x6_time_true_true_true = bin_6x6_time
                    bin_6x6_checkd_true_true_true = bin_6x6_checkd
                    bin_8x8_time_true_true_true = bin_8x8_time
                    bin_8x8_checkd_true_true_true = bin_8x8_checkd
                    bin_10x10_time_true_true_true = bin_10x10_time
                    bin_10x10_checkd_true_true_true = bin_10x10_checkd
                    fuk_4x4_time_true_true_true = fuk_4x4_time
                    fuk_4x4_checkd_true_true_true = fuk_4x4_checkd
                    fuk_5x5_time_true_true_true = fuk_5x5_time
                    fuk_5x5_checkd_true_true_true = fuk_5x5_checkd
                    fuk_6x6_time_true_true_true = fuk_6x6_time
                    fuk_6x6_checkd_true_true_true = fuk_6x6_checkd

                if not is_bt and not is_var_heu and not is_val_heu:
                    bin_6x6_time_false_false_false = bin_6x6_time
                    bin_6x6_checkd_false_false_false = bin_6x6_checkd
                    bin_8x8_time_false_false_false = bin_8x8_time
                    bin_8x8_checkd_false_false_false = bin_8x8_checkd
                    bin_10x10_time_false_false_false = bin_10x10_time
                    bin_10x10_checkd_false_false_false = bin_10x10_checkd
                    fuk_4x4_time_false_false_false = fuk_4x4_time
                    fuk_4x4_checkd_false_false_false = fuk_4x4_checkd
                    fuk_5x5_time_false_false_false = fuk_5x5_time
                    fuk_5x5_checkd_false_false_false = fuk_5x5_checkd
                    fuk_6x6_time_false_false_false = fuk_6x6_time
                    fuk_6x6_checkd_false_false_false = fuk_6x6_checkd

                if not is_bt and not is_var_heu and is_val_heu:
                    bin_6x6_time_false_false_true = bin_6x6_time
                    bin_6x6_checkd_false_false_true = bin_6x6_checkd
                    bin_8x8_time_false_false_true = bin_8x8_time
                    bin_8x8_checkd_false_false_true = bin_8x8_checkd
                    bin_10x10_time_false_false_true = bin_10x10_time
                    bin_10x10_checkd_false_false_true = bin_10x10_checkd
                    fuk_4x4_time_false_false_true = fuk_4x4_time
                    fuk_4x4_checkd_false_false_true = fuk_4x4_checkd
                    fuk_5x5_time_false_false_true = fuk_5x5_time
                    fuk_5x5_checkd_false_false_true = fuk_5x5_checkd
                    fuk_6x6_time_false_false_true = fuk_6x6_time
                    fuk_6x6_checkd_false_false_true = fuk_6x6_checkd

                if not is_bt and is_var_heu and not is_val_heu:
                    bin_6x6_time_false_true_false = bin_6x6_time
                    bin_6x6_checkd_false_true_false = bin_6x6_checkd
                    bin_8x8_time_false_true_false = bin_8x8_time
                    bin_8x8_checkd_false_true_false = bin_8x8_checkd
                    bin_10x10_time_false_true_false = bin_10x10_time
                    bin_10x10_checkd_false_true_false = bin_10x10_checkd
                    fuk_4x4_time_false_true_false = fuk_4x4_time
                    fuk_4x4_checkd_false_true_false = fuk_4x4_checkd
                    fuk_5x5_time_false_true_false = fuk_5x5_time
                    fuk_5x5_checkd_false_true_false = fuk_5x5_checkd
                    fuk_6x6_time_false_true_false = fuk_6x6_time
                    fuk_6x6_checkd_false_true_false = fuk_6x6_checkd

                if not is_bt and is_var_heu and is_val_heu:
                    bin_6x6_time_false_true_true = bin_6x6_time
                    bin_6x6_checkd_false_true_true = bin_6x6_checkd
                    bin_8x8_time_false_true_true = bin_8x8_time
                    bin_8x8_checkd_false_true_true = bin_8x8_checkd
                    bin_10x10_time_false_true_true = bin_10x10_time
                    bin_10x10_checkd_false_true_true = bin_10x10_checkd
                    fuk_4x4_time_false_true_true = fuk_4x4_time
                    fuk_4x4_checkd_false_true_true = fuk_4x4_checkd
                    fuk_5x5_time_false_true_true = fuk_5x5_time
                    fuk_5x5_checkd_false_true_true = fuk_5x5_checkd
                    fuk_6x6_time_false_true_true = fuk_6x6_time
                    fuk_6x6_checkd_false_true_true = fuk_6x6_checkd
                is_val_heu = True
            is_var_heu = True
        is_bt = False

    #zad1 przeszukiwane starny porównanie wpływu heurystyk y = ilość stanów x = n

    # binary backtrack brak heurystyk
    print(bin_6x6_checkd_true_false_false)
    print(bin_8x8_checkd_true_false_false)
    print(bin_10x10_checkd_true_false_false)

    #binary backtrack random val
    print(bin_6x6_checkd_true_false_true)
    print(bin_8x8_checkd_true_false_true)
    print(bin_10x10_checkd_true_false_true)

    print("\nporównanie binary backtracking heur i bez\n")
    pyl.plot([6,8,10], [sum(bin_6x6_checkd_true_false_false)/len(bin_6x6_checkd_true_false_false),
                        sum(bin_8x8_checkd_true_false_false)/len(bin_8x8_checkd_true_false_false),
                        sum(bin_10x10_checkd_true_false_false)/len(bin_10x10_checkd_true_false_false)],
             label='bez heur')
    pyl.plot([6,8,10], [sum(bin_6x6_checkd_true_false_true)/len(bin_6x6_checkd_true_false_true),
                        sum(bin_8x8_checkd_true_false_true)/len(bin_8x8_checkd_true_false_true),
                        sum(bin_10x10_checkd_true_false_true)/len(bin_10x10_checkd_true_false_true)],
             label=' heur')
    pyl.legend()
    pyl.show()

    #plot 1 porównanie binary backtracking heur i bez---------------------------------------------------------------------

    #futoshiki backtrack brak heurystyk
    print(fuk_4x4_checkd_true_false_false)
    print(fuk_5x5_checkd_true_false_false)
    print(fuk_6x6_checkd_true_false_false)

    # futoshiki backtrack random val
    print(fuk_4x4_checkd_true_false_true)
    print(fuk_5x5_checkd_true_false_true)
    # print(fuk_6x6_checkd_true_false_true)
    # , sum(fuk_6x6_checkd_true_false_false) / len(fuk_6x6_checkd_true_false_false)
    # , sum(fuk_6x6_checkd_true_false_true) / len(fuk_6x6_checkd_true_false_true)

    print("\nplot 2 porównanie fukoshiki backtracking heur i bez\n")
    pyl.plot([4, 5, 6], [sum(fuk_4x4_checkd_true_false_false)/len(fuk_4x4_checkd_true_false_false),
                         sum(fuk_5x5_checkd_true_false_false)/len(fuk_5x5_checkd_true_false_false),
                         sum(fuk_6x6_checkd_true_false_false) / len(fuk_6x6_checkd_true_false_false)],
             label='bez heur')
    pyl.plot([4, 5, 6], [sum(fuk_4x4_checkd_true_false_true)/len(fuk_4x4_checkd_true_false_true),
                         sum(fuk_5x5_checkd_true_false_true)/len(fuk_5x5_checkd_true_false_true),
                         sum(fuk_6x6_checkd_true_false_true) / len(fuk_6x6_checkd_true_false_true)],
             label=' heur')
    pyl.legend()
    pyl.show()

    # plot 2 porównanie fukoshiki backtracking heur i bez-----------------------------------------------------------------

    #dla backtracku heurystyka wyboru zmiennej nie ma wpływu!

    #binary foreward brak heur
    print(bin_6x6_checkd_false_false_false)
    print(bin_8x8_checkd_false_false_false)
    print(bin_10x10_checkd_false_false_false)

    #binary foreward val heur
    print(bin_6x6_checkd_false_false_true)
    print(bin_8x8_checkd_false_false_true)
    print(bin_10x10_checkd_false_false_true)

    #binary foreward var heur
    print(bin_6x6_checkd_false_true_false)
    print(bin_8x8_checkd_false_true_false)
    print(bin_10x10_checkd_false_true_false)

    #binary foreward both
    print(bin_6x6_checkd_false_true_true)
    print(bin_8x8_checkd_false_true_true)
    print(bin_10x10_checkd_false_true_true)
    print("\nplot 3porównanie binary dla foreward heur i bez\n")
    pyl.plot([6, 8, 10], [sum(bin_6x6_checkd_false_false_false)/len(bin_6x6_checkd_false_false_false),
                          sum(bin_8x8_checkd_false_false_false)/len(bin_8x8_checkd_false_false_false),
                          sum(bin_10x10_checkd_false_false_false)/len(bin_10x10_checkd_false_false_false)],
             label='bez heur')
    pyl.plot([6, 8, 10], [sum(bin_6x6_checkd_false_false_true)/len(bin_6x6_checkd_false_false_true),
                          sum(bin_8x8_checkd_false_false_true)/len(bin_8x8_checkd_false_false_true),
                          sum(bin_10x10_checkd_false_false_true)/len(bin_10x10_checkd_false_false_true)],
             label='val heur')
    pyl.plot([6, 8, 10], [sum(bin_6x6_checkd_false_true_false)/len(bin_6x6_checkd_false_true_false),
                          sum(bin_8x8_checkd_false_true_false)/len(bin_8x8_checkd_false_true_false),
                          sum(bin_10x10_checkd_false_true_false)/len(bin_10x10_checkd_false_true_false)],
             label='var heur')
    pyl.plot([6, 8, 10], [sum(bin_6x6_checkd_false_true_true)/len(bin_6x6_checkd_false_true_true),
                          sum(bin_8x8_checkd_false_true_true)/len(bin_8x8_checkd_false_true_true),
                          sum(bin_10x10_checkd_false_true_true)/len(bin_10x10_checkd_false_true_true)],
             label='both heur')
    pyl.legend()
    pyl.show()

    #plot 3porównanie binary dla foreward heur i bez-------------------------------------------------------------------

    #fukoshiki foreward brak heur
    print(fuk_4x4_checkd_false_false_false)
    print(fuk_5x5_checkd_false_false_false)
    print(fuk_6x6_checkd_false_false_false)

    #fukoshiki foreward val heur
    print(fuk_4x4_checkd_false_false_true)
    print(fuk_5x5_checkd_false_false_true)
    print(fuk_6x6_checkd_false_false_true)

    #fukoshiki foreward var heur
    print(fuk_4x4_checkd_false_true_false)
    print(fuk_5x5_checkd_false_true_false)
    print(fuk_6x6_checkd_false_true_false)

    #fukoshiki foreward both
    print(fuk_4x4_checkd_false_true_true)
    print(fuk_5x5_checkd_false_true_true)
    print(fuk_6x6_checkd_false_true_true)
    print("\nplot 4 porównanie foreward dla foreward heur i bez\n")
    pyl.plot([4, 5, 6], [sum(fuk_4x4_checkd_false_false_false)/len(fuk_4x4_checkd_false_false_false),
                         sum(fuk_5x5_checkd_false_false_false)/len(fuk_5x5_checkd_false_false_false),
                         sum(fuk_6x6_checkd_false_false_false)/len(fuk_6x6_checkd_false_false_false)],
             label='bez heur')
    pyl.plot([4, 5, 6], [sum(fuk_4x4_checkd_false_false_true)/len(fuk_4x4_checkd_false_false_true),
                         sum(fuk_5x5_checkd_false_false_true)/len(fuk_5x5_checkd_false_false_true),
                         sum(fuk_6x6_checkd_false_false_true)/len(fuk_6x6_checkd_false_false_true)],
             label='val heur')
    pyl.plot([4, 5, 6], [sum(fuk_4x4_checkd_false_true_false) / len(fuk_4x4_checkd_false_true_false),
                         sum(fuk_5x5_checkd_false_true_false) / len(fuk_5x5_checkd_false_true_false),
                         sum(fuk_6x6_checkd_false_true_false)/len(fuk_6x6_checkd_false_true_false)],
             label='var heur')
    pyl.plot([4, 5, 6], [sum(fuk_4x4_checkd_false_true_true) / len(fuk_4x4_checkd_false_true_true),
                         sum(fuk_5x5_checkd_false_true_true) / len(fuk_5x5_checkd_false_true_true),
                         sum(fuk_6x6_checkd_false_true_true)/len(fuk_6x6_checkd_false_true_true)],
             label='both heur')
    pyl.legend()
    pyl.show()

    # plot 4 porównanie foreward dla foreward heur i bez---------------------------------------------------------------

    #porównanie czasów backtracking vs foreward dla różnych heurystyk (4 poloty)

    #binary backtracking czas brak heurystyk
    print(bin_6x6_time_true_false_false)
    print(bin_8x8_time_true_false_false)
    print(bin_10x10_time_true_false_false)

    #binary foreward czas brak heur
    print(bin_6x6_time_false_false_false)
    print(bin_8x8_time_false_false_false)
    print(bin_10x10_time_false_false_false)
    print("\nplot 5 porównanie binary foreward i backtracking bez heur\n")
    pyl.plot([6, 8, 10], [sum(bin_6x6_time_true_false_false) / len(bin_6x6_time_true_false_false),
                          sum(bin_8x8_time_true_false_false) / len(bin_8x8_time_true_false_false),
                          sum(bin_10x10_time_true_false_false) / len(bin_10x10_time_true_false_false)],
             label='backtracking bez heur')
    pyl.plot([6, 8, 10], [sum(bin_6x6_time_false_false_false) / len(bin_6x6_time_false_false_false),
                          sum(bin_8x8_time_false_false_false) / len(bin_8x8_time_false_false_false),
                          sum(bin_10x10_time_false_false_false) / len(bin_10x10_time_false_false_false)],
             label='foreward bez heur')
    pyl.legend()
    pyl.show()

    # binary backtracking czas val heur
    print(bin_6x6_time_true_false_true)
    print(bin_8x8_time_true_false_true)
    print(bin_10x10_time_true_false_true)

    # binary foreward czas val heur
    print(bin_6x6_time_false_false_true)
    print(bin_8x8_time_false_false_true)
    print(bin_10x10_time_false_false_true)
    print("\nplot 6 porównanie binary foreward i backtracking z val heur\n")
    pyl.plot([6, 8, 10], [sum(bin_6x6_time_true_false_true) / len(bin_6x6_time_true_false_true),
                          sum(bin_8x8_time_true_false_true) / len(bin_8x8_time_true_false_true),
                          sum(bin_10x10_time_true_false_true) / len(bin_10x10_time_true_false_true)],
             label='backtracking val heur')
    pyl.plot([6, 8, 10], [sum(bin_6x6_time_false_false_true) / len(bin_6x6_time_false_false_true),
                          sum(bin_8x8_time_false_false_true) / len(bin_8x8_time_false_false_true),
                          sum(bin_10x10_time_false_false_true) / len(bin_10x10_time_false_false_true)],
             label='foreward val heur')
    pyl.legend()
    pyl.show()

    # binary backtracking czas var heur
    print(bin_6x6_time_true_true_false)
    print(bin_8x8_time_true_true_false)
    print(bin_10x10_time_true_true_false)

    # binary foreward czas var heur
    print(bin_6x6_time_false_true_false)
    print(bin_8x8_time_false_true_false)
    print(bin_10x10_time_false_true_false)
    print("\nplot 7 porównanie binary foreward i backtracking z var heur\n")
    pyl.plot([6, 8, 10], [sum(bin_6x6_time_true_true_false) / len(bin_6x6_time_true_true_false),
                          sum(bin_8x8_time_true_true_false) / len(bin_8x8_time_true_true_false),
                          sum(bin_10x10_time_true_true_false) / len(bin_10x10_time_true_true_false)],
             label='backtracking var heur')
    pyl.plot([6, 8, 10], [sum(bin_6x6_time_false_true_false) / len(bin_6x6_time_false_true_false),
                          sum(bin_8x8_time_false_true_false) / len(bin_8x8_time_false_true_false),
                          sum(bin_10x10_time_false_true_false) / len(bin_10x10_time_false_true_false)],
             label='foreward var heur')
    pyl.legend()
    pyl.show()

    # binary backtracking czas both heur
    print(bin_6x6_time_true_true_true)
    print(bin_8x8_time_true_true_true)
    print(bin_10x10_time_true_true_true)

    # binary foreward czas both heur
    print(bin_6x6_time_false_true_true)
    print(bin_8x8_time_false_true_true)
    print(bin_10x10_time_false_true_true)
    print("\nplot 8 porównanie binary foreward i backtracking z both heur\n")
    pyl.plot([6, 8, 10], [sum(bin_6x6_time_true_true_true) / len(bin_6x6_time_true_true_true),
                          sum(bin_8x8_time_true_true_true) / len(bin_8x8_time_true_true_true),
                          sum(bin_10x10_time_true_true_true) / len(bin_10x10_time_true_true_true)],
             label='backtracking both heur')
    pyl.plot([6, 8, 10], [sum(bin_6x6_time_false_true_true) / len(bin_6x6_time_false_true_true),
                          sum(bin_8x8_time_false_true_true) / len(bin_8x8_time_false_true_true),
                          sum(bin_10x10_time_false_true_true) / len(bin_10x10_time_false_true_true)],
             label='foreward both heur')
    pyl.legend()
    pyl.show()

    #fukoshiki backtracking brak heur
    print(fuk_4x4_time_true_false_false)
    print(fuk_5x5_time_true_false_false)
    print(fuk_6x6_time_true_false_false)

    # fukoshiki foreward brak heur
    print(fuk_4x4_time_false_false_false)
    print(fuk_5x5_time_false_false_false)
    print(fuk_6x6_time_false_false_false)
    print("\nplot 9 porównanie fukushiki foreward i backtracking bez heur\n")
    pyl.plot([4, 5, 6], [sum(fuk_4x4_time_true_false_false) / len(fuk_4x4_time_true_false_false),
                         sum(fuk_5x5_time_true_false_false) / len(fuk_5x5_time_true_false_false),
                         sum(fuk_6x6_time_true_false_false) / len(fuk_6x6_time_true_false_false)],
             label='backtracking brak heur')
    pyl.plot([4, 5, 6], [sum(fuk_4x4_time_false_false_false) / len(fuk_4x4_time_false_false_false),
                         sum(fuk_5x5_time_false_false_false) / len(fuk_5x5_time_false_false_false),
                         sum(fuk_6x6_time_false_false_false) / len(fuk_6x6_time_false_false_false)],
             label='foreward brak heur')
    pyl.legend()
    pyl.show()

    # fukoshiki backtracking val heur
    print(fuk_4x4_time_true_false_true)
    print(fuk_5x5_time_true_false_true)
    print(fuk_6x6_time_true_false_true)

    # fukoshiki foreward val heur
    print(fuk_4x4_time_false_false_true)
    print(fuk_5x5_time_false_false_true)
    print(fuk_6x6_time_false_false_true)
    print("\nplot 10 porównanie fukushiki foreward i backtracking z val heur\n")
    pyl.plot([4, 5, 6], [sum(fuk_4x4_time_true_false_true) / len(fuk_4x4_time_true_false_true),
                         sum(fuk_5x5_time_true_false_true) / len(fuk_5x5_time_true_false_true),
                         sum(fuk_6x6_time_true_false_true) / len(fuk_6x6_time_true_false_true)],
             label='backtracking val heur')
    pyl.plot([4, 5, 6], [sum(fuk_4x4_time_false_false_true) / len(fuk_4x4_time_false_false_true),
                         sum(fuk_5x5_time_false_false_true) / len(fuk_5x5_time_false_false_true),
                         sum(fuk_6x6_time_false_false_true) / len(fuk_6x6_time_false_false_true)],
             label='foreward val heur')
    pyl.legend()
    pyl.show()

    # fukoshiki backtracking var heur
    print(fuk_4x4_time_true_true_false)
    print(fuk_5x5_time_true_true_false )
    print(fuk_6x6_time_true_true_false)

    # fukoshiki foreward var heur
    print(fuk_4x4_time_false_true_false)
    print(fuk_5x5_time_false_true_false)
    print(fuk_6x6_time_false_true_false)
    print("\nplot 11 porównanie fukushiki foreward i backtracking z var heur\n")
    pyl.plot([4, 5, 6], [sum(fuk_4x4_time_true_true_false) / len(fuk_4x4_time_true_true_false),
                         sum(fuk_5x5_time_true_true_false) / len(fuk_5x5_time_true_true_false),
                         sum(fuk_6x6_time_true_true_false) / len(fuk_6x6_time_true_true_false)],
             label='backtracking var heur')
    pyl.plot([4, 5, 6], [sum(fuk_4x4_time_false_true_false) / len(fuk_4x4_time_false_true_false),
                         sum(fuk_5x5_time_false_true_false) / len(fuk_5x5_time_false_true_false),
                         sum(fuk_6x6_time_false_true_false) / len(fuk_6x6_time_false_true_false)],
             label='foreward var heur')
    pyl.legend()
    pyl.show()

    # fukoshiki backtracking both heur
    print(fuk_4x4_time_true_true_true)
    print(fuk_5x5_time_true_true_true)
    print(fuk_6x6_time_true_true_true)

    # fukoshiki foreward both heur
    print(fuk_4x4_time_false_true_true)
    print(fuk_5x5_time_false_true_true)
    print(fuk_6x6_time_false_true_true)
    print("\nplot 12 porównanie fukushiki foreward i backtracking z both heur\n")
    pyl.plot([4, 5, 6], [sum(fuk_4x4_time_true_true_true) / len(fuk_4x4_time_true_true_true),
                         sum(fuk_5x5_time_true_true_true) / len(fuk_5x5_time_true_true_true),
                         sum(fuk_6x6_time_true_true_true) / len(fuk_6x6_time_true_true_true)],
             label='backtracking both heur')
    pyl.plot([4, 5, 6], [sum(fuk_4x4_time_false_true_true) / len(fuk_4x4_time_false_true_true),
                         sum(fuk_5x5_time_false_true_true) / len(fuk_5x5_time_false_true_true),
                         sum(fuk_6x6_time_false_true_true) / len(fuk_6x6_time_false_true_true)],
             label='foreward both heur')
    pyl.legend()
    pyl.show()

    # print("binary 6x6")
    # print(bin_6x6_checkd_true_true_false)
    # print(bin_6x6_checkd_true_true_true)
    # print("binary 8x8")
    # print(bin_8x8_checkd_true_true_false)
    # print(bin_8x8_checkd_true_true_true)
    # print("binary 10x10")
    # print(bin_10x10_checkd_true_true_false)
    # print(bin_10x10_checkd_true_true_true)
    # print("fukoshiki 4x4")
    # print(fuk_4x4_checkd_true_true_false )
    # print(fuk_4x4_checkd_true_true_true )
    # print("fukoshiki 5x5")
    # print(fuk_5x5_checkd_true_true_false)
    # print(fuk_5x5_checkd_true_true_true)
    # print("fukoshiki 6x6")
    # print(fuk_6x6_checkd_true_true_false)
    # print(fuk_6x6_checkd_true_true_true)

    #dorobić ploty

