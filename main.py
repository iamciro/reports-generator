# KIVY
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.properties import ObjectProperty

# KIVYMD
from kivymd.app import MDApp

# MODULES
from assets.utils import texts as txt
from assets.utils.dialog import Dialog
from datetime import datetime
import re

class ReportScreen(Screen):

	# Client section
	client_section = ObjectProperty()	

	# Device section
	device_section = ObjectProperty()	

	# Device section
	reported_problem_section = ObjectProperty()

	# Today's datetime
	date_time = datetime.now()

	# Service's order number
	service_order_number = "2020-111100"

	# Service's datetime
	service_datetime = date_time.strftime("%d/%m/%Y, %H:%M:%S")

	def __init__(self, **kwargs): 
		super(ReportScreen, self).__init__(**kwargs)
		self.dialog = Dialog()

	def validate_data(self, data):

		is_valid = True
		dialog_message = ''

		if len(data['client_name']) == 0:
			is_valid = False
			dialog_message = txt.dialog['INVALID_MESSAGES']['client_name']
		elif len(data['client_phone_number']) == 0:
			# Pattern DDDD-DDDD
			is_valid = False
			dialog_message = txt.dialog['INVALID_MESSAGES']['client_phone_number']
		elif not re.search('[0-9]', data['client_phone_number']):
			is_valid = False
			dialog_message = 'No se pueden ingresar letras en el campo Teléfono'

		elif len(data['device_type']) == 0:
			is_valid = False
			dialog_message = txt.dialog['INVALID_MESSAGES']['device_type']
		elif len(data['device_company']) == 0:
			is_valid = False
			dialog_message = txt.dialog['INVALID_MESSAGES']['device_company']

		return {"is_valid": is_valid, "dialog_message": dialog_message}

	def get_data(self):

		# Service's order
		service_order_number = self.service_order_number
		# Service's datetime
		service_datetime = self.service_datetime
		
		# Client's name
		client_name = self.client_section.ids.client_name.text
		# Client's phone number
		client_phone_number = self.client_section.ids.client_phone_number.text

		# Device's type
		device_type =  self.device_section.ids.device_type.text
		# Device's company
		device_company = self.device_section.ids.device_company.text
		# Device's model
		device_model = self.device_section.ids.device_model.text

		# Reported problem
		reported_problem = self.reported_problem_section.ids.reported_problem.text

		# Convert data to dictionary object
		data = {
			"client_name": client_name,
			"client_phone_number": client_phone_number,
			"device_type": device_type,
			"device_company": device_company,
			"device_model": device_model,
			"reported_problem": reported_problem
		}

		# Validate data
		valid_data = self.validate_data(data)

		if valid_data['is_valid']:
			self.dialog.open("Validacion valida")
		else:
			self.dialog.open(valid_data['dialog_message'])

class HomeScreen(Screen):
	pass

class MainApp(MDApp):
	def build(self):
		self.title = txt.APP_TITLE
		return Builder.load_file('assets/kv/app.kv')


MainApp().run()