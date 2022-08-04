class FormulaError(Exception):
    pass


def repl():
    while True:
        try:
            user_input = input(">>>")
            if user_input == "quit":
                print("Bye")
                break
            else:
                print(evaluate_formula(user_input))
        except FormulaError as e:
            print(f"Error: {e}")


def evaluate_formula(user_input):
    tokens = user_input.split(" ")
    if len(tokens) != 3:
        raise FormulaError("Malformed formula")

    try:
        operand1 = float(tokens[0])
        operand2 = float(tokens[2])
    except ValueError as e:
        raise FormulaError("Could not parse operands") from e

    operator = tokens[1]
    if operator == "+":
        return operand1 + operand2
    elif operator == "-":
        return operand1 - operand2
    elif operator == "*":
        return operand1 * operand2
    elif operator == "/":
        return operand1 / operand2
    else:
        raise FormulaError("Unknown operator")


if __name__ == "__main__":
    print("Welcome to the  interactive calculator!")
    print("Type 'quit' to exit")
    print("please don't forgot to use spacing between operands for ex. >>>5 + 3")
    repl()
