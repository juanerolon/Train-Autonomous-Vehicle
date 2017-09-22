
#The following script creates a symbolic representation of the Q-table entries
#represented in the provided text file corresponding to the output of the improved Q-learning
#algorithm
#author: @J.E. Rolon

import operator
import random
import matplotlib.pyplot as plt

# ******************* Extract a random sample from Q-table *******************
def qtable_sample(fname, nsamples):
    """Input filename of textfile storing qtable. Number of samples requested
       Returns a sample of observations from the q-table. Each observation is
       a dictionary specifying the observed state, the input percepts and the
       action that maximizes the Q value.
    """
    f = open(fname, 'r')
    span = len(f.readlines())
    f.seek(0)
    state_maxQ_ldicts = []
    for i in range(span):
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
            inps = (state[1], state[2], state[3], state[4])
            acts = zip(lst1, lst2)
            maxq_act = lst1[index]
            tmp_dict['waypoint'] = wypt
            tmp_dict['inp_light'] = inps[0]
            tmp_dict['inp_left'] = inps[1]
            tmp_dict['inp_oncoming'] = inps[2]
            tmp_dict['inp_right'] = inps[3]
            tmp_dict['avail_actions'] = acts
            tmp_dict['maxQaction'] = maxq_act
            state_maxQ_ldicts.append(tmp_dict)

    return random.sample(state_maxQ_ldicts, nsamples)

# *************************** Plotting functions **********************************************
#
# The following set of functions encapsulate different objects representing the elements of the
# the Q-table. Together generate a figure representing the state, input percepts and action taken.
def create_canvas(axlabels):
    """Defines the figure frame dimensions and axis specs"""
    plt.plot()
    plt.xlim(-1.2, 1.2)
    plt.ylim(-0.8, 1.8)
    # show axis (off, on)
    plt.axis(axlabels)
    plt.xticks([])
    plt.yticks([])

def intersection_point():
    """Generates a circle specifying the intersection point location"""
    intersect = plt.Circle((0.05, 0.3), radius=0.05, fc='k', fill=False, linestyle='dashed')
    return plt.gca().add_patch(intersect)

def percept_traffic_light(light_color):
    """Creates a representation of the traffic light states. Input current light color"""
    ypos = 1.6
    xpos = -0.9
    dx = 0.35
    if light_color == 'green':
        # green traffic light
        circle = plt.Circle((xpos, ypos), radius=0.15, fc='lime')
        plt.gca().add_patch(circle)
        # red traffic light
        circle2 = plt.Circle((xpos+dx, ypos), radius=0.15, fc='gray', linestyle='dashed', fill=False)
        plt.gca().add_patch(circle2)
        plt.text(xpos, ypos-0.25, 'Traffic light', rotation='horizontal', fontsize='9')
    elif light_color == 'red':
        # green traffic light
        circle = plt.Circle((xpos, ypos), radius=0.15, fc='gray', linestyle='dashed', fill=False)
        plt.gca().add_patch(circle)
        # red traffic light
        circle2 = plt.Circle((xpos+dx, ypos), radius=0.15, fc='r')
        plt.gca().add_patch(circle2)
        plt.text(xpos, ypos - 0.25, 'Traffic light', rotation='horizontal', fontsize='9')
    else:
        raise Exception('Invalid traffic light state')

def percept_input_left(input):
    """Represents the input percept and direction of a potential vehicle approaching from the LEFT
       valid inputs: approaching vehicle turning right, turning left,  moving forward.
       Percepts as observed from agent. Turns represented respect to approaching vehicle.
    """
    if input == 'right':
        # input left
        plt.arrow(-0.7, -0.2, 0.15, 0.0, lw=2, head_width=0.04, head_length=0.05, fc='gray', ec='gray',
                  linestyle='dashed')
        plt.arrow(-0.5, -0.2, 0.0, -0.15, lw=2, head_width=0.04, head_length=0.05, fc='gray', ec='gray',
                  linestyle='dashed')
        plt.text(-0.75, -0.15, 'Input left: right', rotation='horizontal', fontsize='9', color='gray')
    elif input == 'left':
        # input right
        plt.arrow(-0.7, -0.2, 0.15, 0.0, lw=2, head_width=0.04, head_length=0.05, fc='gray', ec='gray',
                  linestyle='dashed')
        plt.arrow(-0.5, -0.2, 0.0, 0.15, lw=2, head_width=0.04, head_length=0.05, fc='gray', ec='gray',
                  linestyle='dashed')
        plt.text(-0.75, -0.30, 'Input left: left', rotation='horizontal', fontsize='9', color='gray')
    elif input == 'forward':
        # input forward
        plt.arrow(-0.75, -0.2, 0.35, 0.0, lw=2, head_width=0.04, head_length=0.05, fc='gray', ec='gray',
                  linestyle='dashed')
        plt.text(-0.8, -0.15, 'Input left: forward', rotation='horizontal', fontsize='9', color='gray')
    elif input == None or 'None':
        pass
    else:
        raise Exception('Invalid percept input')

