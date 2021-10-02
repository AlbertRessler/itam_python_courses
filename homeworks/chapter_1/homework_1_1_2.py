list = input()
list_splitted = list.split()
max = list_splitted[0]
min = list_splitted[0]
i = 0
for i in range(len(list_splitted)):
    if int(list_splitted[i]) > int(max):
        max = list_splitted[i]
for k in range(len(list_splitted)):
    if int(list_splitted[k]) < int(min):
        min = list_splitted[k]
print(max, min)