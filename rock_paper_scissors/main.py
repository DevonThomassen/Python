class Game:
    def __init__(self, newuName):
        self.uName = newuName
        self.uHand = 'N/A'
        self.bot = 'N/A'
        self.winner = 'No winner yet'
        print('New instance of game class for ' + self.uName)

    def runGame(self):
        # from termcolor import colored
        self.uHand = input('Rock, Paper, Scissors: ').lower()  # Avoid case sensitivity
        if self.uHand == 'rock' or self.uHand == 'paper' or self.uHand == 'scissors':
            print(100 * '-')
            print('You have pick: ' + self.uHand.capitalize())
        # Invalid value will reset
        else:
            print('Invalid input \n')
            main()
        if self.bot == 0:
            print('CPU picked: Rock')
        elif self.bot == 1:
            print('CPU picked: Paper')
        elif self.bot == 2:
            print('CPU picked: Scissors')
        # user won
        if (self.uHand == 'rock' and self.bot == 2) or \
                (self.uHand == 'paper' and self.bot == 0) or \
                (self.uHand == 'scissors') and self.bot == 1:
            self.winner = 'You won'
        # user lost
        elif (self.uHand == 'rock' and self.bot == 1) or \
                (self.uHand == 'paper' and self.bot == 2) or \
                (self.uHand == 'scissor' and self.bot == 0):
            self.winner = 'You lost'
        # user tied
        elif (self.uHand == 'rock' and self.bot == 0) or \
                (self.uHand == 'paper' and self.bot == 1) or \
                (self.uHand == 'scissors' and self.bot == 2):
            self.winner = 'Tie'
        else:
            print('Error')


def main():
    import random

    myGame = Game(input("Select your name: "))

    myGame.bot = random.randint(0, 2)

    myGame.runGame()
    print(myGame.winner)


main()
