# This file is for PDF's generation

from fpdf import FPDF

class PDF(FPDF):

	def __init__(self, *args): 
		super(PDF, self).__init__(*args)
		self.alias_nb_pages()
		self.add_page()
		self.set_font('Arial', '', 20)

		self.offset =  self.x + 150

	def header(self):
		self.set_font('Arial', 'B', 25)
		self.rect(5, 5, 287, 25, style = '')
		self.cell(0, 10, 'Tecno Services', 0, 1, 'C')
		self.set_font('Arial', '', 15)
		#self.cell(0, 10, 'Av. Bozan 44', 0, 1, 'C')

	def service_info_section(self, service_order_number, service_datetime):

		self.cell(0, 15, '', 0, 1, 'C')

		# Save top coordinate
		top = self.y
		self.x = 40

		self.multi_cell(150,10,'Número de orden: ' + service_order_number,0,0)

		# Reset y coordinate
		self.y = top

		# Move to computed offset
		self.x = self.offset 

		self.multi_cell(130,10,'Fecha de orden: ' + service_datetime,0,0)	 

		return self.offset

	def client_info_section(self, client_name, client_phone_number):
		self.cell(0, 15, '', 0, 1, 'C')

		self.x = 25

		self.multi_cell(140,10,'Nombre del cliente: ' + client_name,1,1)

		# Save top coordinate
		top = self.y

		# Reset y coordinate
		self.y = top 

		# Move to computed self.offset
		self.x = self.offset +15

		self.multi_cell(80,10,'Teléfono: ' + client_phone_number,1,0)

	def device_info_section(self, device_type, device_company, device_model):
		self.cell(0, 20, '', 0, 1, 'C')

		self.x = 20

		self.multi_cell(100,10,'Dipositivo: ' + device_type,1,1)

		# Save top coordinate
		top = self.y

		# Reset y coordinate
		self.y = top 

		# Move to computed self.offset
		self.x = 130

		self.multi_cell(60,10,'Marca: ' + device_company,1,0)

		# Move to computed self.offset
		self.x = 200

		self.multi_cell(60,10,'Modelo: ' + device_model,1,0)

	def problem_info_section(self, reported_problem):
		# Set X position
		self.x = 5

		self.cell(0, 45, 'Problema reportado', 0, 1, 'C')
		self.rect(20, 100, 240, 40, style = '')

		# Set X and Y axis position
		self.x = 22
		self.y = 103

		self.set_font('Arial', '', 15)
		self.multi_cell(240,6,reported_problem,0,0)

	def date_client_firm_section(self):
		#Set X and Y axis position
		self.y = 150
		self.x = 20

		self.cell(0, 0, 'Fecha probable de reparación: ', 0, 1)

		# Set X position
		self.x = 185

		self.cell(0, 0, 'Firma del cliente ', 0, 1)

		# Set X and Y position
		self.x = 7
		self.y = 168

	def footer(self):
		self.set_font('Arial', '', 16)

		self.cell(0, 0, '- Este comprobante es obligatorio SIN EXCEPCIÓN para retirar el dispositivo que Ud. haya dejado en reparación.', 0, 1)
		self.x = 7
		self.cell(0, 12, '- Pasados los 30 días hábiles de reparación se actualizarán precios a la fecha sin previo aviso.', 0, 1)
		self.x = 7
		self.cell(0, 0, '- Pasados los 60 días hábiles de la fecha de retiro pasará a abandono legal conforme a la Ley 2523/2526,', 0, 1)
		self.cell(0, 9.8, 'la Casa no se responsabilizará por el mismo.', 0, 1)
