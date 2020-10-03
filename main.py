from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

from kivymd.app import MDApp

from assets.utils import texts as txt

class ReportScreen(Screen):
	pass

class HomeScreen(Screen):
	pass

class MainApp(MDApp):
	def build(self):
		self.title = txt.APP_TITLE
		return Builder.load_file('assets/kv/app.kv')


MainApp().run()