import networkx as nx
import matplotlib.pyplot as plt
from bfs import bfs_iterative
from dfs import dfs_iterative
from dijkstra import dijkstra

def main():
    G = nx.Graph()  
    red_line = ["Вокзальна", "Університет", "Театральна", "Хрещатик", "Арсенальна", "Дніпро"]
    blue_line = ["Контрактова площа", "Поштова площа", "Майдан Незалежності", "Площа Український Героїв", "Олімпійська", "Палац Україна"]
    green_line = ["Дорогожичі", "Лук'янівська", "Золоті ворота", "Палац спорту", "Кловська", "Печерська"]

    for line in [red_line, blue_line, green_line]:
        G.add_nodes_from(line)
        nx.add_path(G, line)

    node_color_map = []
    for station in G:
        if station in red_line:
            node_color_map.append('red')
        elif station in blue_line:
            node_color_map.append('blue')
        elif station in green_line:
            node_color_map.append('green')

    
    for line in [red_line, blue_line, green_line]:
        for i in range(len(line) - 1):
            G.add_edge(line[i], line[i+1], weight=3)

    G.add_edge("Театральна", "Золоті ворота", weight=5) 
    G.add_edge("Майдан Незалежності", "Хрещатик", weight=5) 
    G.add_edge("Площа Український Героїв", "Палац спорту", weight=5)

    graph_dict = nx.to_dict_of_dicts(G)
    shortest_paths = dijkstra(graph_dict, "Театральна")

    max_station_name_length = max(len(station) for station in shortest_paths)
    header = f"| {'Станція':<{max_station_name_length}} | хвилини |"
    divider = f"|{'-' * (max_station_name_length + 2)}|---------|"

    print(header)
    print(divider)
    sorted_stations = sorted(shortest_paths.items(), key=lambda item: item[1])
    for tuple in sorted_stations:
        print(f"| {tuple[0]:<{max_station_name_length}} | {tuple[1]:<7} |")

    start, end = 'Вокзальна', 'Печерська'
    dfs_path = dfs_iterative(graph_dict, start, end)
    print("DFS Path:")
    print_path(dfs_path)

    print("\nBFS Path:")
    bfs_path = bfs_iterative(graph_dict, start, end)
    print_path(bfs_path)

    edge_color_map = {("Хрещатик", "Майдан Незалежності"): "yellow",
                      ("Театральна", "Золоті ворота"): "yellow",
                      ("Площа Український Героїв", "Палац спорту"): "yellow"}
    edge_colors = [edge_color_map[edge]
                   if edge in edge_color_map else "grey" for edge in G.edges()]

    plt.figure(figsize=(16, 9))
    options = {
        "node_color": node_color_map,
        "edge_color": edge_colors,
        "font_size": 8,
        "node_size": 1500,
        "width": 3,
        "with_labels": True
    }
    
    print("Кількість вершин (станцій):", G.number_of_nodes())
    print("Кількість ребер (з'єднань між станціями):", G.number_of_edges())
    print("Ступені вершин:")
    for station in G.nodes():
        print(f"Станція {station} має ступінь {G.degree(station)}")

    pos = nx.kamada_kawai_layout(G)
    nx.draw(G, pos, **options)
    plt.title("Граф Київського метрополітену")
    plt.show()

    


def print_path(lst):
    joined_string = ' → '.join(map(str, lst))
    print(joined_string)


if __name__ == "__main__":
    main()
