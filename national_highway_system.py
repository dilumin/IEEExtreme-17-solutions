from itertools import combinations


#as


def find_all_msts(graph):
    def is_spanning_tree(graph, edges):

        vertices = set()
        for edge in edges:
            vertices.add(edge[0])
            vertices.add(edge[1])

        if len(vertices) != len(graph):
            return False

        visited = {vertex: False for vertex in vertices}
        for vertex in vertices:
            visited[vertex] = True
            queue = [vertex]
            while queue:
                current = queue.pop()
                for neighbor, weight in graph[current]:
                    if (current, neighbor, weight) not in edges and (neighbor, current, weight) not in edges:
                        continue
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)

        return all(visited.values())

    all_edges = set()
    for vertex, neighbors in graph.items():
        for neighbor, weight in neighbors:
            if (vertex, neighbor, weight) not in all_edges and (neighbor, vertex, weight) not in all_edges:
                all_edges.add((vertex, neighbor, weight))

    graph_size = len(graph)
    min_weight = float('inf')
    min_spanning_trees = []

    for num_edges in range(graph_size - 1, len(all_edges) + 1):
        for possible_edges in combinations(all_edges, num_edges):
            if is_spanning_tree(graph, possible_edges):
                total_weight = sum(weight for _, _, weight in possible_edges)
                if total_weight < min_weight:
                    min_weight = total_weight
                    min_spanning_trees = [possible_edges]
                elif total_weight == min_weight:
                    min_spanning_trees.append(possible_edges)

    return min_spanning_trees


graph = {}
lis=[]
n = int(input())
for _ in range(n):
    value1 , value2 , w = input().split()
    w = int(w)
    if value1 not in lis:
        lis.append(value1)
    else:
        lis.remove(value1)
    if value2 not in lis:
        lis.append(value2)
    else:
        lis.remove(value2)

    if value1 not in graph.keys():
        graph[value1] = [(value2, w)]
    else:
        graph[value1].append((value2, w))
    if value2 not in graph.keys():
        graph[value2] = [(value1, w)]
    else:
        graph[value2].append((value1, w))
if len(lis) >= 3:
     print(-1)
     exit()
msts = find_all_msts(graph)
ant = set()
for i in msts:
    ant.update(i)
ant = list(ant)
sum = 0
for l in range(len(ant)):
    sum += int(ant[l][2])
print(sum)


