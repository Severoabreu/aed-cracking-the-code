def has_cycle(graph: dict[str, list[str]]) -> bool:
    visited = {vertex: 0 for vertex in graph.keys()}

    def dfs(vertex):
        visited[vertex] = 1

        for vizinho in graph[vertex]:
            if visited[vizinho] == 1:
                return True

            if visited[vizinho] == 0:
                if dfs(vizinho):
                    return True

        visited[vertex] = 2
        return False

    for vertex in graph.keys():
        if visited[vertex] == 0:
            if dfs(vertex):
                return True

    return False
