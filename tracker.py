import csv
import datetime

current_date = datetime.datetime.now()

def message(message, number):
    print(f'{message} {number} €')

def add():
    #input + date
    new_input = input('Enter New Expese ...: ').title().split()
    new_input.append( current_date.strftime("%B"))
    new_input.append( current_date.year)
    duplicate_found = False
    
    #iterate csv file for match
    with open ('tracker.csv', 'r' , newline='') as file:
        reader = csv.reader(file, delimiter = ',')
        lines = list(reader)

        for x in enumerate(lines):
                current_year = current_date.year
                if new_input[0] in x[1] and lines[x[0]][2] == current_date.strftime("%B") and current_year == int(lines[x[0]][3]):
                    duplicate_found = True
                    lines[x[0]][1] = float(lines[x[0]][1]) + float(new_input[1])
                    with open ('tracker.csv', 'w', newline='') as file:
                        writer = csv.writer(file, delimiter = ',')
                        writer.writerows(lines)
                        print('Duplicate Found. Expense Added.')

        #no match found
        if duplicate_found == False:
             with open ('tracker.csv', 'a', newline='') as file:
                writer = csv.writer(file, delimiter = ',')
                writer.writerow(new_input)
                print("New Expense Added.")


"""Expenses of this month"""
def calculate_current_month():
    with open ('tracker.csv', 'r' , newline='') as file:
        reader = csv.reader(file, delimiter = ',')
        lines = list(reader)
        numbers_list = []

        for x ,y in enumerate(lines):
            if y[2] == current_date.strftime("%B"):
                numbers = float(y[1])
                numbers_list.append(numbers)
                
        sum_numbers_list = sum(numbers_list)
        #print('Total Expenses of the current month is:', round(sum_numbers_list, 2), "€")
        message('Total Expenses of this month is', round(sum_numbers_list, 2))


"""Expense of choosen month"""
def calculate_any_month():
    input_month = input().title()

    with open ('tracker.csv', 'r' , newline='') as file:
        reader = csv.reader(file, delimiter = ',')
        lines = list(reader)
        numbers_list = []

        for x ,y in enumerate(lines):
            if y[2] == input_month:
                numbers = float(y[1])
                numbers_list.append(numbers)

        sum_numbers_list = sum(numbers_list)
        print('Total Expenses of',input_month, 'is:', round(sum_numbers_list, 2), "€")
        message("")


"""Expenses of choosen year"""
def calculate_year():
    input_year = int(input('Enter a year: '))

    with open ('tracker.csv', 'r' , newline='') as file:
        reader = csv.reader(file, delimiter = ',')
        lines = list(reader)
        numbers_list = []

        for x ,y in enumerate(lines):
            if int(y[3]) == input_year:
                numbers = float(y[1])
                numbers_list.append(numbers)

        sum_numbers_list = sum(numbers_list)
        print('Total Expenses of this year  is:', round(sum_numbers_list, 2), "€")


"""User Interface"""
def choices():
    input_choice = int(input('[1] Add New Expense\n' + '[2] Total Expenses of this month\n' + '[3] Calculate any month\n' + '[4] Calculate all year\n' + 'Enter : '))
    
    if input_choice == 1:
        add()
    elif input_choice == 2:
        calculate_current_month()
    elif input_choice == 3:
        calculate_any_month()
    elif input_choice == 4:
        calculate_year()

    else:
        print('Not Valid Input')

choices()



