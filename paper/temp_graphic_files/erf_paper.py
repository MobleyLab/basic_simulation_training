import numpy as np
from scipy import special as spc
import matplotlib.pyplot as plt

r = np.linspace(1.0, 3.0, 30)
print(r)

y = 1./r
ylj = np.power(y, 6)
print(ylj)
e = spc.erfc(r) / r
e = e /e[0]

fig = plt.figure()
plt.plot(r, y, 'b*', r, ylj, 'r--', r, e, 'k-')
plt.title("Comparison of 1/r, erfc(r) and 1/r^6")
plt.legend(['1/r', '1/r^6', 'erfc(r)/r'])
plt.xlabel('distance (r)')
plt.ylabel('Function value ')
plt.show()
fig.savefig("py_decay_comparison.pdf", bbox_inches='tight')
