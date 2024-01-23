while True:
    try:
        a=int(input("1st number"))
        b=int(input("2nd number"))
        print(a/b)
    except ZeroDivisionError:
        print("Zero cannot be divided.")
    except ValueError:
        print("Please only enter numbers value.")
    