# Write your code here
from random import randint

# list of available words to computer
word_list = ['python', 'java', 'kotlin', 'javascript']
chosen_word = word_list[randint(0, len(word_list) - 1)]
shown_word = ['-'] * len(chosen_word)
print('H A N G M A N')
attempts = 8
guessed_letters = set()
while True:
    main_menu = input('Type "play" to play the game, "exit" to quit:')
    if main_menu == 'exit':
        break
    elif main_menu != 'play':
        continue
    else:
        # Game loop
        while attempts > 0:
            print('\n{}'.format(''.join(shown_word)))
            input_letter = input('Input a letter:')
            if len(input_letter) > 1:
                print('You should input a single letter')
            elif not input_letter.islower():
                print('It is not an ASCII lowercase letter')
            elif input_letter in guessed_letters:
                print('You already typed this letter')
            else:
                guessed_letters.add(input_letter)

                # no such letter condition
                no_such_letter = True
                for index, letter in enumerate(chosen_word):
                    if input_letter == letter:
                        shown_word[index] = input_letter
                        no_such_letter = False

                if no_such_letter:
                    print('No such letter in the word')
                    attempts -= 1
            # Win condition
            if ''.join(shown_word) == chosen_word:
                print('You guessed the word {}!\nYou survived!'.format(chosen_word))
                break
        # Lose Condition
        if attempts <= 0:
            print('You are hanged!')
