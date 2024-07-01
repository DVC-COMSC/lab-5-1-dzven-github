def getinput():
    # ******************************
    # Make your Code
    # ******************************
    num = int(input("Please enter numeric value: "))
    return num

def getsum(v1, v2):
    # ******************************
    # Make your Code
    # ******************************
    return v1 + v2

def printval(v1, v2, total):
    # ******************************
    # Make your Code
    # ******************************
    print('Input')
    print(v1)
    print(v2)
    print('Output')
    print(total)

def main():
    userval1 = getinput()
    userval2 = getinput()
    total = getsum(userval1, userval2)
    printval(userval1, userval2, total)


if __name__ == '__main__':
    main()
