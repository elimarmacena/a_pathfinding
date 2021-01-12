import sys
from entities.map import Map
def main():
    test_map = Map(node_begin=None, node_end=None)
    print(test_map.get_surface())
if __name__ == "__main__":
    main()