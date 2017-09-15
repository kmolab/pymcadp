disp ('Program started')
vrep=remApi('remoteApi');
vrep.simxFinish(-1); % just in case, close all opened connections
clientID = vrep.simxStart('127.0.0.1',19997,true,true,5000,5); % Connect to V-REP
if clientID ~= -1
    disp ('Connected to remote API server')
    ret = vrep.simxStartSimulation(clientID,vrep.simx_opmode_oneshot);
    [ret,handle] = vrep.simxGetObjectHandle(clientID,'Revolute_joint',vrep.simx_opmode_oneshot_wait);
    [ret,handle1] = vrep.simxGetObjectHandle(clientID,'Revolute_joint0',vrep.simx_opmode_oneshot_wait);
    [ret,handle_output] = vrep.simxGetObjectHandle(clientID,'Cuboid1',vrep.simx_opmode_oneshot_wait);

    a1 = 0.2;
    a2 = 0.05;

    y = 0.05:-0.01:-0.21;
    z = generate_trajectory(0.42857,0.2714,y);

    disp('Trajectory to track:')
    for i=1:length(y)
        disp(sprintf('y = %.2f, z = %.2f', y(i), z(i)))
    end
    
    for i=1:length(y)
        theta = RR_inverse_kinematics(y(i), z(i), a1, a2);
        theta1 = theta(1); theta2 = theta(2);
        forwk_position = RR_forward_kinematics(a1,a2,theta1,theta2);

        position = [0,0,0];
        while ~check_position(position(2), position(3), forwk_position(2), forwk_position(3))
           ret = vrep.simxSetJointTargetPosition(clientID,handle,theta1*pi/180,vrep.simx_opmode_oneshot);
           ret = vrep.simxSetJointTargetPosition(clientID,handle1,theta2*pi/180,vrep.simx_opmode_oneshot);
           [ret,position] = vrep.simxGetObjectPosition(clientID,handle_output,-1,vrep.simx_opmode_streaming);
        end
        disp(sprintf('Angles: %.2f, %.2f',theta1, theta2));
        disp(sprintf('End Effector Position: %.2f, %.2f, %.2f', position(1), position(2), position(3)));
    end
    ret = vrep.simxStopSimulation(clientID,vrep.simx_opmode_oneshot)
end