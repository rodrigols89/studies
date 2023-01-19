def process_items(items_t: Tuple[int, int, str]):
    return items_t


if __name__ == "__main__":

    my_tuple = tuple([10, 10, "Rodrigo"])
    new_tuple = process_items(my_tuple)

    print(new_tuple)
    print(type(new_tuple))
