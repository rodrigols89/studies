from typing import Union


def process_item(item: Union[int, str]):
    print(item)


if __name__ == "__main__":
    age: int = 10
    name: str = "Rodrigo"

    process_item([age, name])
