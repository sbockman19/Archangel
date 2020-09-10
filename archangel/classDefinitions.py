	#print("hello world")

# plan to use SOAP APIs because they are more secure

# https://github.com/anmolsaxena10/myHospital

class Hospital():
	"""docstring for hospital:
		this is the hospital information

		attributes:
			hospital_id
			hospital_address
			hospital_specialties ([list of specialties])
			hospital_wards_per_specialty
			hospital_daily_avg)specialty_ward_capacity
			hospital_avg_specialty_physician_capacity
			
		methods:
			get_capacity, gets number of specific hospital beds
	"""
	def __init__(self, hospital_id, hospital_address, hospital_specialties, hospital_wards_per_specialty, hospital_daily_avg_specialty_ward_capacity, hospital_avg_specialty_physician_capactiy):
		super(Hopital, self).__init__()
		self.hospital_id = hospital_id
		self.hospital_address = hospital_address
		self.hospital_specialties = hospital_specialties
		self.hospital_wards_per_specialty = hospital_wards_per_specialty
		self.hospital_daily_avg_specialty_ward_capacity = hospital_daily_avg_specialty_ward_capacity
		self.hospital_avg_specialty_physician_capactiy = hospital_avg_specialty_physician_capactiy
		
	def get_capacity():
		"""
		inputs: none

		actions:
			pull current information from DB

		returns:
			table of sortable hospital beds
		"""
		pass

class Ward():
	"""docstring for ward:
		this is the class for a hospital room

		attributes:
			ward_id
			hospital_id
			ward_classification
			ward_room
			ward_beds
			ward_m3
			ward_specialty
			ward_covid_prepared
			ward_covid_attending
			ward_ventilation_level
			ward_hygiene_level
			ward_min_physicians
			ward_max_physicians
			ward_authorization_level
			ward_max_patients
			ward_availability
			ward_average_capacity
			ward_count_phsician
			ward_count_patient

		methods:
	"""
	def __init__(self, wardData):
		# ward_id, hospital_id, ward_classification, ward_room, ward_beds, ward_m3, ward_specialty, ward_covid_prepared, ward_covid_attending, ward_ventilation_level, ward_hygiene_level, ward_min_physicians, ward_max_physicians, ward_authorization_level, ward_max_patients, ward_availability, ward_average_capacity, ward_count_patient, ward_count_phsician):
		self.ward_id = wardData[0] #ward_id
		self.hospital_id = wardData[1] #hospital_id
		self.ward_classification = wardData[2] #ward_classification
		self.ward_room = wardData[3] #ward_room
		self.ward_beds = wardData[4] #ward_beds
		self.ward_m3 = wardData[5] #ward_m3
		self.ward_sepcialty = wardData[6] #ward_sepcialty
		self.ward_covid_prepared = wardData[7] #ward_covid_prepared
		self.ward_covid_attending = wardData[8] #ward_covid_attending
		self.ward_ventilation_level = wardData[9] #ward_ventilation_level
		self.ward_hygiene_level = wardData[10] #ward_hygiene_level
		self.ward_min_physicians = wardData[11] #ward_min_physicians
		self.ward_max_physicians = wardData[12] #ward_max_physicians
		self.ward_authorization_level = wardData[13] #ward_authorization_level
		self.ward_max_patients = wardData[14] #ward_max_patients
		self.ward_availability = wardData[15] #ward_availability
		self.ward_average_capacity = wardData[16] #ward_average_capacity
		self.ward_count_physician = wardData[17] #ward_count_physician
		self.ward_count_patient = wardData[18] #ward_count_patient


	def check_ward():
		"""checks status of ward

		returns available, busy, ready to be cleaned
		"""
		pass


