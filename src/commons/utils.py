from typing import List
""" Return a matrix of integers
Function used to transform information from a file to a matrix of integer.

This function is highly focused on current problme.
"""
def create_matrix(input_file):
    matrix_output = []
    for line in input_file:
        line_information = line.split(' ')
        integers_line = [int(i) for i in line_information]
        matrix_output.append(integers_line)
    return matrix_output

""" Return the manhattan value; recive two list of integer presenting two positions"""
def manhattan_distance(position_x:List[int], position_y:List[int]):
    value_m = abs(position_x[0] - position_y[0]) + abs(position_x[1] - position_y[1])
    return value_m

def find_lower_value(node_list):
    keeper = node_list[0]
    for current_node in node_list:
        if(keeper.get_value_f() > current_node.get_value_f()):
            keeper = current_node
    return keeper