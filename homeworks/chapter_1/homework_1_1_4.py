list = input()
list_splitted = list.split()
count_of_negative = 0
more_than_eight = 0
count_of_even = 0
for i in range(len(list_splitted)):
    if int(list_splitted[i]) < 0:
        count_of_negative += 1
    if int(list_splitted[i]) % 2 == 0:
        count_of_even += 1
    if int(list_splitted[i]) > 8:
        more_than_eight += 1
print(count_of_negative, more_than_eight, count_of_even)