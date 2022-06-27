class Person:
    def __init__(self, name: str):
        self.name = name


def get_person_name(one_person: Person):
    return one_person.name


if __name__ == "__main__":

    my_name: str = "Rodrigo"
    p = Person(name=my_name)

    name_returned = get_person_name(p)
    print(name_returned)
