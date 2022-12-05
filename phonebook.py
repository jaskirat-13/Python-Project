def print_menu():
    print('1. Print Phone Numbers')
    print('2. Add a Phone Number')
    print('3. Search a Phone Number')
    print('4. Quit')
    print()

numbers = {}
ch = 0
print_menu()
while True:
    ch = int(input("Type in a number (1-4): "))
    if ch == 1:
        print("Telephone Numbers:")
        for x in numbers.keys():
            print("Name: ", x, "\tNumber:", numbers[x])
        print()
        
    elif ch == 2:
        print("Add Name and Number")
        name = input("Name: ")
        phone = input("Number: ")
        numbers[name] = phone

    elif ch == 3:
        print("Search Number")
        name = input("Name: ")
        if name in numbers:
            print("The number is", numbers[name])
        else:
            print(name, "was not found")
    elif ch == 4:
        break
    
    else:
        print("Enter a valid choice")
