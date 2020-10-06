from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

from kivymd.app import MDApp

from assets.utils import texts as txt

from datetime import datetime

class ReportScreen(Screen):

	date_time = datetime.now()

	service_order_number = "2020-111100"
	service_datetime = date_time.strftime("%d/%m/%Y, %H:%M:%S")

class HomeScreen(Screen):
	pass

class MainApp(MDApp):
	def build(self):
		self.title = txt.APP_TITLE
		return Builder.load_file('assets/kv/app.kv')


MainApp().run()