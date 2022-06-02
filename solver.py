import itertools

OPERATORS = ["+", "-", "*", "/"]
DIGITS = "0123456789"
BRACKETS = "()"
template = ""

def genTemplate(length):
    global template
    template = ""
    bracketIndex = 0
    for i in range(length):
        template += "B{}".format(str(bracketIndex))
        bracketIndex += 1
        template += "N{}".format(str(i))
        template += "B{}".format(str(bracketIndex))
        bracketIndex += 1
        if i < length-1:
            template += "O{}".format(str(i))

def format(numbers, brackets, operators):
    expression = template
    for i in range(len(brackets)):
        expression = expression.replace("B{}".format(str(i)), brackets[i])

    for i in range(len(numbers)):
        expression = expression.replace("N{}".format(str(i)), str(numbers[i]))
        if i < len(numbers)-1:
            expression = expression.replace("O{}".format(str(i)), operators[i])

    valid = True
    for i in range(len(expression)-1):
        current = expression[i]
        if current in DIGITS and expression[i+1] == "(":
            valid = False
            break
        if current == ")" and expression[i+1] in DIGITS:
            valid = False
            break

        if current in OPERATORS and expression[i+1] == ")":
            valid = False
            break
        if current == "(" and expression[i+1] in OPERATORS:
            valid = False
            break

    if valid:
        return expression

def getBracketCombinations(length):
    brackets = [[""] * length * 2]
    possibleBrackets = [""] * length * 2
    for i in range(0, len(possibleBrackets), 2):
        possibleBrackets[i] = "("
        possibleBrackets[i+1] = ")"
        for combination in list(itertools.permutations(possibleBrackets)):
            valid = True
            layers = 0
            for part in list(combination):
                if part == "(":
                    layers += 1
                elif part == ")":
                    layers -= 1

                if layers < 0:
                    valid = False
                    break
            
            if not valid:
                continue

            for i in range(len(combination)-1):
                if combination[i] == "(" and combination[i+1] == ")":
                    valid = False
                    break

            if valid and not list(combination) in brackets:
                brackets.append(list(combination))

    return brackets
def getOperatorCombinations(length):
    combinations = []
    for combination in list(itertools.product(OPERATORS, repeat=length-1)):
        combinations.append(list(combination))
    return combinations


def solve(numbers):
    operators = getOperatorCombinations(len(numbers))
    permutations = list(itertools.permutations(numbers))
    brackets = getBracketCombinations(len(numbers))

    genTemplate(len(numbers))

    possibilities = []
    for i in range(len(permutations)):
        for j in range(len(brackets)):
            for k in range(len(operators)):
                expression = format(permutations[i], brackets[j], operators[k])
                if expression is not None:
                    possibilities.append(expression)

    solutions = []
    for expression in possibilities:
        try:
            if eval(expression) == 24:
                solutions.append(expression)
        except:
            continue

    if len(solutions) == 0:
        return "No solution"
    
    best = "                              "
    for solution in solutions:
        if len(solution) < len(best):
            best = solution

    return best