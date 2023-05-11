# optional programming exercise for fundamentals, week 6

def derive(coefficients, n):
    """Calculates nth derivatives of polynomial stored in coefficients."""
    # coeffs is dictionary as {order of x: coefficient}
    if n == 0:
        return coefficients
    else:
        results = {}
        for orders in coefficients:
            results[orders - 1] = orders * coefficients[orders]
        return derive(results, n-1)


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
            if elements[index+1][0] == '-':
                output_string += " - "
            else:
                output_string += " + "
    return output_string


def newton():
    pass


def main():
    degree = int(input("Enter degree of derivative: "))
    highest = int(input("Enter highest order: "))
    lowest = int(input("Enter lowest order: "))
    c = {}
    for i in range(highest, lowest - 1, -1):
        if i != 0:
            c[i] = int(input(f"Enter coefficient of x^{i}: "))
        else:
            c[i] = int(input("Enter constant: "))
    print("Result: " + derivative_to_string(derive(c, degree)))


main()