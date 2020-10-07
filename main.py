# KIVY
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.properties import ObjectProperty

# KIVYMD
from kivymd.app import MDApp

# MODULES
from assets.utils import texts as txt
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

	def get_data(self):

		# Service's order
		service_order = self.service_order_number
		# Service's datetime
		service_datetime = self.service_datetime
		
		# Client's name
		client_name = self.client_section.ids.client_name.text
		# Client's phone number
		client_phone = self.client_section.ids.client_phone_number.text

		# Device's type
		device_type =  self.device_section.ids.device_type.text
		# Device's company
		device_company = self.device_section.ids.device_company.text
		# Device's model
		device_model = self.device_section.ids.device_model.text

		# Reported problem
		reported_problem = self.reported_problem_section.ids.reported_problem.text

		print(service_order, " .... ", service_datetime)

class HomeScreen(Screen):
	pass

class MainApp(MDApp):
	def build(self):
		self.title = txt.APP_TITLE
		return Builder.load_file('assets/kv/app.kv')


MainApp().run()