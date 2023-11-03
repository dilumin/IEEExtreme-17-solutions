from collections import defaultdict

def find_sources(graph):
    # Initialize a set to store possible sources
    sources = set(graph.keys())
    remove_list = set()
    t=0
    # Create a list of nodes to remove
    while (t<20):
     for node in list(graph.keys()):  # Create a copy of keys
        for neighbor in graph[node]:
            if (node not in graph[neighbor]) and (neighbor in sources):
                remove_list.add(neighbor)
            elif (node in remove_list):
                remove_list.add(neighbor)
     t+=1
    # Remove nodes with incoming edges from the set
    for node in remove_list:
      if node in sources:
        sources.remove(node)

    return sorted(sources)


# Input: Number of relationships
n = int(input())
graph = defaultdict(list)

# Build the directed graph
for _ in range(n):
    line = input()
    if "->" in line:
        p1, p2 = line.split(" -> ")
        graph[p1].append(p2)
    else:
        p1, p2 = line.split(" ?? ")
        graph[p1].append(p2)
        graph[p2].append(p1)

# Find possible sources
sources1 = find_sources(graph)

# Output possible sources, one per line
for source in sources1:
    print(source)


# alice ?? bob
# bob -> chuck
# bob -> dev
# dev ?? eve