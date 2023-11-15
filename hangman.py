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

word_list = ['finger', 'back', 'knee']
display = []

select_word = random.choice(word_list)
end_of_game = False
lives = 6

for i in select_word:
    display += '_'
print(display)

while not end_of_game:

    select_letter = input('Enter letter: ').lower()

    for i in range(len(select_word)):
        index_letter = select_word[i]
        if index_letter == select_letter:
            display[i] = index_letter

    if select_letter not in select_word:
        lives -= 1
        print(f'You have lost one life. Your lives: {lives}')
        if lives == 0:
            end_of_game = True
            print('You lose')

    print(f"{' '.join(display)}")

    if '_' not in display:
        end_of_game = True
        print('You win')

    print(stages[lives])
