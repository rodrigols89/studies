def say_hello(msg):
    print(msg)

def return_print_function(msg):
    return print(msg)

def return_string(msg):
    return msg


if __name__ == '__main__':

    msg = 'Hello world!'

    resultSayHello = say_hello(msg)
    print(resultSayHello)
    print(type(resultSayHello), '\n')

    resultReturnHello = return_print_function(msg)
    print(resultReturnHello)
    print(type(resultReturnHello), '\n')

    resultReturnString = return_string(msg)
    print(resultReturnString)
    print(type(resultReturnString))
