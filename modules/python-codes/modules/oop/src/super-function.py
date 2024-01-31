class Company:
    def company_name(self):
        return "Google"


class Employee(Company):
    def info(self):
        # Calling the superclass method using super() function.
        c_name = super().company_name()
        print("Jessa works at", c_name)


if __name__ == "__main__":
    emp = Employee()
    emp.info()
