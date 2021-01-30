import sys
import commons.file_operations as file_operations
from entities.map import Map
from entities.node import Node
from commons.utils import create_matrix
from pathfinding import find_path

def main():
    location_start = list()
    location_end = list()
    file_path = ""
    try:
        file_path = sys.argv[1]
        location_start = [int(sys.argv[2]), int(sys.argv[3])]
        location_end = [int(sys.argv[4]), int(sys.argv[5])]
    except:
        print("Missing user arguments")

    file_input = file_operations.read_file(file_path)
    integer_matrix = create_matrix(file_input)
    file_operations.close_file(file_input)
    
    begin_node = Node(location_x = location_start[0], location_y= location_start[1], value_g=0)
    end_node = Node(location_x = location_end[0], location_y = location_end[1], value_g=0)
    
    input_map = Map(
       surface=integer_matrix,
       node_begin = begin_node,
       node_end = end_node
    )
    path = find_path(input_map)
    input_map.set_setep_nodes(path)
    print(input_map.show_map_path())
if __name__ == "__main__":
    main()