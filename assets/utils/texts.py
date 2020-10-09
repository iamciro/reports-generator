### Constants and Texts used across the app

from kivy.utils import get_color_from_hex

# APPLICATION TITLE
APP_TITLE = 'Tecno Services | Generación de reportes'

# HEADER BG COLORS CONSTANTS
HEADER_BG_COLOR = get_color_from_hex('3AB054')
BUTTON_BG_COLOR = get_color_from_hex('3AB054')

dialog = {
	"OK_BTN_TEXT": "Aceptar",
	"INVALID_MESSAGES": {
		"client_name": 'El campo "Nombre del cliente" es obligatorio',
		"client_phone_number": 'El campo "Teléfono" es obligatorio',
		"client_phone_number_invalid_format": 'No se puede ingresar letras en el campo "Teléfono"',
		"device_type": 'El campo "Dispositivo" es obligatorio',
		"device_company": 'El campo "Marca" es obligatorio',
	}
}

pdf = {
	"title": "Tecno Services",
	"service_order_number": 'Número de orden: ',
	"service_datetime": 'Fecha de orden: ',	
	"client_name": 'Nombre del cliente: ',
	"client_phone_number": 'Teléfono: ',
	"device_type": "Dipositivo: ",
	"device_company": "Marca: ",
	"device_model": "Modelo: ",
	"reported_problem": "Problema reportado: ",
	"repair_date": "Fecha probable de reparación: ",
	"client_firm": "Firma del cliente: "
}

# HEADER TEXTS
header = {
	"title": 'Tecno Services'
}

# HomeScreen TEXTS
home_screen = {
	"welcome_text": '¡Bienvenido!',
	"reportscreen_btn_text": 'Realizar reporte'
}

# ReportScreen TEXCS
report_screen = {
	# MEJORAR ESTO
	"service_order": 'Orden de servicio: ',
	"service_datetime": 'Fecha de orden: ',
	"client_name": 'Nombre del cliente',
	"client_phone_number": 'Teléfono',
	"device": 'Dispositivo',
	"company": 'Marca',
	"model": 'Modelo',
	"reported_problem": 'Problema reportado',
	"generate_report_btn_text": 'Generar reporte'
}