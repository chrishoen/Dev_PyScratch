import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.animation as anim
from IPython.display import HTML
from pathlib import Path

f = lambda x: np.sin(x)
x = np.linspace(-np.pi, np.pi, 100)
y = f(x)

# Initialize plot
fig, ax = plt.subplots(figsize = (7, 5))
wave, = ax.plot(x, y, "-", color = "C3", lw = 2)

ax.set_xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi])
ax.set_xticklabels((r"-$\pi$", r"-$\pi/2$", "0", r"$\pi/2$", r"$\pi$"))
ax.set_yticks((-1, 0, 1))
ax.grid(True)
ax.set_title(r"A traveling sine wave: $u(x, t) = \sin(x - ct)$")

# Transpose f(x) -> f(x - ct)
def shift(t, c = 1):
    # Transpose the wave
    new_y = f(x - c*t)
    wave.set_ydata(new_y)
    return(wave,)

# Set up animation
ani = anim.FuncAnimation(fig, shift, frames = 190, 
                         fargs = (0.1,),
                         interval = 30, blit = True)
plt.show()

    



