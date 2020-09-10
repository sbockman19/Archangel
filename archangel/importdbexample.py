## Import DB_Example excel to set variables to initialize within classDefinitions.py

from classDefinitions import Ward, Hospital, Physicians, Task
import pandas as pd

wardData = pd.read_excel("ArchangelDBexample.xlsx", sheet_name = "Ward")
taskData = pd.read_excel("ArchangelDBexample.xlsx", sheet_name = "Tasks")
physData = pd.read_excel("ArchangelDBexample.xlsx", sheet_name = "HealthWorker")

# print(wardData.columns[0],wardData.iat[0,0])
# print(taskData.iat[0,len(taskData.columns)-1])

def updateTasks():
	taskQueue = [] # task queue imported from db example
	#later this will need frequent syncing from all devices
	for h,i in enumerate(taskData.columns):
		try:
			tid = taskData.iat[h,0]
			# if tid in taskQueue: # make sure no duplicate tasked added
			# 	return taskQueue
		except:
			return taskQueue
		tdata=[]
		for k in range(len(taskData.columns)):
			tdata.append(taskData.iat[h,k])
		taskn = Task(tdata)
		taskQueue.append(taskn)
	return taskQueue

def updateWards():
	wards = [] # ward list imported from db example
	#later this will need frequent syncing from all devices
	for h,i in enumerate(wardData.columns):
		try:
			wid = wardData.iat[h,0]
			# if tid in taskQueue: # make sure no duplicate tasked added
			# 	return taskQueue
		except:
			return wards
		wdata=[]
		for k in range(len(wardData.columns)):
			wdata.append(wardData.iat[h,k])
		wardn = Ward(wdata)
		wards.append(wardn)
	return wards

def updatePhys():
	phys = [] # physicians list imported from db example
	#later this will need frequent syncing from all devices
	for h,i in enumerate(physData.columns):
		try:
			pid = physData.iat[h,0]
			# if pid in phys: # make sure no duplicate phys added
			# 	return phystq = updateTasks()
		except:
			return phys
		pdata=[]
		for k in range(len(physData.columns)):
			pdata.append(physData.iat[h,k])
		physn = Physicians(pdata)
		phys.append(physn)
	return phys


# tq = updateTasks()
# print("tq",len(tq),tq)
# p = updatePhys()
# print("p",len(p),p)
# w = updateWards()
# print("w",len(w),w)
# print(w[0].ward_beds)
# print(p[0].physician_counter_daysworked)