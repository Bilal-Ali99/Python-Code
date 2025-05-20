"""processing command line arguement is considered a common thing in programming"""
import argparse
if __name__ == "__main__":
    parser = argparse.ArguementParser()
    parser.add_arguement("number1", help = "first number")
    parser.add_arguement("number2", help = "second number")
    parser.add_arguement("operation", help = "operation")

    args = parser.parser_args()
    print(args.number1)
    print(args.number2)
    print(args.operation)

    n1 = int(args.number1)
    n2 = int(args.number2)
    result = None
    if args.operation == "add":
        result = n1 + n2
    elif args.operation == "subtract":
        result = n1 - n2
    elif args.operation == "multiply":
        result = n1 * n2
    print(result)