import os
options_list = ["Store item information.", "Display items of the same type.",
                    "Edit an item.", "Delete an item.", "Add an item.", "Sort items."]
makeup_list = []

def log_in():
    PASSWORD = '1234'
    entered_password = str(input('Enter the Password:'))
    while entered_password != PASSWORD:
        print ('The password is incorrect')
        print('')
        entered_password = str(input('Enter the Password again:'))
    print('The password is correct')

def choosing_option():
    print ('Which option do you want to carry out:\n'
                        '1) Store item information: name, type, and quantity\n'
                        '2) Display all items from the same type \n'
                        '3) Edit one item quantity\n'
                        '4) Delete an item\n'
                        '5) Add an item\n'
                        '6) Sort items ascending or descending\n')

    choosing_option = input('Enter your number here: ')

    if choosing_option == '1':
        store()
    elif choosing_option == '2':
        display()
    elif choosing_option == '3':
        edit()
    elif choosing_option == '4':
        delete()
    elif choosing_option == '5':
        add()
    elif choosing_option == '6':
        sort()
    else:
        exit_program()

def store():
    makeup_file = open('makeup.txt', 'w')
    print('Enter the following data for the makeup products:')
    answer = 'y'

    while answer == 'y' or answer == 'Y':
        makeup = str(input('Enter the name of the product:'))
        type = str(input('Enter the type of the product (face,eye,lip):'))
        quantity = str(input('Enter the quantity of the product:'))
        print ('')

        makeup_file.write(str(makeup + '\n'))
        makeup_file.write(str(type + '\n'))
        makeup_file.write (str(quantity) + '\n')

        answer = input('Do you want to add another product? (yes = y,no = n)')

    makeup_file.close()
    print('The information has been saved in makeup.txt :)')

def display():
    found = False
    search_type = str(input("Which product's type do you want to display?"))
    makeup_file = open('makeup.txt','r')
    makeup = makeup_file.readline()
    line = makeup_file.readline()
    while line != '':
        quantity = makeup_file.readline()
        line = line.rstrip('\n')
        if line == search_type:
            print('Product:',makeup)
            print('Type:', type)
            print('Quantity',quantity)
            found = True
        line = makeup_file.readline()
    makeup_file.close()
    if not found:
        print('That type was not available')

def edit():
    found = False

    search = input('Enter a description to search for: ')
    new_quantity = int(input('Enter the new quantity: '))

    makeup_file = open('makeup.txt', 'r')
    temp_file = open('temp.txt', 'w')

    name = makeup_file.readline()

    while name != '':
        type = makeup_file.readline()
        quantity = makeup_file.readline()
        name = name.rstrip('\n')
        type = type.rstrip('\n')
        quantity = quantity.rstrip('\n')

        if name == search:
            temp_file.write(name + '\n')
            temp_file.write(type + '\n')
            temp_file.write(str(new_quantity) + '\n')

            found = True
        else:
            temp_file.write(name + '\n')
            temp_file.write(type + '\n')
            temp_file.write(str(quantity) + '\n')

        name = makeup_file.readline()

    makeup_file.close()
    temp_file.close()
    os.remove('makeup.txt')
    os.rename('temp.txt', 'makeup.txt')

    if found:
        print('The file has been updated.')
    else:
        print('That item was not found in the file.')

def delete():
    found = False
    search = input('which product do you want to delete? ')
    makeup_file = open('makeup.txt', 'r')
    temp_file = open('temp.txt','w')
    descr = makeup_file.readline()
    while descr != '':
        qty = str(makeup_file.readline())
        descr = descr.rstrip('\n')
        if descr != search:
            temp_file.write(descr + '\n')
            temp_file.write(str(qty) + '\n')
        else:
            found = True
        descr = makeup_file.readline()
    makeup_file.close()
    temp_file.close()
    os.remove('makeup.txt')
    os.rename('temp.txt','makeup.txt')
    if found:
        print('the file has been updated.')
    else :
        print('that item was not found in the file.')

def add():
    makeup_file = open('makeup.txt','a')
    answer = 'y'
    while answer == 'y' or answer == 'Y':
        makeup = str(input('Enter the name of the product:'))

        type = str(input('Enter the type of the product (face,eye,lip):'))

        quantity = str(input('Enter the quantity of the product:'))

        print('')

        makeup_file.write(str(makeup + '\n'))
        makeup_file.write(str(type + '\n'))
        makeup_file.write(str(quantity) + '\n')

        answer = input('Do you want to add another product? (yes = y, no = n) ')

    makeup_file.close()
    print('The information has been saved in makeup.txt :)')

def sort():
    order = input('Choose between sorting in ascending or descending order: (a = ascending, d = descending) ')
    makeup_file = open('makeup.txt', 'r')

    name = (makeup_file.readline()).rstrip('\n')
    type = (makeup_file.readline()).rstrip('\n')
    quantity = (makeup_file.readline()).rstrip('\n')

    while name != '':
        makeup_list.append([name, type, quantity])

        name = (makeup_file.readline()).rstrip('\n')
        type = (makeup_file.readline()).rstrip('\n')
        quantity = (makeup_file.readline()).rstrip('\n')
    makeup_file.close()

    if order == 'a':
        makeup_list.sort()
    elif order == 'd':
        makeup_list.sort(reverse=True)

    rows = len(makeup_list)
    columns = len(makeup_list[0])

    temp_file = open('temporary.txt', 'w')
    for r in range(rows):
        for c in range(columns):
            temp_file.write(makeup_list[r][c] + '\n')
    temp_file.close()

    os.remove('makeup.txt')
    os.rename('temporary.txt', 'makeup.txt')
    print('Products have been sorted')

def exit_program():
    print('Closing the Program . . .')

def main():
    print('Welcome to Sephora')
    print('')
    log_in()
    answer = 'y'
    while answer == 'y' or answer == 'Y':
        choosing_option()
        answer = input('Do you want to carry out another option? (yes = y, no = n) ')

    exit_program()

main()