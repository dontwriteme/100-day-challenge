import random

stages = ['''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
========== 
''', '''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
========== 
''', '''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
==========
''', '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
========== 
''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
========== 
''', '''
    +---+
    |   |
    O   |
        |
        |
        |
========== 
''', '''
    +---+
    |   |
        |
        |
        |
        |
========== ''']

word_list = ['breast', 'chin', 'shoulder']
chosen_word = random.choice(word_list)

display = []
for i in chosen_word:
    display += '_'
print(display)

end_of_game = 0
lives = 6

while end_of_game == 0:
    selected_letter = input('Select a letter: ').lower()

    for i in range(len(chosen_word)):
        index_letter = chosen_word[i]

        if index_letter == selected_letter:
            display[i] = index_letter
    print(display)

    if selected_letter not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = 1
        print(f'Lose one live! You have {lives} lives')

    if '_' not in display:
        end_game = 1
        print('You win!')

    print(stages[lives])
