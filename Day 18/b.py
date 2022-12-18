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
        self.reachable = set()

    def add_cube(self, cube):
        self.cubes.add(cube.key())

    def find_min_xyz(self):
        mx, my, mz = 1000, 1000, 1000
        for x, y, z in self.cubes:
            mx = min(mx, x)
            my = min(my, y)
            mz = min(mz, z)
        return (mx, my, mz)

    def find_max_xyz(self):
        mx, my, mz = -1000, -1000, -1000
        for x, y, z in self.cubes:
            mx = max(mx, x)
            my = max(my, y)
            mz = max(mz, z)
        return (mx, my, mz)

    def find_reachable(self):
        ix, iy, iz = self.find_min_xyz()
        ax, ay, az = self.find_max_xyz()
        stack = []
        for x in range(ix - 1, ax + 2):
            for y in range(iy - 1, ay + 2):
                stack.append((x, y, iz - 1))
                stack.append((x, y, az + 1))

        for y in range(iy - 1, ay + 2):
            for z in range(iz - 1, az + 2):
                stack.append((ix - 1, y, z))
                stack.append((ax + 1, y, z))

        for z in range(iz - 1, az + 2):
            for x in range(ix - 1, ax + 2):
                stack.append((x, iy - 1, z))
                stack.append((x, ay + 1, z))

        # Do dfs to find all visible spots
        visited = set()
        while len(stack) != 0:
            x, y, z = stack[-1]
            del stack[-1]

            if x < ix - 1 or x > ax + 1:
                continue
            if y < iy - 1 or y > ay + 1:
                continue
            if z < iz - 1 or z > az + 1:
                continue
            
            if (x, y, z) in visited:
                continue
            visited.add((x, y, z))

            if (x, y, z) in self.cubes:
                continue
            
            self.reachable.add((x, y, z))
            dxs = [1, 0, 0, -1, 0, 0]
            dys = [0, 1, 0, 0, -1, 0]
            dzs = [0, 0, 1, 0, 0, -1]
            for i in range(len(dxs)):
                stack.append((x + dxs[i], y + dys[i], z + dzs[i]))

    def count_sides(self, cube):
        count = 0
        x, y, z = cube
        dxs = [1, 0, 0, -1, 0, 0]
        dys = [0, 1, 0, 0, -1, 0]
        dzs = [0, 0, 1, 0, 0, -1]
        for i in range(len(dxs)):
            if (x + dxs[i], y + dys[i], z + dzs[i]) not in self.cubes:
                if (x + dxs[i], y + dys[i], z + dzs[i]) in self.reachable:
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

    droplet.find_reachable()
    print(droplet.count_area())

# Total: 30min