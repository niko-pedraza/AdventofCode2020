class Path:
    def __init__(self, map):
        self.trees = 0
        self.map = map

    def count_tree(self):
        self.trees += 1

    def traverse_path(self, slope_x, slope_y):
        horizontal_max = len(self.map[0])
        position_x = 0  # current index on the string
        position_y = 0

        while position_y < len(self.map):
            if self.map[position_y][position_x] == "#":
                self.count_tree()
            position_x = (position_x + slope_x) % horizontal_max
            position_y += slope_y
        return self.trees


file = open("input", 'r')
terrain = []

for row in file:
    terrain.append(row.strip())

path1 = Path(terrain)
path2 = Path(terrain)
path3 = Path(terrain)
path4 = Path(terrain)
path5 = Path(terrain)

result =path1.traverse_path(1,1)*path2.traverse_path(3,1)*path3.traverse_path(5,1)*\
        path4.traverse_path(7,1)*path5.traverse_path(1,2)

print(result)