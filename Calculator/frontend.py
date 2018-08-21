from tkinter import *
from tkinter import ttk


# Not the final version of the calculator
class Calculator:
    calcValue = 0.0

    div_trigger = False
    mul_trigger = False
    add_trigger = False
    sub_trigger = False

    def btnClick(self, value):
        print(value)
        counter = 0
        displayValue = self.inputDisplay.get()

        displayValue += value

        self.inputDisplay.delete(0, 'end')

        self.inputDisplay.insert(0, displayValue)

    def isFloat(self, str_val):
        try:
            float(str_val)
            return True
        except ValueError:
            return False

    def mathButton(self, value):
        if self.isFloat(str(self.inputDisplay.get())):
            self.div_trigger = False
            self.mul_trigger = False
            self.add_trigger = False
            self.sub_trigger = False

            self.calcValue = float(self.inputDisplay.get())

            if value == '/':
                print('/')
                self.div_trigger = True
            elif value == '*':
                print('*')
                self.mul_trigger = True
            elif value == '+':
                print('+')
                self.add_trigger = True
            elif value == '-':
                print('-')
                self.sub_trigger = True

            self.inputDisplay.delete(0, 'end')

    def equalButton(self):
        if self.add_trigger or self.sub_trigger or self.mul_trigger or self.div_trigger:
            if self.add_trigger:
                solution = self.calcValue + float(self.inputValue.get())
            elif self.sub_trigger:
                solution = self.calcValue - float(self.inputValue.get())
            elif self.mul_trigger:
                solution = self.calcValue * float(self.inputValue.get())
            elif self.div_trigger:
                solution = self.calcValue / float(self.inputValue.get())

            print(self.calcValue, '', float(self.inputDisplay.get()), '', solution)
            self.inputDisplay.delete(0, 'end')
            self.inputDisplay.insert(0, solution)

    def __init__(self, root):
        root.title('Calculator')
        root.geometry('600x400')
        root.resizable(width=False, height=False)
        root.iconbitmap('C:\Windows\System32\shell32.dll')
        frame = Frame(root)
        frame.pack()

        operator = ''

        style = ttk.Style()
        style.configure('TButton', font='Serif 15', padding=10)
        style.configure('TEntry', font='Serif 18', padding=10)

        self.inputValue = StringVar(root, value='')
        self.inputDisplay = ttk.Entry(frame, textvariable=self.inputValue, width=50)
        self.inputDisplay.grid(row=0, columnspan=4)

        """SET 1"""

        self.buttonCE = ttk.Button(frame, text='CE', command=lambda: self.printMessage)
        self.buttonCE.grid(row=1, column=1, sticky=W)
        self.buttonC = ttk.Button(frame, text='C', command=lambda: self.printMessage)
        self.buttonC.grid(row=1, column=2, sticky=W)
        self.buttonDelete = ttk.Button(frame, text='<', command=lambda: self.printMessage)
        self.buttonDelete.grid(row=1, column=3, sticky=W)
        self.buttonDiv = ttk.Button(frame, text='/', command=lambda: self.mathButton('/'))
        self.buttonDiv.grid(row=1, column=4, sticky=W)

        """SET 2"""

        self.button7 = ttk.Button(frame, text='7', command=lambda: self.btnClick('7'))
        self.button7.grid(row=2, column=1, sticky=W)
        self.button8 = ttk.Button(frame, text='8', command=lambda: self.btnClick('8'))
        self.button8.grid(row=2, column=2, sticky=W)
        self.button9 = ttk.Button(frame, text='9', command=lambda: self.btnClick('9'))
        self.button9.grid(row=2, column=3, sticky=W)
        self.buttonMul = ttk.Button(frame, text='*', command=lambda: self.mathButton('*'))
        self.buttonMul.grid(row=2, column=4, sticky=W)

        """SET 3"""

        self.button4 = ttk.Button(frame, text='4', command=lambda: self.btnClick('4'))
        self.button4.grid(row=3, column=1, sticky=W)
        self.button5 = ttk.Button(frame, text='5', command=lambda: self.btnClick('5'))
        self.button5.grid(row=3, column=2, sticky=W)
        self.button6 = ttk.Button(frame, text='6', command=lambda: self.btnClick('6'))
        self.button6.grid(row=3, column=3, sticky=W)
        self.buttonSub = ttk.Button(frame, text='-', command=lambda: self.mathButton('-'))
        self.buttonSub.grid(row=3, column=4, sticky=W)

        """"SET 4"""

        self.button1 = ttk.Button(frame, text='1', command=lambda: self.btnClick('1'))
        self.button1.grid(row=4, column=1, sticky=W)
        self.button2 = ttk.Button(frame, text='2', command=lambda: self.btnClick('2'))
        self.button2.grid(row=4, column=2, sticky=W)
        self.button3 = ttk.Button(frame, text='3', command=lambda: self.btnClick('3'))
        self.button3.grid(row=4, column=3, sticky=W)
        self.buttonAdd = ttk.Button(frame, text='+', command=lambda: self.mathButton('+'))
        self.buttonAdd.grid(row=4, column=4, sticky=W)

        """SET 5"""

        self.button0 = ttk.Button(frame, text='0', command=lambda: self.btnClick('0'))
        self.button0.grid(row=5, column=1, columnspan=2, sticky=W)
        self.buttonDot = ttk.Button(frame, text='.', command=lambda: self.btnClick('.'))
        self.buttonDot.grid(row=5, column=3, sticky=W)
        self.buttonEnter = ttk.Button(frame, text='Enter', command=lambda: self.equalButton())
        self.buttonEnter.grid(row=5, column=4, sticky=W)

        # self.quitButton = Button(frame, text='Quit', command=frame.quit)
        # self.quitButton.pack(row=10, sticky=W)


root = Tk()

d = Calculator(root)

root.mainloop()
# =============================================================
# ==================Back-up for improvements===================
# =============================================================
