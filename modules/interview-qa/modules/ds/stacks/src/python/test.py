from stacks import *

if __name__ == "__main__":

    stack_one = StackUsingArray(100)
    stack_two = StackUsingLinkedList()
    stack_three = StackUsingPythonBuiltIn()

    string = input("Word/Phrase to reverse: ")
    print("Passed Word/Phrase:", string)

    print("\nReversing Word/Phrase using StackUsingArray() class:")
    reversed_string = stack_one.reverser_word_phrase(string)
    print("Reversed Word/Phrase:", reversed_string)

    print("\nReversing Word/Phrase using StackUsingLinkedList() class:")
    reversed_string = stack_two.reverser_word_phrase(string)
    print("Reversed Word/Phrase:", reversed_string)


    print("\nReversing Word/Phrase using StackUsingPythonBuiltIn() class:")
    reversed_string = stack_three.reverser_word_phrase(string)
    print("Reversed Word/Phrase:", reversed_string)
