import itertools

number_of_days = 0
min = -1
paths_found = []
cat_next_choices = [[-1, 1], [0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, -1]]
human_current_path = {}
a_cat_path_reach_limit_but_not_meet = False
global_human_fail_flag = False
a_human_start_fail = False

def check_cat(today, cat_choice, current_path_limit):

    global a_cat_path_reach_limit_but_not_meet
    if a_cat_path_reach_limit_but_not_meet == True:
        # print("cat", today, cat_choice,number_of_days, "case1")

        return 0
    if cat_choice == -1:
        # print("cat", today, cat_choice,number_of_days, "case2")

        return 1
    if today < current_path_limit:
        # print("cat", today, cat_choice,number_of_days, "case3")

        if cat_choice != human_current_path[today]:
            
            # print("cat", today, cat_choice,number_of_days, "case3a")

            return check_cat(today + 1, cat_next_choices[cat_choice][0], current_path_limit) * check_cat(today + 1, cat_next_choices[cat_choice][1], current_path_limit)
        else:
            # print("cat", today, cat_choice,number_of_days, "case3b")

            return 1
    else:
        # print("cat", today, cat_choice,number_of_days, "case4")

        a_cat_path_reach_limit_but_not_meet = True
        return 0
    
def check_human(today, human_choice):
    # print("human", today, human_choice, number_of_days)
    # print(human_current_path.items())
    global min
    if today < number_of_days:
        human_current_path[today] = human_choice
        # print(human_current_path.items())
        a_cat_start_fail = False
        for cat_start in range(7):
            global a_cat_path_reach_limit_but_not_meet 
            a_cat_path_reach_limit_but_not_meet = False
            if check_cat(0, cat_start, today + 1) == 0:
                a_cat_start_fail = True
                break

        if a_cat_start_fail == True:
            for choice in range(7):
                check_human(today + 1, choice)
        else:
            min = today + 1
            paths_found.append(dict(itertools.islice(human_current_path.items(), today + 1)).values())

# a_cat_path_reach_limit_but_not_meet = False
# print(check_cat(0, 0))
# a_cat_path_reach_limit_but_not_meet = False
# print(check_cat(0, 1))
# a_cat_path_reach_limit_but_not_meet = False
# print(check_cat(0, 2))
# a_cat_path_reach_limit_but_not_meet = False
# print(check_cat(0, 3))
# a_cat_path_reach_limit_but_not_meet = False
# print(check_cat(0, 4))


while min == -1:
    number_of_days += 1
    for human_choice in range(7):
        check_human(0, human_choice)

for path in paths_found:
    if len(path) == min:
        print(path)






        




            