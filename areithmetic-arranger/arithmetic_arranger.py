import re

SpaceBetweenProblems = 4
Error = None

def validateProblemCount(problems):
    if len(problems) > 5:
        global Error 
        Error = "Error: Too many problems."


def validateOperation(operation):
    if operation == "+" or operation == "-" :
        return 
    else:
        global Error
        Error = "Error: Operator must be '+' or '-'."

def reportResults(formatedProblems):
    global Error
    if Error == None:
        return formatedProblems
    else:
        return Error

def maximumLenghtOfTwoString(aString, bString): 
    a = len(aString)
    b = len(bString)
    if a >= b: 
        return a 
    else: 
        return b 

def ValidateNumbers(numberArray):
    global Error
    for number in numberArray:
        if len(number) > 4:
            Error = "Error: Numbers cannot be more than four digits."
        elif re.search('[a-zA-Z]', number):
            Error = "Error: Numbers must only contain digits."

def chopUpProblems(problem, problemDictionary):
    global Error
    if Error is not None:
        return

    problem = str(problem)
    splitProblem = problem.split()

    operation = splitProblem[1]
    numberOne = splitProblem[0]
    numberTwo = splitProblem[2]

    ValidateNumbers([numberOne, numberTwo])
    if Error is not None:
        return

    validateOperation(operation)
    if Error is not None:
        return

    problemDictionary["firstNumbers"].append(numberOne)
    problemDictionary["secondNumbers"].append(numberTwo)
    problemDictionary["operations"].append(operation)

    formatLength = maximumLenghtOfTwoString(numberOne, numberTwo) + 2 # plus two. One for operation and one for a space
    problemDictionary["formatingLength"].append(formatLength)

def doMath(operation, firstNumber, secondNumber):
    a = int(firstNumber)
    b = int(secondNumber)
    if operation == "+":
        return a + b
    else:
        return a - b


def formatProblems(problemDictionary, showAnswers = False):
    printString = ""
    totalLenght = 0
    for problemFormatLength in problemDictionary["formatingLength"]:
        totalLenght = totalLenght + problemFormatLength + SpaceBetweenProblems
    totalLenght - SpaceBetweenProblems #clean up trailing space

    # Top Numbers
    index = 0
    for operation in problemDictionary["operations"]:
        singleProblemLength = problemDictionary["formatingLength"][index]
        firstNumber = problemDictionary["firstNumbers"][index]
        leadingSpacesNeeded = singleProblemLength - len(firstNumber)
        printString += ' ' * leadingSpacesNeeded
        printString += firstNumber
        printString += ' ' * SpaceBetweenProblems
        index += 1

    printString = printString[:-SpaceBetweenProblems] # to trim up tail of the problem
    printString += "\n"

    ## Operation and Bottom number 
    index = 0
    for operation in problemDictionary["operations"]:
        singleProblemLength = problemDictionary["formatingLength"][index]
        secondNumber = problemDictionary["secondNumbers"][index]
        leadingSpacesNeeded = singleProblemLength - len(secondNumber) - 1 # operation takes one space

        printString += operation
        printString += ' ' * leadingSpacesNeeded
        printString += secondNumber
        printString += ' ' * SpaceBetweenProblems
        index += 1

    printString = printString[:-SpaceBetweenProblems] # to trim up tail of the problem
    printString += "\n"

    # Dashes
    index = 0
    for operation in problemDictionary["operations"]:
        singleProblemLength = problemDictionary["formatingLength"][index]

        printString += "-" * singleProblemLength
        printString += " " * SpaceBetweenProblems
        index += 1
    printString = printString[:-SpaceBetweenProblems] # to trim up tail of the problem
        
    # Answer
    if showAnswers:
        printString += "\n"
        index = 0
        for operation in problemDictionary["operations"]:
            singleProblemLength = problemDictionary["formatingLength"][index]
            firstNumber = problemDictionary["firstNumbers"][index]
            secondNumber = problemDictionary["secondNumbers"][index]
            answer = str(doMath(operation, firstNumber, secondNumber))
            leadingSpacesNeeded = singleProblemLength - len(answer)

            printString += " " * leadingSpacesNeeded
            printString += answer
            printString += " " * SpaceBetweenProblems
            index += 1
        printString = printString[:-SpaceBetweenProblems] # to trim up tail of the problem        

    return printString




def arithmetic_arranger(problems, showAnswer = False):
    global Error 
    Error = None

    arranged_problems = ''
    validateProblemCount(problems)


    if Error is not None:
        return reportResults(arranged_problems)

    problemDictionary = { "firstNumbers": [], "secondNumbers": [], "operations": [], "formatingLength": [] }
    for problem in problems:
        chopUpProblems(problem, problemDictionary)

    arranged_problems = formatProblems(problemDictionary, showAnswer)

    return reportResults(arranged_problems)

