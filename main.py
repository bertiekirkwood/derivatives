# optional programming exercise for fundamentals, week 6

def calc(function, x):
    result = 0
    for order, coeff in function.items():
        result += coeff * (x ** order)
    return result


def derive(coefficients, n):
    """Calculates nth derivatives of polynomial stored in coefficients."""
    # coeffs is dictionary as {order of x: coefficient}
    if n == 0:
        return coefficients
    else:
        results = {}
        for order, coeff in coefficients.items():
            results[order - 1] = order * coeff
        return derive(results, n - 1)


def derivative_to_string(coefficients):
    # takes dict format of derivative and outputs string
    elements = []
    for i in coefficients:
        if coefficients[i] != 0:
            if coefficients[i] == 1 and i != 0:
                elements.append(f"x^{i}")
            else:
                if i == 0:
                    elements.append(str(coefficients[i]))
                elif i == 1:
                    elements.append(f"{coefficients[i]}x")
                else:
                    elements.append(f"{coefficients[i]}x^{i}")

    output_string = ""
    for index, x in enumerate(elements):
        if x[0] == '-':
            output_string += x[1:]
        else:
            output_string += x
        if index < len(elements) - 1:
            if elements[index + 1][0] == '-':
                output_string += " - "
            else:
                output_string += " + "
    return output_string


def newton(f, fdash, dp, x_log=None, iterations=0):
    """Repeats Newton's algorithm until accuracy to specified number of decimal places found."""
    if x_log is None:
        x_log = [0.0, 1.0]

    if round(x_log[-1], dp) == round(x_log[-2], dp):
        return round(x_log[-1], dp), iterations
    else:
        next_x = x_log[-1] - (calc(f, x_log[-1]) / calc(fdash, x_log[-1]))
        x_log.append(next_x)
        return newton(f, fdash, dp, x_log=x_log, iterations=iterations+1)


def get_function():
    highest = int(input("Enter highest order: "))
    lowest = int(input("Enter lowest order: "))
    c = {}
    for i in range(highest, lowest - 1, -1):
        if i != 0:
            c[i] = int(input(f"Enter coefficient of x^{i}: "))
        else:
            c[i] = int(input("Enter constant: "))
    return c


def main():
    # standard derivative calculations:
    # degree = int(input("Enter degree of derivative: "))
    # c = get_function()
    # print("Result: " + derivative_to_string(derive(c, degree)))

    # newton's thing
    # func = get_function()
    # f_dash = derive(func, 1)
    # dp = int(input("Enter desired accuracy: "))
    func = {3: 1, 2: -3, 0: 2}
    for i in range(20):
        result, iterations = newton(func, derive(func, 1), i, x_log=[0.0, 100.0])
        print(result)
        print(f"Took {iterations} iterations.")


main()
