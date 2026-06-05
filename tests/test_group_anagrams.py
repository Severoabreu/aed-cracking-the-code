import pytest

from challenges.group_anagrams import group_anagrams


def normalize(groups):
    normalized = []

    for group in groups:
        normalized.append(tuple(sorted(group)))

    return sorted(normalized)


@pytest.mark.parametrize(
    "words, expected",
    [
        pytest.param(
            ["amor", "roma"],
            [["amor", "roma"]],
            id="single-group",
        ),
        pytest.param(
            ["amor", "roma", "mora"],
            [["amor", "roma", "mora"]],
            id="single-group-three-words",
        ),
        pytest.param(
            ["amor", "roma", "mora", "carro", "arroc"],
            [
                ["amor", "roma", "mora"],
                ["carro", "arroc"],
            ],
            id="two-groups",
        ),
        pytest.param(
            [],
            [],
            id="empty-list",
        ),
        pytest.param(
            ["amor"],
            [["amor"]],
            id="single-word",
        ),
        pytest.param(
            ["a", "b", "c"],
            [["a"], ["b"], ["c"]],
            id="no-anagrams",
        ),
        pytest.param(
            ["", "", "abc"],
            [["", ""], ["abc"]],
            id="empty-strings",
        ),
    ],
)
def test_group_anagrams(words, expected):

    result = group_anagrams(words)

    assert normalize(result) == normalize(expected)


def test_repeated_words():

    words = [
        "amor",
        "roma",
        "amor",
    ]

    expected = [
        [
            "amor",
            "roma",
            "amor",
        ]
    ]

    result = group_anagrams(words)

    assert normalize(result) == normalize(expected)


def test_large_group():

    words = [
        "abc",
        "cab",
        "bac",
        "acb",
        "cba",
        "bca",
    ]

    expected = [
        [
            "abc",
            "cab",
            "bac",
            "acb",
            "cba",
            "bca",
        ]
    ]

    result = group_anagrams(words)

    assert normalize(result) == normalize(expected)


def test_many_groups():

    words = [
        "abc",
        "cab",
        "dog",
        "god",
        "listen",
        "silent",
        "evil",
        "vile",
        "stone",
    ]

    expected = [
        ["abc", "cab"],
        ["dog", "god"],
        ["listen", "silent"],
        ["evil", "vile"],
        ["stone"],
    ]

    result = group_anagrams(words)

    assert normalize(result) == normalize(expected)


def test_case_sensitive():

    words = [
        "Amor",
        "roma",
    ]

    expected = [
        ["Amor"],
        ["roma"],
    ]

    result = group_anagrams(words)

    assert normalize(result) == normalize(expected)


def test_preserves_all_words():

    words = [
        "amor",
        "roma",
        "mora",
        "carro",
        "arroc",
        "python",
    ]

    result = group_anagrams(words)

    flattened = []

    for group in result:
        flattened.extend(group)

    assert sorted(flattened) == sorted(words)
