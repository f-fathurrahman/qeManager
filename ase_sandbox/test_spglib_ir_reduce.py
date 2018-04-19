import spglib

lattice = [[ 2.9306368570142554, 0.0000000000000000, 0.0000000000000000],
           [-1.4653184285071277, 2.5380059674413284, 0.0000000000000000],
           [ 0.0000000000000000, 0.0000000000000000, 4.6381396667889572]]
numbers = [1, 1]

points = [[0.6666666666666665, 0.3333333333333333, 0.7500000000000000],
          [0.3333333333333334, 0.6666666666666667, 0.2500000000000000]]

cell = (lattice, points, numbers)

print("-----------")
print("Using 3x3x1 mesh")
mesh = [3, 3, 1]
mapping, grid = spglib.get_ir_reciprocal_mesh(mesh, cell, is_shift=[0, 0, 0])
for m, g in zip(mapping, grid):
    print(("%2d " * 4) % (g[0], g[1], g[2], m))

print("-----------")
print("Using 3x5x1 mesh")
mesh = [3, 5, 1]
mapping, grid = spglib.get_ir_reciprocal_mesh(mesh, cell, is_shift=[0, 0, 0])
for m, g in zip(mapping, grid):
    print(("%2d " * 4) % (g[0], g[1], g[2], m))

print("-----------")
print("Using 15x15x1 mesh")
mesh = [15, 15, 1]
mapping, grid = spglib.get_ir_reciprocal_mesh(mesh, cell, is_shift=[0, 0, 0])

import numpy as np
red_grid = np.array([(g, m) for g, m in zip(grid, mapping) if (g % [5, 3, 1] == [0, 0, 0]).all()])

for g, m in red_grid:
    print(("%2d " * 4) % (g[0], g[1], g[2], m))

for g, m in red_grid:
    print(("%f " * 3 + "%d") % (g[0] / 15.0, g[1] / 15.0, g[2], m))


# print(grid[np.unique(mapping)] / np.array(mesh, dtype=float))

