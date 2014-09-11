import testFunc

def main():
    variable1 = testFunc.getValue()
    variable2 = testFunc.getValue()
    if testFunc.validateValue(variable1) and testFunc.validateValue(variable2):
        print("Objects verified as type integer")
    else:
        print("ERROR!")
    print("The area is:", testFunc.findArea(variable1, variable2))

if __name__ == "__main__":
    main()

