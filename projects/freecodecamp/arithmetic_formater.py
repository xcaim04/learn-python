def arithmetic_arranger(problems, show_answer=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'
    first = ""
    second = ""
    lines = ""
    sumx = ""
    string = ""
    for problem in problems:
        l = problem.split()
        first_number = l[0]
        operator = l[1]
        second_number = l[2]

        if operator != "+" and operator != "-":
            return "Error: Operator must be '+' or '-'."
        elif not first_number.isdigit() or not second_number.isdigit():
            return 'Error: Numbers must only contain digits.'
        elif len(first_number) > 4 or len(second_number) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        sum = ""
        if operator == "+":
            sum = str(int(first_number) + int(second_number))
        else:
            sum = str(int(first_number) - int(second_number))

        length = max(len(first_number), len(second_number)) + 2
        top = str(first_number).rjust(length)
        bottom = operator + str(second_number).rjust(length - 1)
        line = ""
        res = str(sum).rjust(length)
        for s in range(length):
            line += "-"

        first += top + "    "
        second += bottom + "    "
        lines += line + "    "
        sumx += res + "    "

    if show_answer:
        string = first + "\n" + second + "\n" + lines + "\n" + sumx
    else:
        string = first + "\n" + second + "\n" + lines
    return string.rstrip()

arithmetic_solve = arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43"], True)
print(arithmetic_solve)