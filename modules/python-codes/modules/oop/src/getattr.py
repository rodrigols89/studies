class Student:
    # Class variables.
    country = "Brazil"

    def __init__(self, name, age):
        # Instance variables.
        self.name = name
        self.age = age


if __name__ == "__main__":
    stud = Student("Rodrigo", 34)

    stud_name = getattr(stud, "name")
    stud_age = getattr(stud, "age")
    std_country = getattr(stud, "country")

    print("Name:", stud_name)
    print("Age:", stud_age)
    print("Country:", std_country)
