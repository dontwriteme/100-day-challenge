import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
 ========= 
 ''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
 ========= 
 ''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
 ========= 
 ''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
 ========= 
 ''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
 ========= 
  ''', '''
  +---+
  |   |
  O   |
      |
      |
      |
 ========= 
 ''', '''
  +---+
  |   |
      |
      |
      |
      |
 ========= 
 ''']

word_list = ['palm','brest','knuckle']

chosen_word = random.choice(word_list)

print(chosen_word)

blanks_list = []

for i in chosen_word:
    blanks_list += '_'

end_of_game = False
lives = 6

while not end_of_game:
 letter = input('Choose a letter: ').lower()

 for i in range(len(chosen_word)):
    index_letter = chosen_word[i]
    if index_letter == letter:
        blanks_list[i] = index_letter
    
 print(blanks_list)
 print(lives)

 if '_' not in blanks_list:
     end_of_game = True
     print('You win!')
