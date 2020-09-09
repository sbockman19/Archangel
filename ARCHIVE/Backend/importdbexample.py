## Import DB_Example excel to set variables to initialize within classDefinitions.py

from classDefinitions import Admin, Hospital, Physicians
import pandas as pd

db = pd.read_excel("ArchangelDBexample.xlsx")
# import Excel #import medical excel file

"""
# Import Hospital information from excel table as Hospital Class and pass in corresponding columns of excel table
Hospital Table = Hosptial(Column1, Column2, ...)

# Import Ward information from excel table as Ward Class and pass in corresponding columns of excel table
Ward Table = Ward(Column1,Column2, ...)

# Import Task1 information from excel table as Task Class and pass in corresponding columns of excel table
Task1 Table = Task(Column1,Column2, ...)

# Import Physician1 information from excel table as Physicians Class and pass in corresponding columns of excel table
Physician1 Table = Physicians(Column1,Column2, ...)

"""
#created physician table
#created task queue
#created ward table
IMAC = Hospital(importdbexample[sheet1])

def updateTasks():
	taskQueue = {} # task queue imported from db example
	#later this will need frequent syncing from all devices
	for i in importdbexample[sheet2]:
		task = Task(i)
		if i not in taskQueue:
			taskQueue.update(task)
		if i in taskQueue:
			if i[5] == "complete": # index n is status of task and arbitrarily marked, arbitrary name "complete" as well
				del taskQueue[task]

def updateWards():
	IMACwards = {} # wards imported from db example
	#later this will need frequent syncing from all devices
	for j in importdbexample[sheet3]:
		if j not in IMACwards:
			IMACwards.update(Ward(j))
		if j in IMACwards:
			IMACwards.update(Ward(j))

def updatedPhys():
	phys = {}
	for q in importdbexample[sheet4]:
		if q not in phys:
			phys.update(Physicians(q))