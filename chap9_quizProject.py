#! python3
"""Project: Generating Random Quiz Files. System agnostic
    https://automatetheboringstuff.com/2e/chapter9/
"""

import random
import os
from pathlib import Path

NUMQUIZES = 9
CAPITALS = {'Alabama': 'Montgomery',
            'Alaska': 'Juneau',
            'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock',
            'California': 'Sacramento',
            'Colorado': 'Denver',
            'Connecticut': 'Hartford',
            'Delaware': 'Dover',
            'Florida': 'Tallahassee',
            'Georgia': 'Atlanta',
            'Hawaii': 'Honolulu',
            'Idaho': 'Boise',
            'Illinois': 'Springfield',
            'Indiana': 'Indianapolis',
            'Iowa': 'Des Moines',
            'Kansas': 'Topeka',
            'Kentucky': 'Frankfort',
            'Louisiana': 'Baton Rouge',
            'Maine': 'Augusta',
            'Maryland': 'Annapolis',
            'Massachusetts': 'Boston',
            'Michigan': 'Lansing',
            'Minnesota': 'Saint Paul',
            'Mississippi': 'Jackson',
            'Missouri': 'Jefferson City',
            'Montana': 'Helena',
            'Nebraska': 'Lincoln',
            'Nevada': 'Carson City',
            'New Hampshire': 'Concord',
            'New Jersey': 'Trenton',
            'New Mexico': 'Santa Fe',
            'New York': 'Albany',
            'North Carolina': 'Raleigh',
            'North Dakota': 'Bismarck',
            'Ohio': 'Columbus',
            'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem',
            'Pennsylvania': 'Harrisburg',
            'Rhode Island': 'Providence',
            'South Carolina': 'Columbia',
            'South Dakota': 'Pierre',
            'Tennessee': 'Nashville',
            'Texas': 'Austin',
            'Utah': 'Salt Lake City',
            'Vermont': 'Montpelier',
            'Virginia': 'Richmond',
            'Washington': 'Olympia',
            'West Virginia': 'Charleston',
            'Wisconsin': 'Madison',
            'Wyoming': 'Cheyenne'}
idx2letter = {0: 'A', 1: 'B', 2: 'C', 3: 'D'}


def main():
    """Generates NUMQUIZES random US states capitals
    quiz and answer key files"""
    full_path = prompt_user()
    # Generate 35 quiz files
    for quiz_num in range(NUMQUIZES):
        # create quiz and answer key files
        with open(full_path / f"quiz{quiz_num}.txt", 'w') as quiz_file:
            with open(full_path / f"key{quiz_num}.txt", 'w') as key_file:
                # write headers
                header = f'### QUIZ {quiz_num} ###'.center(65)
                quiz_file.write(header + '\n\n')
                header = f' ### ANSWER KEY for QUIZ {quiz_num} ###'
                key_file.write(header + '\n\n')

                # create list of shuffled states
                rnd_states = random.sample(CAPITALS.keys(), len(CAPITALS))

                # loop thru all states, making a question for each
                for q_num, state in enumerate(rnd_states):
                    # create answer bank
                    answers = [CAPITALS[state]]  # add correct answer to list
                    while True:  # add three incorrect answers
                        rnd_idx = random.randint(0, len(CAPITALS) - 1)
                        bad_ans = CAPITALS[rnd_states[rnd_idx]]
                        if bad_ans not in answers:
                            answers.append(bad_ans)
                        if len(answers) == 4:
                            break

                    random.shuffle(answers)
                    # write correct answer to key file
                    key_file.write(
                        f'{str(q_num + 1).zfill(2)}: '
                        f'{idx2letter[answers.index(CAPITALS[state])]}\n'
                    )
                    # write to quiz file
                    quiz_file.write(
                        f'{q_num + 1} -  Capital of {state}:\n    ')
                    for ans_idx, ans in enumerate(answers):
                        quiz_file.write(f'{idx2letter[ans_idx]}) '
                                        f'{ans} ')
                    quiz_file.write('\n\n')


def prompt_user():
    """Prompts the user for location to save file and returns the path"""
    # also ask how many quizzes?
    while True:
        try:
            ans = int(input("Where would you like to save the files?\n"
                            "1 for current dir 2 for new dir: "))
        except ValueError:
            print('Not a valid input')
            continue

        if ans == 1 or ans == 2:
            break
        else:
            print('Not a valid input')

    if ans == 2:
        os.mkdir('quizzes')
        return Path.cwd() / Path('quizzes')
    else:
        return Path.cwd()


if __name__ == '__main__':
    main()
