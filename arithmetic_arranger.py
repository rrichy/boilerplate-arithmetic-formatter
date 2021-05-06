def arithmetic_arranger(problems, answer = False):
    if len(problems) > 5: return "Error: Too many problems."
    operand_1, operand_2, dash, answers = [], [], [], []
    for problem in problems:
        num1, op, num2 = problem.split()
        test1, test2 = 0, 0
        if op != "+" and op != "-": return "Error: Operator must be '+' or '-'."
        try:
            test1 = int(num1)
            test2 = int(num2)
        except:
            return "Error: Numbers must only contain digits."
        if test1 > 9999 or test2 > 9999 or test1 < 0 or test2 < 0: return "Error: Numbers cannot be more than four digits."

        width = len(str(max(test1, test2)))
        operand_1.append("  " + (num1 if len(num1) == width else " "*(width - len(num1)) + num1))
        operand_2.append(op + " " + (num2 if len(num2) == width else " "*(width - len(num2)) + num2))
        dash.append("-"*(width + 2))
        if answer:
            sol = str(test1 + test2 if op == '+' else test1 - test2)
            answers.append(" "*(width + 2 - len(sol)) + sol)
    return "    ".join(operand_1) + "\n" + "    ".join(operand_2) + "\n" + "    ".join(dash) + ("\n" + "    ".join(answers) if answer == True else "")