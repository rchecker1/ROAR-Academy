import numpy as np

v = np.array([2.,2.,4.])

e0 = np.array([1.,0.,0.])
e1 = np.array([0.,1.,0.])
e2 = np.array([0.,0.,1.])

proj0 = np.dot(v,e0)
proj1 = np.dot(v,e1)
proj2 = np.dot(v,e2)

print("projection of e0", proj0)
print("projection of e1", proj1)
print("projection of e2", proj2)
