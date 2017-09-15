#!/usr/bin/env python

import vrep
import math

from RR_kinematics import *

def line(m,c,x):
    return [m*z+c for z in x]

print ('Program started')
vrep.simxFinish(-1) # just in case, close all opened connections
clientID = vrep.simxStart('127.0.0.1',19997,True,True,5000,5) # Connect to V-REP

if clientID != -1:
    print ('Connected to remote API server')
    _ = vrep.simxStartSimulation(clientID,vrep.simx_opmode_oneshot)
    _,handle = vrep.simxGetObjectHandle(clientID,"Revolute_joint",vrep.simx_opmode_blocking)
    _,handle1 = vrep.simxGetObjectHandle(clientID,"Revolute_joint0",vrep.simx_opmode_blocking)
    _,handle_output = vrep.simxGetObjectHandle(clientID,"Cuboid1",vrep.simx_opmode_blocking)

    a1 = 0.2
    a2 = 0.05

    y = [0.05-(float(l)/50) for l in range(14)]
    y = [round(temp,3) for temp in y]

    z = line(0.42857,0.2714,y)
    z = [round(temp,3) for temp in z]

    print("Trajectory to track:")
    for i in range(len(y)):
        print("y = {}, z = {}".format(y[i], z[i]))

    for i in range(len(y)):
        theta1,theta2 = inverse_kinematics(y[i], z[i], a1, a2)

        forwk_position = forward_kinematics(a1,a2,theta1,theta2)
        forwk_position = [round(x,3) for x in forwk_position]
        position = [0,0,0]
        while position != forwk_position:
           returncode = vrep.simxSetJointTargetPosition(clientID,handle,theta1*math.pi/180,vrep.simx_opmode_oneshot)
           returncode1 = vrep.simxSetJointTargetPosition(clientID,handle1,theta2*math.pi/180,vrep.simx_opmode_oneshot)
           _,position = vrep.simxGetObjectPosition(clientID,handle_output,-1,vrep.simx_opmode_streaming)
           position = [round(x,3) for x in position]
        print("Angles: {:.2f}, {:.2f}".format(theta1, theta2))
        print("End Effector Position: {}".format(position))

    _ = vrep.simxStopSimulation(clientID,vrep.simx_opmode_oneshot)
