import statix.descriptive as d
import numpy as np

data = [1, 2, 3, 4, 5]

print(sorted(data))

print(d.mean(data))
print(d.var(data))
print(d.std(data))

print(np.mean(data))
print(np.var(data))
print(np.std(data))