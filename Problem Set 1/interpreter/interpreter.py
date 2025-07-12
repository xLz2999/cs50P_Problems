x = input("Expression: ").strip().split()

match x[1] :
    case "+" :
        result = int(x[0]) + int(x[2])
        print(f"{result:.1f}" )
    case "-" :
        result = int(x[0]) - int(x[2])
        print(f"{result:.1f}" )
    case "*" :
        result = int(x[0]) * int(x[2])
        print(f"{result:.1f}" )
    case "/" :
        result = int(x[0]) / int(x[2])
        print(f"{result:.1f}" )
