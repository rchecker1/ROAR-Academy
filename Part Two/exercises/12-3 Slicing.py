import numpy as np
v = []
for i in range(6):
    a = []
    for j in range(6):
        a.append(j + (i)*10)
    v.append(a)
    
print(v)

v = np.array(v)
blue = v[:, 1]

pink = v[1, 2:4]

green = v[2:4, 4:6]

print("blue", blue)
print("pink", pink)
print("green", green)