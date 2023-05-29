def say_name(first_name: str, last_name: str) -> str:
    return first_name + " " + last_name

if __name__ =="__main__":

    first_name: str = "Rodrigo"
    last_name: str = "Leite"

    name: str = say_name(first_name, last_name)

    print("Name: ", name)
    print("Type: ", type(name))
