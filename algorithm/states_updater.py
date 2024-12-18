import faiss
import numpy as np
from algorithm.common import FIGHT, HISS, WALK

D = 2


def update_states(coords, r0, r1, states):
    res = faiss.StandardGpuResources()
    index = faiss.GpuIndexFlatL2(res, D)
    points = np.array([[coords[0, i], coords[1, i]] for i in range(len(coords[0]))])
    index.add(points)
    distances, _ = index.search(points, k=D)
    ds = distances[:, 1]
    for i in range(len(coords[0])):
        d = ds[i]
        if d <= r0:
            states[i] = FIGHT
        elif d <= r1:
            p = 1.0 / (d * d)
            if np.random.rand() > p:
                states[i] = HISS
            else:
                states[i] = WALK
        else:
            states[i] = WALK
