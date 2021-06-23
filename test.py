import b0RemoteApi
print ("importing successful!")

with b0RemoteApi.RemoteApiClient('b0RemoteApi_V-REP-addOn','b0RemoteApiAddOn') as client:  #This line defines the client, which provides all functions of the remote API
# the function list can be found here: https://www.coppeliarobotics.com/helpFiles/en/b0RemoteApi-functionList.htm
	 
	_,jointHandle = client.simxGetObjectHandle("IRB4600_joint1",client.simxServiceCall()) #use client to get the handle of the robot base joint
	client.simxStartSimulation(client.simxServiceCall()) #use client to start the simulation
	while(True):
		_,jointPosition = client.simxGetJointPosition(jointHandle,client.simxServiceCall()) #use client to retrieve the joint position
		print(jointPosition) #print the joint position to console window


