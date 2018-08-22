from tkinter import *
from tkinter import ttk
import random

class rps:

    def __init__(self, root, uName):
        root.title('Rock, Paper, Scissor')
        root.geometry('500x100')
        root.resizable(width=False, height=False)
        root.iconbitmap('C:\Windows\System32\shell32.dll')
        frame = Frame(root)
        frame.pack()

        self.uName = uName
        self.uHand = 'N/A'
        self.bot = 'N/A'
        self.winner = 'No winner yet'
        self.score = 0
        self.games = 0
        print('New instance of game class for ' + self.uName)

        style = ttk.Style()
        style.configure('TButton', font='Serif 15', padding=10)

        """ 
            First row
            Name --- Score --- Total games
        """
        self.labelName = Label(frame, text='Player name: ' + self.uName)
        self.labelName.grid(row=0, column=1, sticky=W)
        self.labelScore = Label(frame, text='Total wins: ' + str(self.score))
        self.labelScore.grid(row=0, column=2, sticky=W)
        self.labelGames = Label(frame, text='Total Games: ' + str(self.games))
        self.labelGames.grid(row=0, column=3, sticky=W)

        """
            Second row
            Buttons
            Rock --- Paper --- Scissors
        """

        self.buttonR = ttk.Button(frame, text='Rock', command=lambda: self.btnclick('rock'))
        self.buttonR.grid(row=1, column=1, sticky=W)
        self.buttonP = ttk.Button(frame, text='Paper', command=lambda: self.btnclick('paper'))
        self.buttonP.grid(row=1, column=2, sticky=W)
        self.buttonS = ttk.Button(frame, text='Scissor', command=lambda: self.btnclick('scissors'))
        self.buttonS.grid(row=1, column=3, sticky=W)

        """
            Last row
            User hand --- Bot hand --- Winner
        """

        self.labelUser = Label(frame, text='You picked: ' + self.uHand)
        self.labelUser.grid(row=2, column=1, sticky=W)
        self.labelBot = Label(frame, text='CPU picked: ' + self.bot)
        self.labelBot.grid(row=2, column=2, sticky=W)
        self.labelWinner = Label(frame, text=self.winner)
        self.labelWinner.grid(row=2, column=3, sticky=W)

    def btnclick(self, value):
        self.uHand = value
        if self.uHand == 'rock' or self.uHand == 'paper' or self.uHand == 'scissors':
            print(100 * '-')
            print('You picked: ' + self.uHand.capitalize())
            self.labelUser['text'] = self.uHand.capitalize()
            self.bot = random.randint(0, 2)
        # Invalid value will reset
        else:
            # Can't put in another value
            print('Invalid input \n')

        if self.bot == 0:
            print('CPU picked: Rock')
            self.labelBot['text'] = 'Rock'
        elif self.bot == 1:
            print('CPU picked: Paper')
            self.labelBot['text'] = 'Paper'
        elif self.bot == 2:
            print('CPU picked: Scissors')
            self.labelBot['text'] = 'Scissors'

        # user won
        if (self.uHand == 'rock' and self.bot == 2) or \
                (self.uHand == 'paper' and self.bot == 0) or \
                (self.uHand == 'scissors') and self.bot == 1:
            self.winner = 'You won'
            self.score += 1
            self.games += 1
            self.labelScore['text'] = 'Total wins: ' + str(self.score)
            self.labelGames['text'] = 'Total Games: ' + str(self.games)
            self.labelWinner['text'] = self.winner
        # user lost
        elif (self.uHand == 'rock' and self.bot == 1) or \
                (self.uHand == 'paper' and self.bot == 2) or \
                (self.uHand == 'scissor' and self.bot == 0):
            self.winner = 'You lost'
            self.games += 1
            self.labelScore['text'] = 'Total wins: ' + str(self.score)
            self.labelGames['text'] = 'Total Games: ' + str(self.games)
            self.labelWinner['text'] = self.winner
        # user tied
        elif (self.uHand == 'rock' and self.bot == 0) or \
                (self.uHand == 'paper' and self.bot == 1) or \
                (self.uHand == 'scissors' and self.bot == 2):
            self.winner = 'Tie'
            self.games += 1
            self.labelScore['text'] = 'Total wins: ' + str(self.score)
            self.labelGames['text'] = 'Total Games: ' + str(self.games)
            self.labelWinner['text'] = self.winner
        else:
            print('Error')




def main():
    uName = input('What is your name?: ')
    x = rps(root, uName)
    # x.bot = random.randint(0, 2)

    root.mainloop()

root = Tk()
main()