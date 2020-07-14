#print("hello world")

# plan to use SOAP APIs because they are more secure


class Hospital():
	"""docstring for hospital:
		this is the hospital information

		attributes:
			name
			address
			
		methods:
			get_capacity, gets number of specific hospital beds
	"""
	def __init__(self, hospital_id):
		super(Hopital, self).__init__()
		self.hospital_id = hospital_id

	def get_capacity():
		"""
		inputs: none

		actions:
			pull current information from DB

		returns:
			table of sortable hospital beds
		"""
		pass

class Admin():
	"""docstring for Admin:
		description: the admin views available physicians, assigns roles, schedules, timing of events

		attributes:
			indentification
			hospital wing

		methods:
			write_physician_data, add physician data to database
			show_all, view available physicians
			search, search physicians by skill
			sort, sort physicians by skill
			filter, filter physicians by skill
			add_new, add physician information

	"""
	def __init__(self, arg):
		super(Admin, self).__init__(admin_id)
		self.id = admin_id

	def write_physician_data(pcp_id, name, skill, training):
		"""
		input:
			PCP ID
			name
			Skill level
			Trainings
		
		actions:
			message: successful addition

		return: none 

		"""
		print("write physician data to database")

		pass

	def get_physician_data(pcp_id):
		"""
		optional inputs:
			active (will search for active physicians)

		returns:
			if no input, returns all physician data

		"""

		#get data 

		#sort data

		#return data

		print("get request physician data")

		pass

class Physicians():
	"""docstring for Physicians
		description: physician is a doctor, PA, surgen, etc

		attributes:
			identification
			skill level
			status (clocked in, clocked out)
			Hospital

		methods:
			get_information, returns individual physician information


	"""
	def __init__(self, phys_id):
		super(Physicians, self).__init__()
		self.id = phys_id
		self.hospital_id = 
		self.status = status

	def clock_in():
		"""
		physician clocks in/out to/from work

		inputs: none
		
		actions:
			communicates with database to log information
			app pop-up stating successful login

		returns:
			nothing
		"""
		print("clocked in")
		pass

