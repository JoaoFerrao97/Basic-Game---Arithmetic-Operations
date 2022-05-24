"""
Here, you can run this script to start the game.

"""

# Libraries

from time import sleep
from colorama import Fore
from random import randint
from constrution_operations import *

score = 0

print()
print('-' * 200)
print(Fore.YELLOW + 'Basic Game - Arithmetic Operations'.center(200) + Fore.RESET)
print('-' * 200)
print()
print(Fore.MAGENTA + 'Note: This program just work with integral numbers. \n' + Fore.RESET)

print(Fore.BLUE + """Difficulty levels:

[1] - Easy
[2] - Medium
[3] - Hard
[4] - Very Hard
""" + Fore.RESET)

while True:
    difficulty: str = input(Fore.RED + '- Choose the difficulty level by indicating the number: ' + Fore.RESET)
    if difficulty.isnumeric():
        difficulty: int = int(difficulty)
        if difficulty > 4 or difficulty < 1:
            print()
            print(Fore.RED + '- The option entered is invalid. Please try again. \n' + Fore.RESET)
        else:
            break
    else:
        print()
        print(Fore.RED + '- The option entered is invalid. Please try again. \n' + Fore.RESET)

while True:
    if difficulty == 1:
        print()
        print('Write the result of the following operation: ')
        choice_function = randint(0, 1)
        if choice_function == 0:
            result_computer = easy_sum_operation()
        else:
            result_computer = easy_subtraction_operation()
        while True:
            result_user: str = input(Fore.RED + '- Result: ' + Fore.RESET)
            if result_user.isnumeric():
                result_user: int = int(result_user)
                break
            else:
                print()
                print(Fore.RED + '- The result entered is invalid. Please try again. \n' + Fore.RESET)
        if result_user == result_computer:
            score += 1
            print(Fore.BLUE + f'Congratulations! Right answer! Your score now is {score} point(s)' + Fore.RESET)
        else:
            print(Fore.BLUE + "Sorry, but you failed. Can't give to you any points" + Fore.RESET)
        print()
        print("""Do you want to continue playing ?
        
        [1] - Yes
        [2] - No
        """)
        while True:
            choice_program: str = input('Choice: ')
            if choice_program.isnumeric():
                choice_program: int = int(choice_program)
                if choice_program == 1:
                    print("All right. Let's continue playing.")
                    break
                elif choice_program == 2:
                    break
                else:
                    print()
                    print(Fore.RED + '- The option entered is invalid. Please try again. \n' + Fore.RESET)
            else:
                print()
                print(Fore.RED + '- The option entered is invalid. Please try again. \n' + Fore.RESET)
        if choice_program == 2:
            break
    if difficulty == 2:
        print()
        print('Write the result of the following operation: ')
        choice_function = randint(0, 2)
        if choice_function == 0:
            result_computer = medium_sum_operation()
        elif choice_function == 1:
            result_computer = medium_subtraction_operation()
        elif choice_function == 2:
            result_computer = medium_multiplication_operation()
        while True:
            result_user: str = input(Fore.RED + '- Result: ' + Fore.RESET)
            if result_user.isnumeric():
                result_user: int = int(result_user)
                break
            else:
                print()
                print(Fore.RED + '- The result entered is invalid. Please try again. \n' + Fore.RESET)
        if result_user == result_computer:
            score += 1
            print(Fore.BLUE + f'Congratulations! Right answer! Your score now is {score} point(s)' + Fore.RESET)
        else:
            print(Fore.BLUE + "Sorry, but you failed. Can't give to you any points" + Fore.RESET)
        print()
        print("""Do you want to continue playing ?

                [1] - Yes
                [2] - No
                """)
        while True:
            choice_program: str = input('Choice: ')
            if choice_program.isnumeric():
                choice_program: int = int(choice_program)
                if choice_program == 1:
                    print("All right. Let's continue playing.")
                    break
                elif choice_program == 2:
                    break
                else:
                    print()
                    print(Fore.RED + '- The option entered is invalid. Please try again. \n' + Fore.RESET)
            else:
                print()
                print(Fore.RED + '- The option entered is invalid. Please try again. \n' + Fore.RESET)
        if choice_program == 2:
            break
    if difficulty == 3:
        print()
        print('Write the result of the following operation: ')
        choice_function = randint(0, 2)
        if choice_function == 0:
            result_computer = hard_sum_operation()
        elif choice_function == 1:
            result_computer = hard_subtraction_operation()
        elif choice_function == 2:
            result_computer = hard_multiplication_operation()
        while True:
            result_user: str = input(Fore.RED + '- Result: ' + Fore.RESET)
            if result_user.isnumeric():
                result_user: int = int(result_user)
                break
            else:
                print()
                print(Fore.RED + '- The result entered is invalid. Please try again. \n' + Fore.RESET)
        if result_user == result_computer:
            score += 1
            print(Fore.BLUE + f'Congratulations! Right answer! Your score now is {score} point(s)' + Fore.RESET)
        else:
            print(Fore.BLUE + "Sorry, but you failed. Can't give to you any points" + Fore.RESET)
        print()
        print("""Do you want to continue playing ?

                        [1] - Yes
                        [2] - No
                        """)
        while True:
            choice_program: str = input('Choice: ')
            if choice_program.isnumeric():
                choice_program: int = int(choice_program)
                if choice_program == 1:
                    print("All right. Let's continue playing.")
                    break
                elif choice_program == 2:
                    break
                else:
                    print()
                    print(Fore.RED + '- The option entered is invalid. Please try again. \n' + Fore.RESET)
            else:
                print()
                print(Fore.RED + '- The option entered is invalid. Please try again. \n' + Fore.RESET)
        if choice_program == 2:
            break
    if difficulty == 4:
        print()
        print('Write the result of the following operation: ')
        choice_function = randint(0, 2)
        if choice_function == 0:
            result_computer = veryhard_sum_operation()
        elif choice_function == 1:
            result_computer = veryhard_subtraction_operation()
        elif choice_function == 2:
            result_computer = veryhard_multiplication_operation()
        while True:
            result_user: str = input(Fore.RED + '- Result: ' + Fore.RESET)
            if result_user.isnumeric():
                result_user: int = int(result_user)
                break
            else:
                print()
                print(Fore.RED + '- The result entered is invalid. Please try again. \n' + Fore.RESET)
        if result_user == result_computer:
            score += 1
            print(Fore.BLUE + f'Congratulations! Right answer! Your score now is {score} point(s)' + Fore.RESET)
        else:
            print(Fore.BLUE + "Sorry, but you failed. Can't give to you any points" + Fore.RESET)
        print()
        print("""Do you want to continue playing ?

                                [1] - Yes
                                [2] - No
                                """)
        while True:
            choice_program: str = input('Choice: ')
            if choice_program.isnumeric():
                choice_program: int = int(choice_program)
                if choice_program == 1:
                    print("All right. Let's continue playing.")
                    break
                elif choice_program == 2:
                    break
                else:
                    print()
                    print(Fore.RED + '- The option entered is invalid. Please try again. \n' + Fore.RESET)
            else:
                print()
                print(Fore.RED + '- The option entered is invalid. Please try again. \n' + Fore.RESET)
        if choice_program == 2:
            break

print()
print('Turning off the program...\n')
sleep(3)
print(Fore.BLUE + f'Program Off. Your final score is {score}' + Fore.RESET)