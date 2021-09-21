from random import choice
import string
import sys


class Game:

    def __init__(self):
        self.answers = []
        self.word = list(choice(['python', 'java', 'kotlin', 'javascript']))
        self.hint = ['-' for _ in range(len(self.word))]
        self.tries = 8

    def player_wins(self):
        return self.hint == self.word

    def check_letter(self, letter):
        if letter in set(self.word) and letter not in self.hint and len(letter) == 1 and letter in string.ascii_lowercase:
            for index, char in enumerate(self.hint):
                if self.word[index] == letter:
                    self.hint[index] = letter
        elif len(letter) != 1:
            print('You should input a single letter')
        elif letter not in string.ascii_lowercase:
            print('Please enter a lowercase English letter')
        elif letter in self.answers:
            print('You\'ve already guessed this letter')
        else:
            print('That letter doesn\'t appear in the word')
            self.tries -= 1
        if letter not in self.answers:
            self.answers.append(letter)

    def reset(self):
        self.answers.clear()
        self.word = list(choice(['python', 'java', 'kotlin', 'javascript']))
        self.hint.clear()
        self.hint = ['-' for _ in range(len(self.word))]
        self.tries = 8


def main():
    game = Game()
    print("H A N G M A N")
    user_choice = input('Type "play" to play the game, "exit" to quit: ')
    while user_choice not in ['play', 'exit']:
        user_choice = input('Type "play" to play the game, "exit" to quit: ')
    if user_choice.lower() == 'play':
        while True:
            print()
            print(''.join(game.hint))
            game.check_letter(input('Input a letter: >\n'))
            if game.player_wins():
                print('You guessed the word!\nYou survived!\n')
                game.reset()
                break
            elif not game.tries:
                print("You lost!\n")
                game.reset()
                break
    elif user_choice.lower() == 'exit':
        sys.exit()


if __name__ == '__main__':
    main()
