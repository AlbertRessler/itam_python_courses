def summation(numbers):
    positive_numbers = []
    normalized_numbers = []
    numbers_list = numbers.split()
    for idx, arg in enumerate(numbers_list):
        int_arg = int(arg)
        if int_arg < 0:
            new_arg = abs(int_arg) * 2
        else:
            new_arg = int_arg
        positive_numbers.append(new_arg)
    max_of_positive_numbers = max(positive_numbers)
    for idx, arg in enumerate(positive_numbers):
        normalized_arg = arg / max_of_positive_numbers
        normalized_numbers.append(normalized_arg)
    print(sum(normalized_numbers))
