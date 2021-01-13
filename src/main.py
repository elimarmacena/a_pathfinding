import sys
from entities.map import Map
from commons.utils import create_matrix
def main():
    file_input = open('D:\\Documents\\github_repositories\\a_pathfinding\\resources\\mapa.txt','r')
    inter_matrix = create_matrix(file_input)
    file_input.close()
    test_map = Map(
        surface=inter_matrix,
        node_begin = None,
        node_end = None
    )
    print(test_map.get_node_indexes())
if __name__ == "__main__":
    main()