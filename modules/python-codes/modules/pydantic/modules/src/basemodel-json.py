from pydantic import BaseModel


json = {
    'name': 'Rodrigo',
    'age': 32,
    'lastname': 'Silva',
    'email': 'drigols.creative@gmail.com',
    'password': 'mypass123'
}


class Record(BaseModel):
    name: str
    age: int
    lastname: str
    email: str
    password: str
    status: bool = True


if __name__ == "__main__":

    my_record = Record(**json) # Instance.

    print(my_record.name)
    print(my_record.age)
    print(my_record.lastname)
    print(my_record.email)
    print(my_record.password)
    print(my_record.status)
