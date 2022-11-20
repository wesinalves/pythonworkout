"""
Simple interest x Compound interest
By Wesin Ribeiro
12/11/2022
"""

import matplotlib.pyplot as plt
from matplotlib import animation

fig = plt.figure()
ax1 = plt.axes()
plt.xlabel('Meses')
plt.ylabel('Capital Acumulado')

plotcols, plabels = ["black", "red"], ["juros simples", "juros compostos"]
lines = []
x1, y1 = [],[]
x2, y2 = [], []

frame_num = 15

for index in range(2):
    lobj = ax1.plot([],[],
        lw=2, color=plotcols[index], label=plabels[index])[0]
    lines.append(lobj)

def init():
    ax1.set_xlim(0, 20)
    ax1.set_ylim(800, 2000)
    ax1.legend(loc='lower right')
    for line in lines:
        line.set_data([],[])
    return lines

def animate(i):
    c = 900 * i * 0.05 # simple interest
    a = 900 * pow((1 + 0.05), i) # compound interest
    x1.append(i)
    y1.append(900 + c)
    x2.append(i)
    y2.append(a)

    xlist = [x1, x2]
    ylist = [y1, y2]

    for lnum,line in enumerate(lines):
        # set data for each line separetely.
        line.set_data(xlist[lnum], ylist[lnum])
    
    return lines

# call the animator
anim = animation.FuncAnimation(
    fig, animate, init_func=init,
    frames=frame_num, interval=200, blit=True, repeat=False)


anim.save('interest.gif', writer='pillow')