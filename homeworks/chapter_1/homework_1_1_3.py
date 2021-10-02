string = input()
if len(string) >= 5:
    print(string[2], string[4])
else:
    print(string[::-2])
