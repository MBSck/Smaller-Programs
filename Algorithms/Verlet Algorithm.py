# Verlet-Algorithm

import numpy as np

# Algorithmus that determines postition and velocties


def verlet_algorithm_velocity(N ,a0=1, v0=1, dt=0.1):
    """Initializes a matric, that determines all positions and velocities depending on the time"""
    x = np.zeros(N)
    v = np.zeros(N)
    t = np.arange(0, (N + 0.5) * dt, dt)
    a = np.ones(N) * 1.0    # initial condition

    # Setting of the starting variables
    x[[0, 1]] = 1           # position of particle at start
    v[0] = v0               # velocity at start
    a[0] = a0               # acceleration at start
    v[1] = v[0] + a[0] * dt

    # This loop calculates the values for velocity and time (Performance / meh)
    for i in range(1, N - 1):
        x[i + 1] = x[i] + v[i] * dt + (a[i] * (dt ** 2) * 0.5)
        v[i + 1] = v[i] + a[i] * dt
    return x[N-1], v[N-1], t[N-1]


print(verlet_algorithm_velocity(1000))