class Task():
	"""docstring for Task:
		description: task requires a role, schedule, speciality and can be created by any physicisan

		attributes:
			admin_id
			task_id
			task_location (NOTE: NOT IN EXCEL TABLE)
			task_description
			task_level_required
			task_availability
			task_response
			task_stress
			task_max_hours
			task_age_restrictions
			task_regulatory_protocol
			task_specialty
			task_skill_level

		methods:
			write_physician_data, add physician data to database
			show_all, view available physicians
			search, search physicians by skill
			sort, sort physicians by skill
			filter, filter physicians by skill
			add_new, add physician information

	"""
	def __init__(self, taskdata):
		# attributes = [admin_id, task_id, task_location, task_description, task_level_required, task_availability, task_response, task_stress, task_max_hours, task_age_restriction, task_regulatory_protocol, task_specialty, task_skill_level]
		# super(self).__init__(self)
		# self.admin_id = admin_id
		# self.task_id = task_id
		# self.task_location = task_location
		# self.task_description = task_description
		# self.task_level_required = task_level_required
		# self.task_availability = task_availability
		# self.task_response = task_response
		# self.task_stress = task_stress
		# self.task_max_hours = task_max_hours
		# self.task_age_restriction = task_age_restriction
		# self.task_regulatory_protocol = task_regulatory_protocol
		# self.task_specialty = task_specialty
		# self.task_skill_level = task_skill_level
		self.task_id = taskdata[0]#task_id
		self.task_description = taskdata[1]#task_description
		self.task_level_required = taskdata[2]#task_level_required
		self.task_availability = taskdata[3]#task_availability
		self.task_response = taskdata[4]#task_response
		self.task_stress = taskdata[5]#task_stress
		self.task_max_hours = taskdata[6]#task_max_hours
		self.task_age_restriction = taskdata[7]#task_age_restriction
		self.task_regulatory_protocol = taskdata[8]#task_regulatory_protocol
		self.task_specialty = taskdata[9]#task_specialty
		self.task_skill_level = taskdata[10]#task_skill_level


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
			physician_id
			hospital_id
			physician_status (clocked in, clocked out)
			physician_skill_level
			physician_position
			physician_specialty
			physician_hour_availability
			physician_day_availability
			physician_counter_daysworked
			physician_counter_nightsworked
			physician_regular_ward_flag
			physician_icu
			physician_emergency
			physician_last_access
			physician_last_checkin
			physician_last_checkout
			physician_last_ward_visited
			physician_covid_symptom
			physician_last_covid_check


		methods:
			get_information, returns individual physician information
			write_to_db, params 
	"""
	def __init__(self, physData): #phys_id, hospital_id, physician_status, physician_skill_level, physician_position, physician_specialty, physician_hour_availability, physician_day_availability, physician_counter_daysworked, physician_counter_nightsworked, physician_regular_ward_flag, physician_icu, physician_emergency, physician_last_access, physician_last_checkin, physician_last_checkout, physician_last_ward_visited, physician_covid_symptom, physician_last_covid_check):
		self.physician_id = physData[0] #physician_id
		# self.hospital_id = physData[1] #hospital_id
		self.physician_status = physData[1] #physician_status
		self.physician_skill_level = physData[2] #physician_skill_level
		self.physician_position = physData[3] #physician_position
		self.physician_specialty = physData[4] #physician_specialty
		self.physician_hour_availability = physData[5] #physician_hour_availability
		self.physician_day_availability = physData[6] #physician_day_availability
		self.physician_counter_daysworked = physData[7] #physician_counter_daysworked
		self.physician_counter_nightsworked = physData[8] #physician_counter_nightsworked
		self.physician_regular_ward_flag = physData[9] #physician_regular_ward_flag
		self.physician_icu = physData[10] #physician_icu
		self.physician_emergency = physData[11] #physician_emergency
		self.physician_last_access = physData[12] #physician_last_access
		self.physician_last_checkin = physData[13] #physician_last_checkin
		self.physician_last_checkout = physData[14] #physician_last_checkout
		self.physician_last_ward_visited = physData[15] #physician_last_ward_visited
		self.physician_covid_symptom = physData[16] #physician_covid_symptom
		self.physician_last_covid_check = physData[17] #physician_last_covid_check


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

	def write_to_db(params):
		#
		pass