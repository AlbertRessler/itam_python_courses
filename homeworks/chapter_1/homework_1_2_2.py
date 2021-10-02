N = int(input())
count_of_trues = 0
count_of_false = 0
count_of_none = 0
for i in range(N):
    list = input()
    list_splitted = list.split()
    if list_splitted.count('True') == 1 and list_splitted.count('False') == 0:
        count_of_trues += 1
    elif list_splitted.count('True') == 0 and list_splitted.count('False') == 1:
        count_of_false += 1
    else:
        if list_splitted[3] == 'True':
            count_of_trues += 1
        elif list_splitted[3] == 'False':
            count_of_false += 1
        else:
            count_of_none += 1
print(count_of_trues, count_of_false, count_of_none)
