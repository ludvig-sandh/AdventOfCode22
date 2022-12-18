# 17:20 - 17:29
from dataclasses import dataclass

@dataclass
class Cube:
    x: int
    y: int
    z: int

    def key(self):
        return (x, y, z)
    
class Droplet:
    def __init__(self):
        self.cubes = set()

    def add_cube(self, cube):
        self.cubes.add(cube.key())

    def count_sides(self, cube):
        count = 0
        x, y, z = cube
        dxs = [1, 0, 0, -1, 0, 0]
        dys = [0, 1, 0, 0, -1, 0]
        dzs = [0, 0, 1, 0, 0, -1]
        for i in range(len(dxs)):
            if (x + dxs[i], y + dys[i], z + dzs[i]) not in self.cubes:
                count += 1
        return count

    def count_area(self):
        area = 0
        for cube in self.cubes:
            area += self.count_sides(cube)
        return area

with open("in.txt", "r") as f:
    droplet = Droplet()

    for line in f.read().split("\n"):
        x, y, z = [int(i) for i in line.split(",")]
        cube = Cube(x, y, z)
        droplet.add_cube(cube)

    print(droplet.count_area())