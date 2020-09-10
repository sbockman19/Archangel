from importdbexample import updateTasks, updatePhys, updateWards

def main():
	# this will first pull status info from devices to get new/completed tasks, updated clock in/clock out to see which physicians are available, etc
	TASKS = updateTasks()
	WARDS = updateWards()
	PHYS = updatePhys()
	# now we have the updated tables of tasks, physicains, wards
	# we can now implement the matching algorithm

	# we will first look at the oldest task

	task = TASKS[-1]
	print(TASKS,task.task_skill_level)

	# filter physicians by skill level

	p = [j for i,j in enumerate(PHYS) if value(j.physician_skill_level) >= value(task.task_skill_level)]

	# filter wards by HW level required

	# print(WARDS[0].ward_authorization_level)
	w = [m for l,m in enumerate(WARDS) if value(m.ward_authorization_level) >= value(task.task_level_required)]

	print("[NOTIFICATION TO PHYSICIAN PHONE], physician_name:", p[0].physician_id, "needs to go to" , w[0].ward_room, "immediately to", task.task_description, "\n", "[BUTTON] ACCEPT OR DECLINE")

def value(sl):
	"""
	ex: sl is V5
	return: 225
	"""
	# print(sl[0])
	r = 98-ord(sl[0]) 
	# print(ord(sl[0]),r+int(sl[1]))
	return r+int(sl[1])

main()


# task is created (update task queue)
# physican is searched for based on x y z (from task)
# phsycians U is selected based on x, z (y confition not m et)
# notificaion sent to Physician




