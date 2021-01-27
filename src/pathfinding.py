from entities.map import Map
from commons.utils import find_lower_value,manhattan_distance
def find_path(work_map:Map):
    end_finded = False
    # List used to create the path
    path_map = list()
    # Both list keep Node data
    open_list = list()
    close_list = list()
    # Used to keep the current node from the @open_list and check the lowest neighbor
    current_node = None
    open_list.append(work_map.get_node_begin())
    while( open_list != [] and not end_finded):
        current_node = find_lower_value(open_list)
        open_list.remove(current_node)
        close_list.append(current_node)
        close_location_list = [close_n.get_location() for close_n in close_list]
        # Will be considered equal when both nodes are from the same place in the map
        if(current_node.get_location() == work_map.get_node_end().get_location()):
            end_finded = True
            break
        #End IF
        neighbors_list = list(filter(lambda x : x != None,work_map.get_neighbors(current_node)))
        # Perform value update
        update_neighbors_g(neighbors_list,current_node)
        for neighbor_node in neighbors_list:
            if(neighbor_node.get_node_value() > -1 and neighbor_node.get_location() not in close_location_list):
                open_node = list(filter(lambda x : x.get_location() == neighbor_node.get_location(), open_list))
                if(open_node and open_node[0].get_value_g() > neighbor_node.get_value_g()):
                    open_node[0].set_value_g(neighbor_node.get_value_g())
                    open_node[0].set_father(current_node)
                #End IF
                if(not open_node):
                    neighbor_node.set_father(current_node)
                    open_list.append(neighbor_node)
                #End IF
            #End IF
        #End FOR
    #End WHILE
    if(end_finded):
        temp_path = list()
        previous_node = current_node.get_father()
        while(previous_node.get_location() != work_map.get_node_begin().get_location()):
            temp_path.append(previous_node.get_location())
            previous_node = previous_node.get_father()
        #End WHILE
        path_map = temp_path[:]
        path_map.reverse()
        return path_map
    #End IF
    else:
        raise(RuntimeError('The end destination was not found'))
    #End ELSE

    

def update_neighbors_g(neighbors, father):
    for node_neighbor in neighbors:
        node_neighbor.set_value_g(node_neighbor.get_node_value() + father.get_value_g())
        