def percept_input_right(input):
    """Represents the input percept and direction of a potential vehicle approaching from the RIGHT
       valid inputs: approaching vehicle turning right, turning left,  moving forward.
       Percepts as observed from agent. Turns represented respect to approaching vehicle.
    """
    if input == 'left':
        # input left
        plt.arrow(0.9, -0.2, -0.15, 0.0, lw=2, head_width=0.04, head_length=0.05, fc='gray', ec='gray',
                  linestyle='dashed')
        plt.arrow(0.70, -0.2, 0.0, -0.15, lw=2, head_width=0.04, head_length=0.05, fc='gray', ec='gray',
                  linestyle='dashed')
        plt.text(0.65, -0.15, 'Input rigth: left', rotation='horizontal', fontsize='9', color='gray')
    elif input == 'right':
        # input right
        print 'X'
        plt.arrow(0.9, -0.2, -0.15, 0.0, lw=2, head_width=0.04, head_length=0.05, fc='gray', ec='gray',
                  linestyle='dashed')
        plt.arrow(0.7, -0.2, 0.0, 0.15, lw=2, head_width=0.04, head_length=0.05, fc='gray', ec='gray',
                  linestyle='dashed')
        plt.text(0.6, -0.30, 'Input right: right', rotation='horizontal', fontsize='9', color='gray')
    elif input == 'forward':
        # input forward
        plt.arrow(0.9, -0.2, -0.3, 0.0, lw=2, head_width=0.04, head_length=0.05, fc='gray', ec='gray',
                  linestyle='dashed')
        plt.text(0.5, -0.15, 'Input right: forward', rotation='horizontal', fontsize='9', color='gray')
    elif input == None or 'None':
        pass
    else:
        raise Exception('Invalid percept input')

def percept_input_oncoming(direction):
    """Represents the input percept of actual oncoming traffic approaching.
       Valid inputs: oncoming traffic from left, forward or right dirrection.
       Percepts taken from perspective of agent.
    """
    if direction == 'left':
        # oncoming left
        plt.arrow(-0.8, 0.3, 0.4, 0.0, head_width=0.04, head_length=0.05, fc='b', ec='b')
        plt.text(-0.8, 0.35, 'Oncoming left', rotation='horizontal', fontsize='9')
    elif direction == 'forward':
        # oncoming forward
        plt.arrow(0.05, 1.2, 0.0, -0.45, head_width=0.04, head_length=0.05, fc='b', ec='b')
        plt.text(-0.05, 1.45, 'Oncoming forward', rotation='vertical', fontsize='9')
    elif direction == 'right':
        # oncoming right
        plt.arrow(0.9, 0.3, -0.4, 0.0, head_width=0.04, head_length=0.05, fc='b', ec='b')
        plt.text(0.45, 0.35, 'Oncoming right', fontsize='9')
    elif direction == None or 'None':
        pass
    else:
        raise Exception('Invalid oncomming traffic percept')

def waypoint(direction):
    """Represents the current waypoint of agent.
       Valid inputs: waypoint turning left, right or moving forward
       Percept taken from perspective of agent.
    """
    # waypoint foward
    if direction == 'forward':
        plt.arrow(0.05, -0.5, 0.0, 0.3, head_width=0.04, head_length=0.05, fc='k', ec='k', linestyle='solid', linewidth=3.5)
        plt.text(-0.1, -0.6, 'Waypoint', fontsize='9', fontweight='bold')
    # waypoint right
    elif direction == 'right':
        plt.arrow(0.05, -0.5, 0.0, 0.15, head_width=0.04, head_length=0.05, fc='k', ec='k', linestyle='solid', linewidth=3.5)
        plt.arrow(0.05, -0.3, 0.1, 0.0, head_width=0.04, head_length=0.05, fc='k', ec='k', linestyle='solid',
                  linewidth=3.5)
        plt.text(-0.1, -0.6, 'Waypoint', fontsize='9', fontweight='bold')
    elif direction == 'left':
        plt.arrow(0.05, -0.5, 0.0, 0.15, head_width=0.04, head_length=0.05, fc='k', ec='k', linestyle='solid', linewidth=3.5)
        plt.arrow(0.05, -0.3, -0.1, 0.0, head_width=0.04, head_length=0.05, fc='k', ec='k', linestyle='solid',
                  linewidth=3.5)
        plt.text(-0.1, -0.6, 'Waypoint', fontsize='9', fontweight='bold')

    elif direction == None or 'None':
        pass
    else:
        raise Exception('Invalid waypoint percept')

