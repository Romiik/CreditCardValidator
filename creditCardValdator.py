def main():
    while True:
        try:
            creditCardNumber = int(
                input('Enter the 16-digit Card number you would like to check : '))
        except:
            print('Please Specify Correct Input')
        else:
            if len(str(creditCardNumber)) == 16:
                break
            else:
                print('Please Enter correct 16 digit Number')
    check(creditCardNumber)


def check(creditCardNumber):
    sum = 0
    itr = 0
    string = str(creditCardNumber)
    accountIdentifier = int(string[-1])
    print('accountIdentifier----->{}'.format(accountIdentifier))
    creditCardNumber = int(string[:len(string)-1:])
    print('New Credit card Number -----> {}'.format(creditCardNumber))
    while creditCardNumber != 0:
        number = creditCardNumber % 10
        sum = sum + operation(number, itr)
        creditCardNumber = creditCardNumber / 10
        itr += 1
    print(sum)
    finalSum = sum + accountIdentifier
    finalCheck(finalSum)


def operation(number, itr):
    if itr % 2 == 0:
        a = number * 2
        if len(str(a)) == 2:
            final = 0
            for x in range(2):
                number = a % 10
                final += number
                number = number / 10
            if len(str(final)) == 2:
                a = final
                final = 0
                for x in range(2):
                    number = a % 10
                    final += number
                    number = number/10
            return int(final)
        else:
            return int(a)
    else:
        return int(number)


def finalCheck(finalSum):
    count = 0
    print(finalSum)
    if finalSum % 10 == 0:
        print('Valid Credit Card Number')
    else:
        print('IN-Valid Credit Card Number')


main()
