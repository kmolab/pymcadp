#!/usr/bin/env python

import vrep
import math

from RR_kinematics import *

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
    theta1 = 40
    theta2 = -80

    forwk_position = forward_kinematics(a1,a2,theta1,theta2)
    forwk_position = [round(x,2) for x in forwk_position]
    position = [0,0,0]
    print("Sending angles: {}, {}".format(theta1, theta2))
    while position != forwk_position:
    	returncode = vrep.simxSetJointTargetPosition(clientID,handle,theta1*math.pi/180,vrep.simx_opmode_oneshot)
    	returncode1 = vrep.simxSetJointTargetPosition(clientID,handle1,theta2*math.pi/180,vrep.simx_opmode_oneshot)
    	_,position = vrep.simxGetObjectPosition(clientID,handle_output,-1,vrep.simx_opmode_streaming)
    	position = [round(x,2) for x in position]
    print("Current End Effector Position: {}".format(position))
    print("Calculated Forward Kinematics Position: {}".format(forwk_position))
    _ = vrep.simxStopSimulation(clientID,vrep.simx_opmode_oneshot)
