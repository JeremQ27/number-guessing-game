import sys
import random, time
from set_high_score import save_new_high_score, view_high_score, create_highscore_json, load_high_score, reset_high_score

high_score_easy = 0
high_score_medium = 0
high_score_hard = 0

def display_menu():
    print('Welcome to the Number Guessing Game!')
    print("I'm thinking of a number between 1 and 100.\n")
    print('Please select the difficulty level:')
    print('1. Easy (10 chances)')
    print('2. Medium (5 chances)')
    print('3. Hard (3 chances)')


def other_options():
    print('Options: ')
    print('\t\'r\' - reset high score')
    print('\t\'h\' - view high score')
    print('\t\'q\' - quit')
    print('\t\'b\' - back')
    while True:
        inp = input('Enter: ')
        if inp == 'r':
            reset_high_score()
            print('High score has been succesfully reset. Returning to main menu...')
            time.sleep(1)
            pick_difficulty()
        elif inp == 'h':
            view_high_score()
        elif inp == 'q':
            sys.exit()
        elif inp == 'b':
            return
        else:
            print('Option not available. Please try again.')

def pick_difficulty():
    load_high_score()
    display_menu()
    while True:
        difficulty_level = input('Enter your choice: Press \'h\' to view high score, \'o\' for other options, \'q\' to exit.')
        str_diff_level = difficulty_level.lower()
        if difficulty_level == '1' or str_diff_level == 'easy':
            return 10
        elif difficulty_level == '2' or str_diff_level == 'medium':
            return 5
        elif difficulty_level == '3' or str_diff_level == 'hard':
            return 3
        elif str_diff_level == 'h':
            view_high_score()
        elif str_diff_level == 'o':
            other_options()
        elif str_diff_level == 'q':
            sys.exit()
        else:
            print('Option not available. Please try again.')


def num_guess(num, num_chance):
    ctr = 0
    while ctr < num_chance:
        try:
            guess = int(input('Enter your guess (int only): '))
        except ValueError:
            print('Input is invalid. Please try again.')
            continue
        if guess == num:
            print(f'Congratulations! You guessed the correct number in {ctr + 1} attempts. Would you like to play again?')
            save_new_high_score(num_chance, ctr + 1)
            time.sleep(0.5)
            return
        elif num < guess:
            print(f'Incorrect!The number is less than {guess}.')
        elif num > guess:
            print(f'Incorrect! The number is greater than {guess}.')
        ctr += 1
    print('Maximum attempt reached. Sorry you lost. Would you like to try again?')
    time.sleep(0.5)

def main():

    while True:

        num_chance = pick_difficulty()
        num = random.randint(1, 100)
        print(f'Num = {num}')
        num_guess(num, num_chance)






if __name__ == "__main__":
    main()