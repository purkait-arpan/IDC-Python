# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 10:38:51 2024

@author: Kanan
"""


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#import random 

#various routines
#https://www.youtube.com/watch?v=cTJBJH8hacc
# Reference video: https://www.youtube.com/watch?v=3Xc3CA655Y4
# data file can be downloaded from here: https://github.com/KeithGalli/matplotlib_tutorial

# Website: https://matplotlib.org/stable/gallery/index.html

'''
x = [1, 2, 3, 4]
y = [5, 6, 7, 8]

#---------the graph-------------
x2 = np.arange(1,4, 0.5)

plt.figure(figsize=(4,3), dpi=150)
plt.plot(x2[:4], x2[:4]**2, label="line 2", color='blue', linestyle='-.', linewidth=2, marker='.', markersize=10, markeredgecolor='red')
plt.plot(x2[3:], x2[3:]**2, label="line 2", color='blue', linestyle='-', linewidth=2, marker='.', markersize=10, markeredgecolor='red')
plt.plot(x, y, label="line 1", color='red', linestyle='--', linewidth=4, marker='.', markersize=20, markeredgecolor='blue')
plt.title("My plot", fontdict={'fontsize': 20})
plt.xlabel("X axis", fontdict={'fontsize': 20})
plt.xticks([1, 2, 3, 3.5, 4]) #x labeling at specific points, same as y ticks
plt.ylabel("Y axis")
plt.legend()

plt.savefig('Mygraph.png', dpi=150)
plt.show()



#-------------Read and plot csv file--------------

gas = pd.read_csv('gas_prices.csv')

plt.figure(figsize=(8,5))
plt.plot(gas.Year, gas.USA)
plt.title('Gas Prices over Time (in USD)', fontdict={'fontweight':'bold', 'fontsize': 18})
plt.plot(gas.Year, gas.USA, 'b.-', label='United States')
plt.plot(gas.Year, gas.Canada, 'r.-')
plt.plot(gas.Year, gas['South Korea'], 'g.-')
plt.plot(gas.Year, gas.Australia, 'y.-')


# Another Way to plot many values!
# countries_to_look_at = ['Australia', 'USA', 'Canada', 'South Korea']
# for country in gas:
#     if country in countries_to_look_at:
#         plt.plot(gas.Year, gas[country], marker='.')


plt.xticks(gas.Year[::3])

plt.xlabel('Year')
plt.ylabel('US Dollars')

plt.legend()

plt.savefig('Gas_price_figure.png', dpi=300)

plt.show()
'''


#-----------histogram from csv file----------------------
'''
fifa = pd.read_csv('fifa_data.csv')

print(fifa.head(5))

#---------histogram--------------


bins = [40,50,60,70,80,90,100]

plt.figure(figsize=(8,5))

plt.hist(fifa.Overall, bins=bins, color='#abcdef')

plt.xticks(bins)

plt.ylabel('Number of Players')
plt.xlabel('Skill Level')
plt.title('Distribution of Player Skills in FIFA 2018')

plt.savefig('histogram.png', dpi=300)

plt.show()
'''

#-------------Image plot ( imshow )-----------------------------
'''
np.random.seed(19680801)

imdata = np.random.normal(0., 1., (101,101)) #Gaussian random number of mean 0, sd=1 of size (100*100)
imdata1 = np.random.normal(0., 1., (101,101))
print(np.mean(imdata))
print(np.std(imdata))

plt.subplot(211)
plt.imshow(imdata)


plt.subplot(212)
plt.imshow(imdata1)

plt.subplots_adjust(bottom=0.1, right=0.8, top=0.9)

cax = plt.axes([0.85, 0.1, 0.075, 0.8])
plt.colorbar(cax=cax)

plt.hist(imdata, 10, density=False)
plt.show()

'''
#--------Image reading-----------------
'''
im = plt.imread("Mygraph.png")
#print(im[1300][500][1])
plt.imshow(im)
'''
#----------Animation---------------------------------------
'''
def sinfunc(x, t):
    return(np.sin(x-3*t))
x = np.linspace(0., 10.*np.pi, 1000)
plt.plot(sinfunc(x,0))

from matplotlib import animation
from matplotlib.animation import PillowWriter
fig, ax =plt.subplots(1, 1, figsize=(8,4))

ln1, =plt.plot([],[])
time_text = ax.text(0.65, 0.95, '',fontsize=15, transform=ax.transAxes, bbox=dict(facecolor='white', edgecolor='black'))
ax.set_xlim(0., 10.*np.pi)
ax.set_ylim(-1.5, 1.5)

def animate(i):
    ln1.set_data(x, sinfunc(x, 1./50*i))
    time_text.set_text("t={:.2f}".format(i/50))

ani = animation.FuncAnimation(fig, animate, frames=240, interval=50) 
ani.save('myanimation.gif', writer='pillow', fps=50, dpi=100)   
'''
#----------Rotating animation----------------
