from typing import List
from entities.node import Node
class Map:
    def __init__(self, node_begin:Node, node_end:Node, surface:List[List[int]] = list()):
        self.surface = surface
        self.node_begin = node_begin
        self.node_end = node_end
        self.node_indexes = dict()
        self.__create_indexes()

    def get_surface(self):
        return self.surface
    
    def get_node_begin(self):
        return self.node_begin
    
    def get_node_end(self):
        return self.node_end
    
    def get_node_indexes(self):
        return self.node_indexes
    

    def __create_indexes(self):
        for x_position in range(len(self.surface)):
            for y_position in range(len(self.surface[x_position])):
                current_node = Node(
                    location_x=x_position,
                    location_y=y_position,
                    value_g = 10 if self.surface[x_position][y_position] != 0 else -1  # check later the correct value for valid blocks
                )
                postion_tuple = (x_position,y_position)
                self.node_indexes[postion_tuple] = current_node