# Hunter Leise
# CSCI-3202 Problem Set 2
# Problem 4 (Mastermind Game)

import sys
from random import choice


class MastermindGame:
    def __init__(self):
        self.options = ['rrr', 'rrb', 'rro', 'rrw', 'rbr', 'rbb', 'rbo', 'rbw', 'ror', 'rob', 'roo', 'row', 'rwr', 'rwb', 'rwo', 'rww', 'brr', 'brb', 'bro', 'brw', 'bbr', 'bbb', 'bbo', 'bbw', 'bor', 'bob', 'boo', 'bow', 'bwr', 'bwb', 'bwo', 'bww', 'orr', 'orb', 'oro', 'orw', 'obr', 'obb', 'obo', 'obw', 'oor', 'oob', 'ooo', 'oow', 'owr', 'owb', 'owo', 'oww', 'wrr', 'wrb', 'wro', 'wrw', 'wbr', 'wbb', 'wbo', 'wbw', 'wor', 'wob', 'woo', 'wow', 'wwr', 'wwb', 'wwo', 'www']

    def run_game(self):
        print("Think of a code composed of 'red', 'blue', 'orange', or 'white' with a length of 3")
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

    def guess_code(self):
        if len(self.options) == 0:
            print("Game over: No valid guesses, maybe you gave me a wrong response?")
            sys.exit()
        else:
            guess = choice(self.options)
            print("Guess: " + guess)
            return guess

    def get_user_response(self):
        response = input("Response: ").lower()
        if response != "" and 'x' not in response and 'o' not in response:
            print("Invalid response, try again")
            self.get_response()
        return response

    def get_response(self, code, guess):
        response = ""
        correct = ""
        not_correct = ""
        for i in range(0, 3):
            if code[i] == guess[i]:
                response += "x"
                correct += guess[i]
            else:
                not_correct += guess[i]

        for color in not_correct:
            # Look out for repeats of colors that already have o's
            if (color in code) and (color not in correct):
                response += "o"

        return response

    def update_options(self, guess, response):
        for code in self.options:
            if self.get_response(code, guess) != response:
                self.options.remove(code)
        return


if __name__ == "__main__":
    new_game = MastermindGame()
    new_game.run_game()
