import numpy as np
from PIL import Image

rule_110 = np.array([False, True, True, True, False, True, True, False])
rule_90 = np.array([False, True, False, True, True, False, True, False])

evolution_steps = 300
vector_size = 150

state_110 = np.random.choice([True, False], size=vector_size)
state_90 = np.random.choice([True, False], size=vector_size)

result_110 = np.zeros(shape=(evolution_steps, vector_size), dtype=bool)
result_90 = np.zeros(shape=(evolution_steps, vector_size), dtype=bool)

for i in range(evolution_steps):
    state_110 = rule_110[
        np.roll(state_110, -1) + 2 * state_110 + 4 * np.roll(state_110, +1)
    ]
    result_110[i] = state_110

for i in range(evolution_steps):
    state_90 = rule_90[
        np.roll(state_90, -1) + 2 * state_90 + 4 * np.roll(state_90, +1)
    ]
    result_90[i] = state_90

pict = Image.fromarray(result_110)
pict.save("evolution_110.png")
pict = Image.fromarray(result_90)
pict.save("evolution_90.png")
