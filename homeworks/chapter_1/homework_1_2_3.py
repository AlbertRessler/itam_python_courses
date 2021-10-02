string = input()
for (first_index, symbol) in enumerate(string):
    new_string = (first_index, symbol)
    if symbol.isupper():
        first_letter = string[first_index]
        break
for (second_index, symbol) in enumerate(string):
    new_string = (second_index, symbol)
    if symbol.isdigit():
        second_letter = string[second_index + 1]
        break
step = int(second_index + 1 - first_index)
other = string[second_index + 1::step]
almost_answer = first_letter + other
if almost_answer[-1] == '.':
    answer = almost_answer.replace('.', '', 1)
else:
    answer = almost_answer
print(answer, end='.')
