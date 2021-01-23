from typing import List
from entities.node import Node
from commons.utils import manhattan_distance
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
    
    # informations on diagonal will be ignored
    def get_neighbors(self,center_node:Node):
        middle_top      = self.node_indexes[(center_node.get_location_x() - 1, center_node.get_location_y())] if center_node.get_location_x() - 1 >= 0 else None
        left_middle     = self.node_indexes[(center_node.get_location_x(), center_node.get_location_y() - 1)] if center_node.get_location_y() - 1 >= 0  else None
        right_middle    = self.node_indexes[(center_node.get_location_x(), center_node.get_location_y() + 1)] if center_node.get_location_y() + 1 <= self.node_end.get_location_y() else None
        middle_bottom   = self.node_indexes[(center_node.get_location_x() + 1, center_node.get_location_y())] if center_node.get_location_x() + 1 <= self.node_end.get_location_x() else None
        neighbors_list = [
            middle_top,
            left_middle,
            right_middle,
            middle_bottom
        ]
        return neighbors_list

    def __create_indexes(self):
        for x_position in range(len(self.surface)):
            for y_position in range(len(self.surface[x_position])):
                current_node = Node(
                    location_x=x_position,
                    location_y=y_position,
                    value_g = 0 if self.surface[x_position][y_position] == 0 else -1,
                    value_h = manhattan_distance([x_position,y_position],self.node_end.get_location())
                )
                postion_tuple = (x_position,y_position)
                self.node_indexes[postion_tuple] = current_node