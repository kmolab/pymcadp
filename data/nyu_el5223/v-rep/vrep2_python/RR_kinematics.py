#!/usr/bin/env python

import math

def forward_kinematics(a1,a2,theta1,theta2):
    return [0,
        -(a1*math.sin(theta1*math.pi/180)+(a2*math.sin((theta1+theta2)*math.pi/180))),
        0.05+a1*math.cos(theta1*math.pi/180)+(a2*math.cos((theta1+theta2)*math.pi/180))]

def inverse_kinematics(y, z, a1, a2):
    theta2=math.acos((pow(y,2)+pow((z-0.05),2)-pow(a1,2)-pow(a2,2))/(2*a1*a2))
    theta1=-(math.atan2(z-0.05,-y)-math.atan2(a1+a2*math.cos(theta2),a2*math.sin(theta2)))

    return [theta1*180/math.pi, theta2*180/math.pi]