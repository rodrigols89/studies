# bool: boolean values (True=1 or False=0)

def check_signal(signal: bool) -> bool:
    if signal == 1:
        return True
    elif signal == 0:
        return False

if __name__ =="__main__":

    turn_on: bool = 1
    turn_off: bool = 0

    # True sample.
    result: bool = check_signal(turn_on)
    print("Status: ", result)
    print("Type: ", type(result))

    # False sample.
    result = check_signal(turn_off)
    print("Status: ", result)
    print("Type: ", type(result))
