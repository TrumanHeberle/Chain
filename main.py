from random import random
from math import floor, log, e
import numpy as np

MAX = 10
MIN = 1
NOISE = [1/100,1/100,1/100]
POWERS = [3,1,2]
DIFF = MAX-MIN
TRUE_FRAMES = 20

frames = []
for j in range(TRUE_FRAMES):
    x1 = MIN + random()*DIFF
    x2 = MIN + random()*DIFF
    x3 = MIN + random()*DIFF
    nx1 = x1+DIFF*NOISE[0]*random()-DIFF*NOISE[0]/2
    nx2 = x2+DIFF*NOISE[0]*random()-DIFF*NOISE[0]/2
    nx3 = x3+DIFF*NOISE[0]*random()-DIFF*NOISE[0]/2
    z = (nx1**POWERS[0])*(nx2**POWERS[1])*(nx3**POWERS[2])
    frames.append([x1, x2, x3, z])

def 

def getPowers(frames):
    vals = [[],[],[]]
    for ai in range(1,len(frames)):
        for bi in range(ai+1, len(frames)):
            for ci in range(bi+1, len(frames)):
                for di in range(ci+1, len(frames)):
                    for ei in range(di+1, len(frames)):
                        for fi in range(ei+1, len(frames)):
                            p1 = [log(abs(frames[ai][n]/frames[bi][n]),e) for n in range(len(frames[ai]))]
                            p2 = [log(abs(frames[ci][n]/frames[di][n]),e) for n in range(len(frames[ci]))]
                            p3 = [log(abs(frames[ei][n]/frames[fi][n]),e) for n in range(len(frames[ei]))]
                            zm = np.matrix([[p1[3]],[p2[3]],[p3[3]]])
                            xm = np.matrix([[p1[0],p1[1],p1[2]],[p2[0],p2[1],p2[2]],[p3[0],p3[1],p3[2]]])
                            avals = np.matmul(np.linalg.inv(xm),zm)
                            vals[0].append(avals.item((0,0)))
                            vals[1].append(avals.item((1,0)))
                            vals[2].append(avals.item((2,0)))
    return [np.mean(li) for li in vals]

print(getPowers(frames))
