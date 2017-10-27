# Hunter Leise
# CSCI-3202 Problem Set 2
# Problem 4 (Mastermind Game)

import sys
from random import choice


class MastermindGame:
    def __init__(self):
        # Doesn't change, therefore it's better to hard code than use resources
        # and time to calculate it every single time
        self.options = ['rrr', 'rrb', 'rro', 'rrw', 'rbr', 'rbb', 'rbo', 'rbw', 'ror',
                        'rob', 'roo', 'row', 'rwr', 'rwb', 'rwo', 'rww', 'brr', 'brb',
                        'bro', 'brw', 'bbr', 'bbb', 'bbo', 'bbw', 'bor', 'bob', 'boo',
                        'bow', 'bwr', 'bwb', 'bwo', 'bww', 'orr', 'orb', 'oro', 'orw',
                        'obr', 'obb', 'obo', 'obw', 'oor', 'oob', 'ooo', 'oow', 'owr',
                        'owb', 'owo', 'oww', 'wrr', 'wrb', 'wro', 'wrw', 'wbr', 'wbb',
                        'wbo', 'wbw', 'wor', 'wob', 'woo', 'wow', 'wwr', 'wwb', 'wwo',
                        'www']

    # Engine to run through the game until the code is guessed
    def run_game(self):
        print("Think of a code composed of 'red', 'blue', 'orange', or 'white'.")
        print("The code should be 3 colors long and can have repeats.")
        input("Press Enter when you're ready to play")

        game_over = False

        while not game_over:
            guess = self.guess_code()

            response = self.get_user_response().lower()

            if response == "xxx":
                game_over = True
                print("Game over: your code was " + guess)
            else:
                self.options.remove(guess)
                self.update_options(guess, response)

    # Randomly guess code from the remaining options
    def guess_code(self):
        if len(self.options) == 0:
            print("Game over: No valid guesses, maybe you gave me a wrong response?")
            sys.exit()
        else:
            guess = choice(self.options)
            print("Guess: " + guess)
            return guess

    # Query the user for their response to the AI's guess
    # Xs should come before Os
    def get_user_response(self):
        response = input("Response: ").lower()
        if response != "" and 'x' not in response and 'o' not in response:
            print("Invalid response, try again")
            self.get_user_response()
        return response

    # Return a response given a guess and a code
    def get_response(self, code, guess):
        response = ""
        code_incorrect = ""
        guess_incorrect = ""
        for i in range(0, 3):  # Add Xs
            if code[i] == guess[i]:
                response += "x"
            else:
                code_incorrect += code[i]
                guess_incorrect += guess[i]

        for color in guess_incorrect:  # Add Os
            if color in code_incorrect:
                response += "o"
                code_incorrect = code_incorrect.replace(
                    code_incorrect[code_incorrect.index(color)], "")

        return response

    # Remove options that would not return the given response given a guess
    def update_options(self, guess, response):
        self.options = [code for code in self.options
                        if self.get_response(code, guess) == response]


if __name__ == "__main__":
    new_game = MastermindGame()
    new_game.run_game()
