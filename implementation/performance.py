from random import shuffle
from time import perf_counter
from typing import Type

from implementation.nim.nim_table import NimTable
from implementation.py.base import BaseHashTable
from implementation.py.hash_table import LLHashTable, BSTHashTable

SIZE = 1000000


def generate_data():
    keys = list(range(SIZE))
    shuffle(keys)
    values = [f"TEST_{i}" for i in range(SIZE)]
    # Dictionary will return sorted data. It is not representative
    # That's why I'm using tuple
    return keys, values


def measure_performance(table_type: Type[BaseHashTable]):
    keys, values = generate_data()
    start = perf_counter()

    ht = table_type(max_load_factor=0.5, size=20000)

    for i, key in enumerate(keys):
        ht[key] = values[i]
    insert_finished = perf_counter()
    for i, key in enumerate(keys):
        ht[key]
    read_finished = perf_counter()

    for key in keys:
        del ht[key]

    delete_finished = perf_counter()

    return (
        insert_finished - start,
        read_finished - insert_finished,
        delete_finished - read_finished
    )


def main():
    print('Measuring PY Linked List Node')
    inserted_py_ll, read_py_ll, deleted_py_ll = measure_performance(
        LLHashTable)

    print('Measuring PY BST Node')
    inserted_py_bst, read_py_bst, deleted_py_bst = measure_performance(
        BSTHashTable)

    print('Measuring NIM')
    inserted_nim, read_nim, deleted_nim = measure_performance(NimTable)

    print('---------')
    print("PY LL results")
    print(f"Insert time: {inserted_py_ll:.2f}")
    print(f"Read time: {read_py_ll:.2f}")
    print(f"Delete time: {deleted_py_ll:.2f}")
    print('---------')
    print("PY BST results")
    print(f"Insert time: {inserted_py_bst:.2f}")
    print(f"Read time: {read_py_bst:.2f}")
    print(f"Delete time: {deleted_py_bst:.2f}")
    print('---------')
    print("NIM LL results")
    print(f"Insert time: {inserted_nim:.2f}")
    print(f"Read time: {read_nim:.2f}")
    print(f"Delete time: {deleted_nim:.2f}")


if __name__ == '__main__':
    main()
