def input_hello():
    return 'Hello!'


def input_phone():
    return 'Give me the phone'


def input_meneger1():
    return 'Youve come for this seasons latest iPhone 14 Pro Max?'


def input_meneger2():
    return 'Do you have 80,000 roubles?'


def input_buyer1():
    p = int(input('1.Yes \n 2.No'))
    return p


def input_buyer2(p):
    if p == 1:
        return 'Yes'
    else:
        return 'No'


def input_meneger3():
    return 'Thank you for your purchase. Goodbye!'


def input_meneger4():
    return 'You have no money! Goodbye!'


def input_meneger5():
    return 'We dont have any other phones. Goodbye!'


def input_buyer3():
    return 'Thank you, goodbye!'


def main():
    print('-', input_hello())
    print('-', input_hello())
    print('-', input_phone())
    print('-', input_meneger1())
    p = input_buyer1()
    if input_buyer2(p) == 'Yes':
        print('-', input_meneger2())
        p = input_buyer1()
        if input_buyer2(p) == 'Yes':
            print('-', input_meneger3())
        else:
            print('-', input_meneger4())
    else:
        print('-', input_meneger5())
    print(' - ', input_buyer3())


if __name__ in '__main__':
    main()


