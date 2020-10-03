from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen

from kivymd.app import MDApp

class HomeScreen(Screen):
	pass

class MainApp(MDApp):
	def build(self):
		self.title = "Tecno Services | Generación de reportes"
		return BoxLayout()

MainApp().run()