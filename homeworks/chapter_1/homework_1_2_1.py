N = int(input())
count_of_true = 0
for i in range(N):
    list = input()
    list_splitted = list.split()
    last_element = list_splitted.pop()
    if last_element == 'True':
        count_of_true += 1
print(count_of_true, N - count_of_true)
