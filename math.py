#! python3
# math.py - multiplication of numbers
import random
"""START OF DICTIONARY"""

def two():
    dict_two = {
        "1 * 2" : 2,
        "2 x 2" : 4,
        "3 x 2" : 6,
        "4 x 2" : 8,
        "5 x 2" : 10,
        "6 x 2" : 12,
        "7 x 2" : 14,
        "8 x 2" : 16,
        "9 x 2" : 18,
        "10 x 2" : 20
    }
    return dict_two

def three():
    dict_three = {
        "1 x 3" : 3,
        "2 x 3" : 6,
        "3 x 3" : 9,
        "4 x 3" : 12,
        "5 x 3" : 15,
        "6 x 3" : 18,
        "7 x 3" : 21,
        "8 x 3" : 24,
        "9 x 3" : 27,
        "10 x 3" : 30
    }
    return dict_three

def four():
    dict_four = {
        "1 x 4" : 4,
        "2 x 4" : 8,
        "3 x 4" : 12,
        "4 x 4" : 16,
        "5 x 4" : 20,
        "6 x 4" : 24,
        "7 x 4" : 28,
        "8 x 4" : 32,
        "9 x 4" : 36,
        "10 x 4" : 40
    }
    return dict_four

def five():
    dict_five = {
        "1 x 5" : 5,
        "2 x 5" : 10,
        "3 x 5" : 15,
        "4 x 5" : 20,
        "5 x 5" : 25,
        "6 x 5" : 30,
        "7 x 5" : 35,
        "8 x 5" : 40,
        "9 x 5" : 45,
        "10 x 5" : 50
    }
    return dict_five

def six():
    dict_six = {
        "1 x 6" : 6,
        "2 x 6" : 12,
        "3 x 6" : 18,
        "4 x 6" : 24,
        "5 x 6" : 30,
        "6 x 6" : 36,
        "7 x 6" : 42,
        "8 x 6" : 48,
        "9 x 6" : 54,
        "10 x 6" : 60
    }
    return dict_six

def seven():
    dict_seven = {
        "1 x 7" : 7,
        "2 x 7" : 14,
        "3 x 7" : 21,
        "4 x 7" : 28,
        "5 x 7" : 35,
        "6 x 7" : 42,
        "7 x 7" : 49,
        "8 x 7" : 56,
        "9 x 7" : 63,
        "10 x 7" : 70
    }
    return dict_seven

def eight():
    dict_eight = {
        "1 x 8" : 8,
        "2 x 8" : 16,
        "3 x 8" : 24,
        "4 x 8" : 32,
        "5 x 8" : 40,
        "6 x 8" : 48,
        "7 x 8" : 56,
        "8 x 8" : 64,
        "9 x 8" : 72,
        "10 x 8" : 80
    }
    return dict_eight

def nine():
    dict_nine = {
        "1 x 9" : 9,
        "2 x 9" : 18,
        "3 x 9" : 27,
        "4 x 9" : 36,
        "5 x 9" : 45,
        "6 x 9" : 54,
        "7 x 9" : 63,
        "8 x 9" : 72,
        "9 x 9" : 81,
        "10 x 9" : 90
    }
    return dict_nine

""" END OF DICTIONARY"""

def calculation():
    correct_answers = 0 # store the correct answers/10

    # iterate over dictionary
    for key, value in choices().items():
        try:
            print(key) # print the question to the user
            question_answer = value # store the answer
            user_answer = int(input("= ")) # user input as number

            # check if the answer is correct
            if question_answer == user_answer:    
                print('Correct!\n' + '----------')
                correct_answers += 1
            else:
                print("Wrong it's", value, '\n' + "----------")

        # if input not a number catch
        except ValueError as e:
            print('Invalid! That is not a number.', e)
        
    print("Correct ratio is", str(correct_answers),"/ 10")

def randomCalculation():
    choosen_dict = choices()
    correct_random = 0

    # iterate random choice 5 times
    for i in range(5):
        try:
            # dictionary transformed to list
            random_question = random.choice(list(choosen_dict.items()))
            # question
            print(random_question[0])
            user_answer = int(input("= "))
            i+=1

            # check if answer is correct
            if random_question[1] == user_answer:
                print("That's Correct!")
                correct_random += 1
            else:
                print("Wrong", random_question[1])

        # if input not a number catch
        except ValueError as e:
            print('Invalid! That is not a number.', e)

    print("Correct ratio is", correct_random, "/ 5")
    
def interface_main():
    input2 = input('normal[N] or random[R]: ').lower()
    if input2 == "n":
        calculation()
    elif input2 == "r":
        randomCalculation()
    else:
        print('invalid option')

def choices():
        input1 = int(input("Choose multiplication from 2 - 9: "))
        if input1 == 2:
            a = two()
            return a
        elif input1 == 3:
            b = three()
            return b
        elif input1 == 4:
            c = four()
            return c
        elif input1 == 5:
            d = five()
            return d
        elif input1 == 6:
            e = six()
            return e
        elif input1 == 7:
            f = seven()
            return f
        elif input1 == 8:
            g = eight()
            return g
        elif input1 == 9:
            h = nine()
            return h

interface_main()