from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

from kivymd.app import MDApp

class HomeScreen(Screen):
	pass

class MainApp(MDApp):
	def build(self):
		self.title = "Tecno Services | Generación de reportes"
		return Builder.load_file('assets/kv/app.kv')


MainApp().run()