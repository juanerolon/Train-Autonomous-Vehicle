import operator
import random
import numpy as np
import matplotlib.pyplot as plt

#Extract a random sample from Q-table
def qtable_sample(fname,nsamples):

    f = open(fname, 'r')
    span = len(f.readlines())
    f.seek(0)
    state_maxQ_list = []
    state_maxQ_ldicts = []
    for i in range(span):
        tmp_entry = []
        tmp_dict = {}
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
            state = eval(str_line.rstrip())
            wypt = state[0]
            inps = (state[1], state[2],state[3],state[4])
            acts = zip(lst1, lst2)
            maxq_act = lst1[index]
            tmp_entry.append(wypt)
            tmp_entry.append(inps)
            tmp_entry.append(acts)
            tmp_entry.append(maxq_act)

            tmp_dict['waypoint'] = wypt
            tmp_dict['inp_light'] =inps[0]
            tmp_dict['inp_left'] = inps[1]
            tmp_dict['oncoming'] = inps[2]
            tmp_dict['inp_right'] =inps[3]
            tmp_dict['avail_actions'] = acts
            tmp_dict['maxQaction'] = maxq_act

            state_maxQ_list.append(tmp_entry)
            state_maxQ_ldicts.append(tmp_dict)


    return random.sample(state_maxQ_ldicts,nsamples)

#Plotting functions
def create_canvas(axlabels):
    # frame
    plt.plot()
    plt.xlim(-1.2, 1.2)
    plt.ylim(-0.8, 1.8)
    # show axis (off, on)
    plt.axis(axlabels)
    # intersection point
    intersect = plt.Circle((0.05, 0.55), radius=0.05, fc='k', fill=False, linestyle='dashed')
    plt.gca().add_patch(intersect)

def traffic_light(light_color):

    if light_color == 'green':

        #green traffic light
        circle = plt.Circle((-0.8, 1.5), radius=0.15, fc='lime')
        plt.gca().add_patch(circle)

        #red traffic light
        circle2 = plt.Circle((-0.45, 1.5), radius=0.15, fc='gray', linestyle='dashed',fill=False)
        plt.gca().add_patch(circle2)

    elif light_color == 'red':

        # green traffic light
        circle = plt.Circle((-0.8, 1.5), radius=0.15, fc='gray', linestyle='dashed',fill=False)
        plt.gca().add_patch(circle)

        # red traffic light
        circle2 = plt.Circle((-0.45, 1.5), radius=0.15, fc='r')
        plt.gca().add_patch(circle2)
    else:
        raise Exception('Invalid traffic light state')

def percept_input(input):

    if input == 'left':
        #input left
        plt.plot((-0.7, -0.3), (-0.2, -0.2), lw=2, color='gray', clip_on=True,linestyle='dashed')
        plt.text(-0.65,-0.15,'Input left', rotation='horizontal', fontsize='9',color='gray')
    elif input == 'right':
        #input right
        plt.plot((0.4, 0.8), (-0.2, -0.2), lw=2, color='gray', clip_on=True,linestyle='dashed')
        plt.text(0.45,-0.15,'Input right', rotation='horizontal', fontsize='9',color='gray')
    elif input == 'forward':
        #input forward
        plt.plot((0.05, 0.05), (0.0, 0.45), lw=2, color='gray', clip_on=True,linestyle='dashed')
        plt.text(-0.05,0.40,'Input foward', rotation='vertical', fontsize='9',color='gray')
    elif input == None or 'None':
        pass
    else:
        raise Exception('Invalid percept input')


def oncoming_traffic(direction):

    if direction == 'left':

        #oncoming left
        xi = -0.8
        yi = 0.5
        dx = 0.4
        dy = 0.0
        plt.arrow(xi, yi, dx,dy, head_width=0.04, head_length=0.05, fc='b', ec='b')
        plt.text(-0.8,0.6,'Oncoming left', rotation='horizontal', fontsize='9')

    elif direction == 'forward':

        #oncoming forward
        xi = 0.05
        yi = 1.2
        dx = 0.0
        dy = -0.4
        plt.arrow(xi, yi, dx,dy, head_width=0.04, head_length=0.05, fc='b', ec='b')
        plt.text(-0.05,1.5,'Oncoming forward', rotation='vertical', fontsize='9')

    elif direction == 'right':

        #oncoming right
        xi =0.9
        yi = 0.5
        dx = -0.4
        dy = 0.0
        plt.arrow(xi, yi, dx,dy, head_width=0.04, head_length=0.05, fc='b', ec='b')
        plt.text(0.45,0.6,'Oncoming right',fontsize='9')

    elif direction == None or 'None':
        pass
    else:
        raise Exception('Invalid oncomming traffic percept')