def maxQ_action(action):
    """Writes a message text indicating the action that maximizes Q given the observed percepts"""
    # maxQ action enclosing rectangle
    maxq_rect = plt.Rectangle((0.45, 1.2), 0.55, 0.55, fill=False)
    plt.gca().add_patch(maxq_rect)
    fs = 9
    # maxQ action forward
    if action == 'forward':
        plt.arrow(0.7, 1.35, 0.0, 0.2, head_width=0.04, head_length=0.05, fc='darkgreen', ec='darkgreen', linestyle='solid',
                  linewidth=3.5)
        plt.text(0.5, 1.25, 'MaxQ action', fontsize=fs, fontweight='bold', color='darkgreen')
        plt.text(0.55, 1.65, 'Forward', fontsize=fs, fontweight='normal', color='darkgreen')

    # maxQ action left
    elif action == 'left':
        plt.arrow(0.7, 1.35, 0.0, 0.15, head_width=0.04, head_length=0.05, fc='darkgreen', ec='darkgreen', linestyle='solid',
                  linewidth=3.5)
        plt.arrow(0.7, 1.55, -0.1, 0.0, head_width=0.04, head_length=0.05, fc='darkgreen', ec='darkgreen',
                  linestyle='solid',
                  linewidth=3.5)
        plt.text(0.5, 1.25, 'MaxQ action', fontsize=fs, fontweight='bold', color='darkgreen')
        plt.text(0.6, 1.65, 'Left', fontsize=fs, fontweight='normal', color='darkgreen')

    # maxQ action right
    elif action == 'right':
        plt.arrow(0.7, 1.35, 0.0, 0.15, head_width=0.04, head_length=0.05, fc='darkgreen', ec='darkgreen', linestyle='solid',
                  linewidth=3.5)
        plt.arrow(0.7, 1.55, 0.1, 0.0, head_width=0.04, head_length=0.05, fc='darkgreen', ec='darkgreen',
                  linestyle='solid',
                  linewidth=3.5)
        plt.text(0.5, 1.25, 'MaxQ action', fontsize=fs, fontweight='bold', color='darkgreen')
        plt.text(0.6, 1.65, 'Right', fontsize=fs, fontweight='normal', color='darkgreen')

    # maxQ action None (idle)
    elif action == None or 'None':
        plt.text(0.63, 1.45, 'Idle', fontsize='12', fontweight='bold', color='darkgreen')
        plt.text(0.5, 1.25, 'MaxQ action', fontsize='9', fontweight='bold', color='darkgreen')
        plt.text(0.6, 1.65, 'None', fontsize=fs, fontweight='normal', color='darkgreen')
    else:
        raise Exception('Invalid maxQ action')

#State = (waypoint, inputs['light'], inputs['oncoming'], inputs['left'], inputs['right'])
#{'avail_actions': [('forward', '-0.44'), ('None', '0.19'), ('right', '-0.24'), ('left', '-0.24')],
# 'inp_light': 'red', 'inp_left': 'forward', 'inp_right': None, 'inp_oncoming': 'forward',
# 'waypoint': 'left', 'maxQaction': 'None'}

def legended_description(obs):
    fs = 8
    xpos = 0.4
    ypos = 1.1
    plt.text(xpos-0.1, ypos, '(Action, MaxQ) chosen from:', rotation='horizontal', fontsize=fs,color='blue')
    for i, act in enumerate(obs['avail_actions']):
        plt.text(xpos+0.1, (ypos-0.1)-i*0.1, act, rotation='horizontal', fontsize=fs,color='blue')

def act_policy_figure(observation):
    """Generates a figure representation of the Q-table entry or policy observation"""
    create_canvas('on')
    intersection_point()
    waypoint(observation['waypoint'])
    percept_input_oncoming(observation['inp_oncoming'])
    percept_input_left(observation['inp_left'])
    percept_input_right(observation['inp_right'])
    percept_traffic_light(observation['inp_light'])
    maxQ_action(observation['maxQaction'])
    legended_description(observation)

# Generate a set of policy observations extracted from Q-table
sample = qtable_sample('sim_improved-learning.txt', 6)
plt.figure(1, figsize=(15, 8))
nrows = 2
ncols = 3
for fig_num, observation in enumerate(sample):
    plt.subplot(nrows, ncols, fig_num+1)
    act_policy_figure(observation)
    plt.tight_layout()
plt.show()
