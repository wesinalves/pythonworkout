import matplotlib.pyplot as plt
from matplotlib import animation

fig = plt.figure()
ax1 = plt.axes()
plt.xlabel('Meses')
plt.ylabel('Capital Acumulado')

plotlays, plotcols, plabels = [2], ["black","red"], ["juros simples", "juros compostos"]
lines = []
x1,y1 = [],[]
x2,y2 = [],[]

# fake data
frame_num = 15

for index in range(2):
    lobj = ax1.plot([],[],lw=2,color=plotcols[index], label=plabels[index])[0]
    lines.append(lobj)


def init():
    ax1.set_xlim(0, 20)
    ax1.set_ylim(800, 2000)
    ax1.legend(loc='lower right')    
    for line in lines:
        line.set_data([],[])
    return lines

def animate(i):

    c = 900 * i * 0.05     
    a = 900 * pow((1 + 0.05), i)       
    x1.append(i)
    y1.append(900 + c)    
    x2.append(i)
    y2.append(a)

    xlist = [x1, x2]
    ylist = [y1, y2]

    #for index in range(0,1):
    for lnum,line in enumerate(lines):
        line.set_data(xlist[lnum], ylist[lnum]) # set data for each line separately. 

    return lines

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=frame_num, interval=50, blit=True, repeat=False )


plt.show()