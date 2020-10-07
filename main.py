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

		right_data = True

		if len(data['client_name']) == 0:
			print("Llená el campo nombre")
			right_data = False
		elif len(data['client_phone_number']) == 0:
			print("Llená el campo Teléfono")
			right_data = False
		elif len(data['device_type']) == 0:
			print("Llená el campo Dispositivo")
			right_data = False
		elif len(data['device_company']) == 0:
			print("Llená el campo Marca")
			right_data = False

		return right_data

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
		validated_data = self.validate_data(data)

		if validated_data:
			self.dialog.open("Validacion valida")
		else:
			self.dialog.open("Validacion invalida")

class HomeScreen(Screen):
	pass

class MainApp(MDApp):
	def build(self):
		self.title = txt.APP_TITLE
		return Builder.load_file('assets/kv/app.kv')


MainApp().run()