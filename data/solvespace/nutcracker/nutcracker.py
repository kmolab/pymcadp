import vrep
import sys, math
# child threaded script: 
# 內建使用 port 19997 若要加入其他 port, 在  serve 端程式納入
#simExtRemoteApiStart(19999)
 
vrep.simxFinish(-1)
 
clientID = vrep.simxStart('127.0.0.1', 19997, True, True, 5000, 5)

'''
connectionAddress: The IP address where the server is (toyest the server address with V-REP).
connectionPort: Port to which there is connection.
waitUntilConnected: If True, then function is blocked on connection time or yet timeout time will not end.
doNotReconnectOnceDisconnected: If True, then communication flow does not try to perepodsoyedinitsya in case of connection loss.
timeOutInMs: Connection timeout in milliseconds (for the first connection).
commThreadCycleInMs: Specifies how often there has to be exchange of data packets. Reduction of this number increases sensitivity, and as value it is by default recommended 5.
'''

#啟動模擬
vrep.simxStartSimulation(clientID, vrep.simx_opmode_oneshot_wait)
 
if clientID!= -1:
    print("Connected to remote server")
else:
    print('Connection not successful')
    sys.exit('Could not connect')
 
errorCode,Revolute_joint_handle=vrep.simxGetObjectHandle(clientID,'right_hinge_base_joint',vrep.simx_opmode_blocking)
 
errorCode0,Revolute_joint_handle0=vrep.simxGetObjectHandle(clientID,'Revolute_joint0',vrep.simx_opmode_oneshot_wait)
 
errorCode0,Revolute_joint_handle0=vrep.simxGetObjectHandle(clientID,'Revolute_joint0',vrep.simx_opmode_oneshot_wait)
 
if errorCode == -1:
    print('Can not find left or right motor')
    sys.exit()
    
#vrep.simSetJointMode(Revolute_joint_handle,vrep.sim_jointmode_passive,0)
vrep.simxSetStringSignal(clientID,"jointModeCmd","joint1ToIk",vrep.simx_opmode_oneshot);
 
deg = math.pi/180

#errorCode=vrep.simxSetJointTargetVelocity(clientID,Revolute_joint_handle,2, vrep.simx_opmode_oneshot_wait)

def setJointPosition(incAngle, steps):
    for i  in range(steps):
        errorCode=vrep.simxSetJointPosition(clientID, Revolute_joint_handle, i*incAngle*deg, vrep.simx_opmode_oneshot)
        vrep.simxSynchronousTrigger(clientID)
        
# 每步 10 度, 轉兩圈
setJointPosition(-1, 40)
# 每步 1 度, 轉兩圈
#setJointPosition(1, 720)
# 每步 0.1  度, 轉720 步
#setJointPosition(0.1, 720)

#vrep.simxFinish(clientID)

'''
三軸同動時
simxPauseCommunication(clientID,1);
simxSetJointPosition(clientID,joint1Handle,joint1Value,simx_opmode_oneshot);
simxSetJointPosition(clientID,joint2Handle,joint2Value,simx_opmode_oneshot);
simxSetJointPosition(clientID,joint3Handle,joint3Value,simx_opmode_oneshot);
simxPauseCommunication(clientID,0);
'''

 
for i in range(360):
    vrep.simxSynchronous(clientID,True)
    vrep.simxPauseCommunication(clientID,True)
    vrep.simxSetJointPosition(clientID, Revolute_joint_handle, 10*deg, vrep.simx_opmode_oneshot)
    vrep.simxSetJointPosition(clientID, Revolute_joint_handle0, 10*deg, vrep.simx_opmode_oneshot)
    vrep.simxPauseCommunication(clientID, False)
    vrep.simxSynchronous(clientID, False)
 
    vrep.simxSynchronous(clientID,True)
    vrep.simxPauseCommunication(clientID,True)
    vrep.simxSetJointPosition(clientID, Revolute_joint_handle, -10*deg, vrep.simx_opmode_oneshot)
    vrep.simxSetJointPosition(clientID, Revolute_joint_handle0, -10*deg, vrep.simx_opmode_oneshot)
    vrep.simxPauseCommunication(clientID, False)
    vrep.simxSynchronous(clientID, False)
