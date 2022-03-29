def swapnumbers():
    number1 = int(input(" Input First Number : "))
    number2 = int(input(" Input Second Number : "))
    print("Before Swapping: ",(number1, number2))
    # making sure that the inputs stay in order
    if number1 > number2:
        temp = number1
        number1 = number2
        number2 = temp

    print("After Swapping:",(number1, number2))


if __name__ == "__main__":
    swapnumbers()