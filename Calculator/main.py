"""
    Yet another calculator
    Just to practise some python
"""


# add function
def add(var1, var2):
    return var1 + var2


# substract function
def sub(var1, var2):
    return var1 - var2


# multiply function
def mul(var1, var2):
    return var1 * var2


# divide function
def div(var1, var2):
    try:
        return var1 / var2
    # prevent error
    except ZeroDivisionError:
        return 0


def run(operation, var1, var2):
    # add
    if operation == 1 or operation == '+':
        # print('Formula: ', var1, '+', var2)
        print('Answer: ', add(var1, var2))
    # subtract
    elif operation == 2 or operation == '-':
        print('Answer: ', sub(var1, var2))
    # multiply
    elif operation == 3 or operation == '*':
        print('Answer: ', mul(var1, var2))
    # divide
    elif operation == 4 or operation == '/':
        print('Answer: ', div(var1, var2))
    else:
        print('Enter a valid operation')


def calculator():
    loop_start = True
    while loop_start:
        valid = False
        while not valid:
            # User input
            try:
                operation = int(input('What do you want to do:  1. Add, 2. substract, 3. multiply, 4. divide: '))
                var1 = int(input('Enter your first varber: '))
                var2 = int(input('Enter your second varber: '))
                valid = True
            except ValueError:
                print('Invalid input')
        run(operation, var1, var2)
        # continue loop
        close = input('Do you want to close the calculator [y/n]: ')
        if close == 'y':
            confirmation = input('Are you sure you want to close the calculator [y/n]: ')
            if confirmation == 'y':
                loop_start = False
            elif confirmation == 'n':
                print(100 * '-')
                continue
            else:
                loop_start = False
                print('Invalid input, closing calculator...')
                print(100 * '-')
        elif close == 'n':
            print(100 * '-')
            continue
        else:
            loop_start = False
            print('Invalid input, closing calculator...')
            print(100 * '-')


if __name__ == "__calculator__":
    calculator()
