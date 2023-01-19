from typing import List


def process_items(items: List[str]):
    for item in items:
        print(item)


if __name__ == "__main__":
    my_list = ["Rodrigo", "Jhon", "Matheus", "10"]
    process_items(my_list)
