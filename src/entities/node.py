class Node:
    def __init__(self, location_x:int, location_y:int, value_g:int, value_h:int, father=None):
        self.location_x = location_x
        self.location_y = location_y
        self.value_g = value_g # movement cost
        self.value_h = value_h # cost to the end
        self.father = father
    
    def get_location_x(self):
        return self.location_x
    def get_location_y(self):
        return self.location_y
    def get_value_g(self):
        return self.value_g
    def get_value_h(self):
        return self.value_h
    def get_father(self):
        return self.father

    def get_value_f(self):
        return (self.value_g + self.value_h)
    
    def __str__(self):
        return f"Location = ({self.location_x}, {self.location_y}), Value ={self.value}"