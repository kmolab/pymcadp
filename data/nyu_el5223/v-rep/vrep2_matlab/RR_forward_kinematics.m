function [ p ] = RR_forward_kinematics( a1, a2, theta1, theta2 )
    p(1) = 0;
    p(2) = -(a1*sin(theta1*pi/180) + (a2*sin((theta1+theta2)*pi/180)));
    p(3) = 0.05 + a1*cos(theta1*pi/180) + (a2*cos((theta1+theta2)*pi/180));
end