def waypoint(direction):

    #waypoint foward
    if direction=='forward':
        xi = 0.05
        yi = -0.5
        dx = 0.0
        dy = 0.3
        plt.arrow(xi, yi, dx,dy, head_width=0.04, head_length=0.05, fc='k', ec='k',linestyle='solid',linewidth=3.5)
        plt.text(-0.1,-0.6,'Waypoint',fontsize='9',fontweight='bold')


    #waypoint right
    elif direction == 'right':
        # ---- base
        xi = 0.05
        yi = -0.5
        dx = 0.0
        dy = 0.15
        plt.arrow(xi, yi, dx,dy, head_width=0.04, head_length=0.05, fc='k', ec='k',linestyle='solid',linewidth=3.5)
        # ---- tip
        xi2 = 0.05
        yi2 = -0.3
        dx2 = 0.1
        dy2 = 0.0
        plt.arrow(xi2, yi2, dx2,dy2, head_width=0.04, head_length=0.05, fc='k', ec='k',linestyle='solid',linewidth=3.5)
        plt.text(-0.1,-0.6,'Waypoint',fontsize='9',fontweight='bold')

    #waypoint left
    elif direction=='left':
        # ---- base
        xi = 0.05
        yi = -0.5
        dx = 0.0
        dy = 0.15
        plt.arrow(xi, yi, dx,dy, head_width=0.04, head_length=0.05, fc='k', ec='k',linestyle='solid',linewidth=3.5)
        # ---- tip
        xi2 = 0.05
        yi2 = -0.3
        dx2 = -0.1
        dy2 = 0.0
        plt.arrow(xi2, yi2, dx2,dy2, head_width=0.04, head_length=0.05, fc='k', ec='k',linestyle='solid',linewidth=3.5)
        plt.text(-0.1,-0.6,'Waypoint',fontsize='9',fontweight='bold')

    elif direction == None or 'None':
        pass
    else:
        raise Exception('Invalid waypoint percept')


def maxQ_action(action):

    # maxQ action enclosing rectangle
    maxq_rect = plt.Rectangle((0.45, 1.2), 0.5, 0.55, fill=False)
    plt.gca().add_patch(maxq_rect)

    # maxQ action forward
    if action == 'forward':
        xi = 0.7
        yi = 1.35
        dx = 0.0
        dy = 0.3
        plt.arrow(xi, yi, dx, dy, head_width=0.04, head_length=0.05, fc='darkgreen', ec='darkgreen', linestyle='solid', linewidth=3.5)
        plt.text(0.5, 1.25, 'MaxQ action', fontsize='9', fontweight='bold', color='darkgreen')

    # maxQ action left
    elif action == 'left':
        xi = 0.7
        yi = 1.35
        dx = 0.0
        dy = 0.15
        plt.arrow(xi, yi, dx, dy, head_width=0.04, head_length=0.05, fc='darkgreen', ec='darkgreen', linestyle='solid', linewidth=3.5)
        xi2 = 0.7
        yi2 = 1.55
        dx2 = -0.1
        dy2 = 0.0
        plt.arrow(xi2, yi2, dx2, dy2, head_width=0.04, head_length=0.05, fc='darkgreen', ec='darkgreen', linestyle='solid',
                 linewidth=3.5)

        plt.text(0.5, 1.25, 'MaxQ action', fontsize='9', fontweight='bold', color='darkgreen')

    # maxQ action right
    elif action == 'right':
        xi = 0.7
        yi = 1.35
        dx = 0.0
        dy = 0.15
        plt.arrow(xi, yi, dx, dy, head_width=0.04, head_length=0.05, fc='darkgreen', ec='darkgreen', linestyle='solid', linewidth=3.5)
        xi2 = 0.7
        yi2 = 1.55
        dx2 = 0.1
        dy2 = 0.0
        plt.arrow(xi2, yi2, dx2, dy2, head_width=0.04, head_length=0.05, fc='darkgreen', ec='darkgreen', linestyle='solid',
                 linewidth=3.5)

        plt.text(0.5, 1.25, 'MaxQ action', fontsize='9', fontweight='bold', color='darkgreen')

    # maxQ action None (idle)
    elif action == None or 'None':
        plt.text(0.63, 1.45, 'Idle', fontsize='12', fontweight='bold', color='darkgreen')
        plt.text(0.5, 1.25, 'MaxQ action', fontsize='9', fontweight='bold', color='darkgreen')
    else:
        raise Exception('Invalid maxQ action')

#Test functions above:
if False:

    plt.figure(1,figsize=(12, 6))

    plt.subplot(1, 2, 1)

    create_canvas('on')
    traffic_light('green')
    percept_input('left')
    oncoming_traffic('right')
    waypoint('left')
    maxQ_action('forward')

    plt.subplot(1, 2, 2)

    create_canvas('on')
    traffic_light('red')
    percept_input('right')
    oncoming_traffic('left')
    waypoint('right')
    maxQ_action('left')


    plt.tight_layout()
    plt.show()


def create_qsample_fig(obs):
    create_canvas('on')


#state = (waypoint, inputs['light'], inputs['oncoming'], inputs['left'], inputs['right'])
sample = qtable_sample('sim_improved-learning.txt',5)

for d in sample:
    print d







