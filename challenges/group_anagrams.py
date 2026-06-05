def group_anagrams(words: list[str]) -> list[list[str]]:
    groups = []

    for word in words:

        inserted = False

        for group in groups:

            representative = group[0]

            if sorted(word) == sorted(representative):
                group.append(word)
                inserted = True
                break

        if not inserted:
            groups.append([word])

    return groups
