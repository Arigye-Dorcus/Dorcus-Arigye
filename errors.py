def positive_number(a):
    try:
        if a < 0:
            raise ValueError("less than zero")
        return "is positive integer"
    except ValueError as e:
        print(e)
        print(positive_number(-1))