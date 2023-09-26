class Student:
    # Class variable.
    school_name = "ABC School"

    def __init__(self, name, age):
        # Instance variables.
        self.name = name
        self.age = age

    @classmethod
    def change_school(Student_class, school_name):
        """Class method."""
        Student_class.school_name = school_name

    # Instance method.
    def show(self):
        print(self.name, self.age, "School:", Student.school_name)


if __name__ == "__main__":
    jessa = Student("Jessa", 20) # Instance.
    jessa.show()

    # change school_name
    Student.change_school("XYZ School")
    jessa.show()
