from typing import List
from entities.node import Node
class Map:
    def __init__(self, node_begin:Node, node_end:Node, surface:List[List[int]] = list()):
        self.surface = surface
        self.node_begin = node_begin
        self.node_end = node_end
        self.path_list = list()

    def get_surface(self):
        return self.surface
    
    def get_node_begin(self):
        return self.node_begin
    
    def get_node_end(self):
        return self.node_end
    
    def get_path_list(self):
        return self.path_list