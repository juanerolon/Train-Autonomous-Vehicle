import operator
import random
import numpy as np
import matplotlib.pyplot as plt


#Count entries of Q policy textfile

f = open('sim_improved-learning.txt', 'r')
span = len(f.readlines())
f.seek(0)
state_maxQ_list = []
for i in range(span):
    tmp_entry = []
    str_line = f.readline()
    if "('" in str_line:
        lst1 = []
        lst2 = []
        for i in range(4):
            tmpl = f.readline()
            if '--' in tmpl:
                pos1 = tmpl.find('--')
                pos2 = tmpl.find(':')
                act_def = tmpl[pos1 + 3:pos2 - 1]
                act_val = tmpl[pos2 + 2:-1]
                lst1.append(act_def)
                lst2.append(act_val)
        index, value = max(enumerate(lst2), key=operator.itemgetter(1))
        e1 = "State = {}".format(str_line.rstrip())
        e2 = "Available actions = {}".format(zip(lst1, lst2))
        e3 = "MaxQ action = {}".format(lst1[index])
        tmp_entry.append(e1)
        tmp_entry.append(e2)
        tmp_entry.append(e3)
        state_maxQ_list.append(tmp_entry)

sample = random.sample(state_maxQ_list,10)
j=1
for s in sample:
    for e in s:
        if e[0] == 'S':
            print '{}. '.format(j) + e
        else:
            print '    ' + e
    print ""
    j += 1


#Plotting cartoons


ax = plt.axes()
plt.xlim(-1.2,1.2)
plt.ylim(-0.8,1.8)

circle = plt.Circle((-0.8, 1.5), radius=0.15, fc='g')
plt.gca().add_patch(circle)

circle2 = plt.Circle((-0.45, 1.5), radius=0.15, fc='r')
plt.gca().add_patch(circle2)

intersect = plt.Circle((0.05, 0.55), radius=0.05, fc='k', fill=True)
plt.gca().add_patch(intersect)


plt.plot((-0.7, -0.3), (-0.2, -0.2), lw=2, color='gray', clip_on=True,linestyle='dashed') #left
plt.plot((0.4, 0.8), (-0.2, -0.2), lw=2, color='gray', clip_on=True,linestyle='dashed')   #right
plt.plot((0.05, 0.05), (0.0, 0.45), lw=2, color='gray', clip_on=True,linestyle='dashed')   #vertical



#oncoming left
xi = -0.8
yi = 0.5
dx = 0.4
dy = 0.0
ax.arrow(xi, yi, dx,dy, head_width=0.04, head_length=0.05, fc='r', ec='r')
plt.text(-0.8,0.6,'Oncoming left', rotation='horizontal', fontsize='9')

# oncoming forward
xi = 0.05
yi = 1.2
dx = 0.0
dy = -0.4
ax.arrow(xi, yi, dx,dy, head_width=0.04, head_length=0.05, fc='b', ec='b')
plt.text(-0.05,1.5,'Oncoming forward', rotation='vertical', fontsize='9')

#oncoming right
xi =0.9
yi = 0.5
dx = -0.4
dy = 0.0
ax.arrow(xi, yi, dx,dy, head_width=0.04, head_length=0.05, fc='g', ec='g')
plt.text(0.45,0.6,'Oncoming right',fontsize='9')

xi = 0.05
yi = -0.5
dx = 0.0
dy = 0.3

ax.arrow(xi, yi, dx,dy, head_width=0.04, head_length=0.05, fc='k', ec='k',linestyle='solid',linewidth=3.5)


#ax.axis('off')
plt.show()

