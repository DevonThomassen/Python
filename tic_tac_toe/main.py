from tkinter import *
from tkinter import ttk
import random


class game:

    def __init__(self, root, uName, uSymbol):
        # Settings
        root.title('Tic Tac Toe')
        root.geometry('500x300')
        root.resizable(width=False, height=False)
        root.iconbitmap('C:\Windows\System32\shell32.dll')
        frame = Frame(root)
        frame.pack()

        # Vars
        self.uName = uName
        self.uSymbol = uSymbol.capitalize()
        if uSymbol.lower() == 'x':
            self.bot = 'O'
        else:
            self.bot = 'X'
        self.wins = 0
        self.games = 0
        self.arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        print('Opening window...')

        # Style
        style = ttk.Style()
        style.configure('TButton', font='Serif 15', padding=10)

        # UI
        """ Labels """
        self.label1 = Label(frame, text='Playername: ' + self.uName)
        self.label1.grid(row=1, column=1, columnspan=3, sticky=W)
        self.label2 = Label(frame, text='Player symbol: ' + self.uSymbol)
        self.label2.grid(row=2, column=1, columnspan=3, sticky=W)
        self.label3 = Label(frame, text='Total Wins: ' + str(self.wins))
        self.label3.grid(row=3, column=1, columnspan=3, sticky=W)
        self.label4 = Label(frame, text='Total Games: ' + str(self.games))
        self.label4.grid(row=4, column=1, columnspan=3, sticky=W)

        """ First row of buttons """

        self.button1 = ttk.Button(frame, command=lambda: self.changeValue('1'))
        self.button1.grid(row=5, column=1, sticky=W)
        self.button2 = ttk.Button(frame, command=lambda: self.changeValue('2'))
        self.button2.grid(row=5, column=2, sticky=W)
        self.button3 = ttk.Button(frame, command=lambda: self.changeValue('3'))
        self.button3.grid(row=5, column=3, sticky=W)

        """ Second row of buttons """

        self.button4 = ttk.Button(frame, command=lambda: self.changeValue('4'))
        self.button4.grid(row=6, column=1, sticky=W)
        self.button5 = ttk.Button(frame, command=lambda: self.changeValue('5'))
        self.button5.grid(row=6, column=2, sticky=W)
        self.button6 = ttk.Button(frame, command=lambda: self.changeValue('6'))
        self.button6.grid(row=6, column=3, sticky=W)

        """ Last row of buttons """

        self.button7 = ttk.Button(frame, command=lambda: self.changeValue('7'))
        self.button7.grid(row=7, column=1, sticky=W)
        self.button8 = ttk.Button(frame, command=lambda: self.changeValue('8'))
        self.button8.grid(row=7, column=2, sticky=W)
        self.button9 = ttk.Button(frame, command=lambda: self.changeValue('9'))
        self.button9.grid(row=7, column=3, sticky=W)
        t = '                        Start over again                       '  # Im lazy (:
        self.button10 = ttk.Button(frame, text=t, command=lambda: self.r())
        self.button10.grid(row=8, column=1, columnspan=3, sticky=W)

    def changeValue(self, number):
        number = int(number)
        print(number)
        y = 'self.button' + str(number) + '[\'text\'] = self.uSymbol'
        z = 'self.button' + str(number) + '[\'state\'] = \'disabled\''
        exec(y)
        exec(z)

        self.autoBot(number)
        self.w()

    def w(self):
        s = ['X', 'O']
        for v in s:
            """
                3 rows horizontal
                3 vertical
                2 diagonal
            """
            if self.button1['text'] == v and self.button2['text'] == v and self.button3['text'] == v or \
                    self.button4['text'] == v and self.button5['text'] == v and self.button6['text'] == v or \
                    self.button7['text'] == v and self.button8['text'] == v and self.button9['text'] == v or \
                    self.button1['text'] == v and self.button4['text'] == v and self.button7['text'] == v or \
                    self.button2['text'] == v and self.button5['text'] == v and self.button8['text'] == v or \
                    self.button3['text'] == v and self.button6['text'] == v and self.button9['text'] == v or \
                    self.button1['text'] == v and self.button5['text'] == v and self.button9['text'] == v or \
                    self.button3['text'] == v and self.button5['text'] == v and self.button7['text'] == v:
                popup = Tk()
                print('v=' + v)
                if self.uSymbol == v:
                    popup.title('You won!')
                    self.labelWin = ttk.Label(popup, text='You won!')
                    self.wins += 1
                else:
                    popup.title('You lost!')
                    self.labelWin = ttk.Label(popup, text='You lost!')
                popup.geometry('50x50')
                style = ttk.Style()
                style.configure('S.Label', font='Serif 50')
                self.labelWin.grid()

                for i in range(1, 10):
                    j = 'self.button' + str(i) + '[\'state\'] = \'disabled\''
                    exec(j)

    def r(self):
        # doesn't work
        self.games += 1
        print('Starting over')
        for i in range(1, 10):
            j = 'self.button' + str(i) + '[\'state\'] = \'enable\''
            k = 'self.button' + str(i) + '[\'text\'] = \'\''
            exec(j)
            exec(k)
        self.arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def autoBot(self, number):
        self.botControl(number)
        x = number - 1
        print('number = ' + str(number))
        print('x = ' + str(x))

    def botControl(self, number):
        # user tile
        self.arr.remove(number)
        botNumber = random.choice(self.arr)
        e = 'self.button' + str(botNumber) + '[\'state\'] = \'disabled\''
        f = 'self.button' + str(botNumber) + '[\'text\'] = self.bot'
        exec(e)
        exec(f)
        # bot tile
        self.arr.remove(botNumber)
        print('bot=' + str(botNumber))
        print('arr=' + str(self.arr))


def main():
    uName = input('What is your name?: ')
    uSymbol = input('Do you want to be X or O: ')
    if uSymbol.lower() == 'x' or uSymbol.lower() == 'o':
        x = game(root, uName, uSymbol)
        root.mainloop()
    else:
        print('Invalid')
        main()


root = Tk()
main()
