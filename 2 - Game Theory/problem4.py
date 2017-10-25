# Hunter Leise
# CSCI-3202 Problem Set 2
# Problem 4 (Mastermind Game)


class MastermindGame:
    def __init__(self):
        self.colors = ["red", "blue", "orange", "white"]
        self.board = ["", "", "", ""]
        self.model = []

    def run_game(self):
        print("Think of a code composed of 'red', 'blue', 'orange', or 'white' with a length of 3")
        input("Press Enter when you're ready to play")
        while True:
            guess = self.guess_code()
            response = self.get_response()

            if response == "xxx":
                return False
            else:
                self.update_model(guess, response)
                return True

    def guess_code(self):
        print("rbo")
        return "rbo"

    def get_response(self):
        response = input("Response: ").lower()
        if response != "" and 'x' not in response and 'o' not in response:
            print("Invalid response, try again")
            self.get_response()
        return response

    def update_model(self, guess, response):
        return

if __name__ == "__main__":
    new_game = MastermindGame()
    new_game.run_game()
