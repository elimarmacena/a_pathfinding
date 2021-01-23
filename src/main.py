import sys
from entities.map import Map
from entities.node import Node
from commons.utils import create_matrix
from pathfinding import find_path
def main():
    file_input = open('D:\\Documents\\github_repositories\\a_pathfinding\\resources\\mapa.txt','r')
    integer_matrix = create_matrix(file_input)
    file_input.close()
    begin_node = Node(location_x = 0, location_y = 0, value_g=0)
    end_node = Node(location_x= 9, location_y=8, value_g=0)
    
    test_map = Map(
       surface=integer_matrix,
       node_begin = begin_node,
       node_end = end_node
    )
    path = find_path(test_map)
    print(path)
if __name__ == "__main__":
    main()