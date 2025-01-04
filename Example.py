from FastNoise import FastNoise
import numpy as np
import time


SIZE = (1000, 1000)
FREQUENCY = 0.01
SEED = 42

array = np.zeros(SIZE[0] * SIZE[1], dtype=np.float32)

perlin_noise = FastNoise("Perlin")
simplex_noise = FastNoise("OpenSimplex2")

final_noise = FastNoise("Add")
final_noise.set_node_lookup("LHS", perlin_noise)
final_noise.set_node_lookup("RHS", simplex_noise)

start = time.time()

min_max = final_noise.gen_uniform_grid_2d(array, 0, 0, SIZE[0], SIZE[1], FREQUENCY, SEED)

print("Generated in", time.time() - start, "seconds")
print("Min:", min_max.min, "Max:", min_max.max)
print("Result:", array)
