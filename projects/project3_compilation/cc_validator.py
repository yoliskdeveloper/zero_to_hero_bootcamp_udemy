def validate(n):

    intArray = intToArray(n)

    if len(intArray) % 2 == 0:
        oddEven(0, intArray)
    else:
        oddEven(1, intArray)

    if sum(intArray) % 10 == 0:
        return True
    else:
        return False

def intToArray(n):
    myArray = str(n)

    intArray = []
    for x in myArray:
        intArray.append(int(x))

    return intArray

def oddEven(startIndex, intArray):
    for i in range(startIndex, len(intArray), 2):
        newDigit = intArray[i] * 2
        if newDigit < 20:
            intArray[i] = newDigit

        else:
            intArray[i] = sumOfDigits(newDigit)

def sumOfDigits(n):
    return (n / 10) + (n % 10)

v = validate(input('Masukkan no. CC untuk memvalidasi\r\n> '))
print(v)

