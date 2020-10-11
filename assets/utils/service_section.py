from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

class RSServiceSection(BoxLayout):

	service_order_number = StringProperty()
	service_datetime = StringProperty()

	def __init__(self, **kwargs): 
		super(RSServiceSection, self).__init__(**kwargs)