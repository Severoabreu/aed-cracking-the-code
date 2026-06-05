from functools import lru_cache
from random import choice, randint, shuffle
from typing import Dict, List, Tuple

import big_o

Schedule = Tuple[int, int]


def generate_schedules(
    quantity: int,
) -> Tuple[List[Schedule], int]:
    schedule = [
        (x, x + randint(0, 3))
        for x in big_o.datagen.integers(quantity, 1, 5)
    ]

    chosen_time_x = randint(1, 8)

    return schedule, chosen_time_x + randint(0, 3)


def generate_anagrams(size: int) -> Tuple[str, str]:
    """
    Gera duas strings que são anagramas.
    """

    first_string = big_o.datagen.strings(size)

    chars = list(first_string)

    shuffle(chars)

    second_string = "".join(chars)

    return first_string, second_string


def generate_group_anagrams(quantity: int):
    words = []

    WORD_SIZE = 20

    for _ in range(quantity):

        first, second = generate_anagrams(WORD_SIZE)

        words.append(first)
        words.append(second)

    return words


def generate_palindromes(size: int) -> str:
    """
    Gera um palíndromo.
    """

    string = big_o.datagen.strings(size)

    mid = size // 2

    return (
        string[:mid]
        + string[mid:size-mid]
        + string[mid-1::-1]
    )


@lru_cache
def generate_integers(quantity: int) -> List[int]:
    if quantity <= 1:
        quantity = 2

    result = []

    while len(result) < quantity - 1:

        num = randint(1, quantity * 10)

        if num not in result:
            result.append(num)

    result.append(choice(result))

    return result


def generate_graph_without_cycle(
    quantity: int,
) -> Dict[int, List[int]]:
    graph = {}

    for node in range(quantity):

        neighbors = []

        if node + 1 < quantity:
            neighbors.append(node + 1)

        if node + 2 < quantity:
            neighbors.append(node + 2)

        graph[node] = neighbors

    return graph


def generate_graph_with_cycle(
    quantity: int,
) -> Dict[int, List[int]]:
    graph = generate_graph_without_cycle(quantity)

    if quantity > 2:
        graph[quantity - 1].append(0)

    return graph


def generate_weighted_graph(
    quantity: int,
) -> Dict[int, List[Tuple[int, int]]]:
    graph = {}

    for node in range(quantity):

        neighbors = []

        if node + 1 < quantity:
            neighbors.append(
                (
                    node + 1,
                    randint(1, 10),
                )
            )

        if node + 2 < quantity:
            neighbors.append(
                (
                    node + 2,
                    randint(1, 10),
                )
            )

        graph[node] = neighbors

    return graph


def generate_tree_values(
    quantity: int,
) -> List[int]:
    """
    Gera valores para construir árvores.

    Exemplo:

    [5, 3, 8, 1, 4]
    """

    values = list(range(quantity))

    shuffle(values)

    return values
