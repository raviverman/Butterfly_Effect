# Illustration of butterfly effect in Chaos Theory

# Situation
# Alex has got letter of acceptance from a popular university.
# He has 5 subjects from which he can do his major. He has a year
# to decide his choice of subject. During that year, he meets 
# his parents and several friends with different interests.
# All these people has different level of influence on Alex
# which will help him decide the subject. The final subject 
# chosen depends heavily upon the initial set conditions. 
# 
# See more : https://en.wikipedia.org/wiki/Butterfly_effect

import numpy as np
import random as r
import pdb 
import matplotlib.pyplot as plt

def assignSign( list_x ):
    return np.array(list(map(lambda x: x* (-1 if \
    r.random() > 0.5 else 1), list_x)))

def willMeet( bias = 0.5 ):
    if( r.random() < bias ):
        return True
    return False

# Initializing interests
subjects = ['Maths', 'Business St. ', 'Economics', 'Geography', 'Science']
# alex = np.random.random(5)
alex = np.zeros(5) 
# father = np.random.random(5)
father = np.array([0.862, 0.235, -0.522, -0.856, 0.952])
# mother = np.random.random(5)
mother = np.array([-0.562, -0.835, 0.502, 0.356, 0.452])

friends = np.random.random((5,5)) 
for i in range(0, len(friends)):
    friends[i] = assignSign(friends[i]) 

# friends = np.array([
#     [0.762, 0.235,  0.222,  0.156, 0.852],
#     [0.862, -0.600, -0.502, -0.856, 0.752],
#     [0.062, 0.635, -0.422,  0.256, 0.532],
#     [-0.662, -0.535, -0.502, -0.726, -0.452],
#     [-0.762, 0.735, -0.122, 0.246, -0.252]
    # ])

f_influence = 0.4
m_influence = 0.2
fr_influence = np.random.random(5) 

# Probability of meeting a person 
meet_bias = { 'father': float(0.6),
              'mother': float(0.8),
              'friend_1': float(0.5),
              'friend_2': float(0.5),
              'friend_3': float(0.5),
              'friend_4': float(0.5),
              'friend_5': float(0.5),
             } 
interest = np.array([alex])
# doing stuff
day = 365
# for all days
for i in range(1, day):
    # 
    add = np.zeros(5)
    # will meet Mom
    if( willMeet(meet_bias['mother'])):
        add += mother * m_influence
    # meet father
    if( willMeet(meet_bias['father'])):
        add += father * f_influence
    for i, fri in enumerate(friends):
        if( willMeet(meet_bias['friend_' + str(i+1)])):
            add += fri * fr_influence[i]
    alex += add
    interest = np.append(interest, [alex], axis=0)

# print interest
days = np.linspace(1, day, day)
# print days
# print interest[:, 0]
# plt.subplot(421)
plt.plot(days, interest[:, 0], label=subjects[0] )
plt.plot(days, interest[:, 1], label=subjects[1] )
plt.plot(days, interest[:, 2], label=subjects[2] )
plt.plot(days, interest[:, 3], label=subjects[3] )
plt.plot(days, interest[:, 4], label=subjects[4] )
plt.legend(subjects)
plt.title('Interests grown in ' + str(day) + ' days')

# Interest Chart
legends = ['father', 'mother', 'friend_1', 'friend_2', 'friend_3', 'friend_4', 'friend_5']
plt.figure()
plt.title("Interests of people in contact")
chart = 421
plt.subplot(chart)
plt.bar(subjects,father, label="father")
plt.legend([legends[0]])

chart +=1
plt.subplot(chart)
plt.bar(subjects, mother)
plt.legend([legends[1]])


for i,friend in enumerate(friends):
    chart+=1
    plt.subplot(chart)
    plt.bar(subjects,friend)
    plt.legend([legends[i+2]])

plt.figure()
plt.title("Influence Chart")
plt.bar(legends, np.append(np.array([f_influence, m_influence]), fr_influence  ))
plt.show()