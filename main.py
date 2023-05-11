# optional programming exercise for fundamentals, week 6

def derive(coeffs):
    # coeffs is dictionary as {order of x: coefficient}
    results = {}
    for orders in coeffs:
        results[orders - 1] = orders * coeffs[orders]
    return results


def newton():
    pass


def main():
    highest = int(input("Enter highest order: "))
    lowest = int(input("Enter lowest order: "))
    c = {}
    for i in range(highest, lowest - 1, -1):
        c[i] = int(input(f"Enter coefficient of x^{i}."))
    derivative = derive(c)
    print("Result:")
    result = []
    for i in derivative:
        result.append(f"{derivative[i]}x^{i}")
    print(" + ".join(result))

main()