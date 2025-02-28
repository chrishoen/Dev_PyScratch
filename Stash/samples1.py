import matplotlib.pyplot as plt
import numpy as np
import csv

filename = '20250226-191429.SAMPLES'
filename = '20250226-192210.SAMPLES'
filename = '20250227-200045.SAMPLES'
filename = '20250227-201845.SAMPLES'

filename = '20250227-201845.SAMPLES'

x = []
y = []
#x = np.linspace(0, 2 * np.pi, 200)
#y = np.sin(x)

with open(filename,'r') as csvfile: 
    lines = csv.reader(csvfile, delimiter=',') 
    for row in lines: 
        y.append(int(row[2])) 

x = np.linspace(0, 1.0, len(y))

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()
