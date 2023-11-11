from stacks import StackUsingArray

if __name__ == "__main__":

    myStack = StackUsingArray(5)
    stack_return = myStack.check_stack()
    print("Return:", stack_return)
    myStack.traverse()
    print("")

    myStack.push(10)
    stack_return = myStack.check_stack()
    print("Return:", stack_return)
    myStack.traverse()
    print("")

    myStack.push(20)
    stack_return = myStack.check_stack()
    print("Return:", stack_return)
    myStack.traverse()
    print("")

    myStack.push(30)
    stack_return = myStack.check_stack()
    print("Return:", stack_return)
    myStack.traverse()
    print("")

    myStack.push(40)
    stack_return = myStack.check_stack()
    print("Return:", stack_return)
    myStack.traverse()
    print("")

    myStack.push(50)
    stack_return = myStack.check_stack()
    print("Return:", stack_return)
    myStack.traverse()
