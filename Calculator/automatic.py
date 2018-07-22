import random

import main

loopMax = random.randint(0, 10)

print('Request for ' + str(loopMax) + ' maths received')

operations = ['+', '-', '*', '/']
# add new operation with operations.append('value')

print('Operations count ' + str(len(operations)))
print('Computer will maths using the following operations ' + str(operations))
print('\n\n')

for i in range(loopMax):
    var1 = random.randint(-99, 99)
    var2 = random.randint(-99, 99)

    # print('Numbers used ' + str(var1) + ' and ' + str(var2))

    # for operation in operations:
    #     print('operation = ' + operation)
    #     main.run(operation, var1, var2)
    #     print()
    #
    # print('\n')

    for i in range(len(operations)):
        print('index = ' + str(i))
        print('Formula: ' + str(var1) + ' ' + operations[i] + ' ' + str(var2))
        main.run(operations[i], var1, var2)
        print('\n' + 100 * '-' + '\n')

    print('\n' + 100 * '-' + '\n')

print('Done')
