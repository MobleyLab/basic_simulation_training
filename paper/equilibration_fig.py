

import numpy as np
import matplotlib.pyplot as plt



tvals = np.arange(0.0, 100.0, 0.5)
randdat = np.random.random(len(tvals))*(2.0) - 1.0
tempvals = np.exp(-tvals/2.0) + 1.0 + randdat*0.3

longvals = 1.0 - np.exp(-(tvals/200.0)**0.75) + randdat*0.1



fig, ax = plt.subplots(2, dpi=300)

ax[0].plot(tvals, tempvals)
ax[1].plot(tvals, longvals)

ax[1].set_ylim([0.0, 0.8])
ax[0].set_xlim(0.0, 100.0)
ax[1].set_xlim(0.0, 100.0)

ax[0].set_xticks([])
ax[1].set_xticks([])
ax[0].set_yticks([])
ax[1].set_yticks([])

ax[1].set_xlabel('Simulation Time', fontsize=18)
ax[0].annotate('Quickly-equilibrating', xy=(0.1, 0.8), xycoords='axes fraction', 
               xytext=(0.1, 0.8), textcoords='axes fraction', ha='left', va='center', fontsize=16)
ax[1].annotate('Slowly-equilibrating', xy=(0.1, 0.8), xycoords='axes fraction', 
               xytext=(0.1, 0.8), textcoords='axes fraction', ha='left', va='center', fontsize=16)

fig.subplots_adjust(hspace=0)

plt.show()





