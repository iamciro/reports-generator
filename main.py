# KIVY MODULES
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.properties import ObjectProperty

# KIVYMD MODULES
from kivymd.app import MDApp

# PERSONALIZED MODULES
from assets.utils import texts as txt
from assets.utils.dialog import Dialog
from assets.utils.pdf import PDF

# PYTHON MODULES
from datetime import datetime
import re
import os
import webbrowser

class ReportScreen(Screen):

	''' This class manages Report Screen's functionalities. '''

	# Report screen object
	report_screen = ObjectProperty()

	# Service section 
	service_section = ObjectProperty()

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

	# PDF flag
	pdf_generated = False

	def __init__(self, **kwargs): 
		super(ReportScreen, self).__init__(**kwargs)
		# Create dialog instance to use across the class.
		self.dialog = Dialog()

	def validate_data(self, data):
		''' This method validates the text inputs' data. '''

		# Flag var to validate if any field is empty or wrong.
		is_valid = True
		# Flag var to use it as the error dialog's message.
		dialog_message = ''

		''' 
			client_name, client_phone_number, device_type
			and device_company are required. Then, they're 
			the fields to validate.
		'''

		# If client_name len is 0
		if len(data['client_name']) == 0:
			is_valid = False
			dialog_message = txt.dialog['INVALID_MESSAGES']['client_name']
		
		# If client_phone_number len is 0
		elif len(data['client_phone_number']) == 0:
			is_valid = False
			dialog_message = txt.dialog['INVALID_MESSAGES']['client_phone_number']
		
		# If client_phone_number value isn't a number one
		elif not re.search('[0-9]', data['client_phone_number']):
			is_valid = False
			dialog_message = txt.dialog['INVALID_MESSAGES']['client_phone_number_invalid_format']

		
		# If device_type len is 0
		elif len(data['device_type']) == 0:
			is_valid = False
			dialog_message = txt.dialog['INVALID_MESSAGES']['device_type']
		
		# If device_company len is 0
		elif len(data['device_company']) == 0:
			is_valid = False
			dialog_message = txt.dialog['INVALID_MESSAGES']['device_company']

		# Return dict object with right/wrong validation and error dialog's message.
		return {"is_valid": is_valid, "dialog_message": dialog_message}

	def empty_fields(self):
		''' This method makes text fields empty. '''

		# Empty client's section fields.
		self.client_section.ids.client_name.text = ''
		self.client_section.ids.client_phone_number.text = ''

		# Empty device's section fields.
		self.device_section.ids.device_type.text = ''
		self.device_section.ids.device_company.text = ''
		self.device_section.ids.device_model.text = ''

		# Empty report problem's section fields.
		self.reported_problem_section.ids.reported_problem.text = ''

	def reinitialize_service_texts(self):
		''' 
			This method reinitializes services' text inputs, 
			with new service_order_number and service_datetime values. 
		'''

		# Service's order number
		self.service_order_number = "2020-cccccc"

		# Today's datetime
		self.date_time = datetime.now()
		# Service's datetime
		self.service_datetime = self.date_time.strftime("%d/%m/%Y, %H:%M:%S")

		# Gives to service_order field a new value.
		self.service_section.ids.service_order.text = txt.report_screen['service_order'] + self.service_order_number
		# Gives to service_datetime field a new value.
		self.service_section.ids.service_datetime.text = txt.report_screen['service_datetime'] + self.service_datetime

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

		# Convert data to a dictionary object
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

		# If data was rightly validated
		if valid_data['is_valid']:
			
			# Try PDF generation
			try:
				# Generate PDF
				
				# Init pdf
				pdf = PDF('L', 'mm', 'A4')

				offset = pdf.service_info_section(service_order_number, service_datetime)

				# Draw client's info section
				pdf.client_info_section(client_name, client_phone_number)

				# Draw device's info section
				pdf.device_info_section(device_type, device_company, device_model)

				# Draw problem's info section
				pdf.problem_info_section(reported_problem)

				# Draw date_client_firm_section
				pdf.date_client_firm_section()

				# Generate PDF
				pdf.output('pdf/example3.pdf', 'F')

				# Successfully generated PDF
				self.pdf_generated = True

			except Exception as e:
				# Unexpected error
				self.dialog.open('Error: ' + e)

			# Reinitializes service's section text values.
			self.reinitialize_service_texts()
			# Reinitializes text inputs's values to an empty string
			# after user has generated a PDF file.
			self.empty_fields()

			# if PDF file was successfully generated
			if self.pdf_generated:

				# Open PDF file
				webbrowser.open_new(r'pdf/example3.pdf')

				# Open a success dialog
				self.dialog.open('¡PDF generado con éxito!')

		else:
			self.dialog.open(valid_data['dialog_message'])

class HomeScreen(Screen):
	pass

class MainApp(MDApp):
	def build(self):
		self.title = txt.APP_TITLE
		return Builder.load_file('assets/kv/app.kv')


if __name__ == '__main__':
	MainApp().run()