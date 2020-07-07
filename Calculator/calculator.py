def presentResults(result):
    print('-- The result is:', result)
    print('-------------')


def add(x, y):
    result = int(x) + int(y)
    presentResults(result)


def subtract(x, y):
    result = int(x) - int(y)
    presentResults(result)


def multiply(x, y):
    result = int(x) * int(y)
    presentResults(result)


def divide(x, y):
    result = float(x) / float(y)
    presentResults(result)


def execute_operation(oper):
    try:
        oper(input('1st number: '), input('2nd number: '))
    except ValueError:
        print('-----')
        print('Please type only numbers')
        print('-----')


calculating = True
operations = ['add', 'sum', 'subtract',
              'subtraction', 'multiply', 'divide', 'mult']
while calculating:
    print('>>> Select operation type:')
    print('---- sum')
    print('---- subtract')
    print('---- multiply')
    print('---- divide')
    print('-- exit program')
    userChoice = input('Waiting for input... ')
    if userChoice not in operations:
        print('-----')
        print(
            f'Sorry, the option {userChoice}, is not available. Try something else.')
        print('-----')
    print('-----')
    print(f'> {userChoice} operation')
    print('-----')
    if userChoice == 'sum' or userChoice == 'add':
        execute_operation(add)
    elif userChoice == 'multiply' or userChoice == 'mult':
        execute_operation(multiply)
    elif userChoice == 'divide' or userChoice == 'division':
        execute_operation(divide)
    elif userChoice == 'subtract' or userChoice == 'subtraction':
        execute_operation(subtract)
    elif userChoice == 'exit program' or userChoice == 'exit':
        calculating = False
