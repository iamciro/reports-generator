# KIVYMD
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

# ASSETS
#from assets import texts as txt

# Class to open and close dialog
class Dialog:

	dialog = None

	# Open dialog
	def open(self, message=''):
		self.dialog = MDDialog(
			title=message,
			buttons=[
				MDFlatButton(
						text="Aceptar",
						on_press=self.close
				)
			],
		)
		self.dialog.open()

	# Close dialog
	def close(self, *args):
		self.dialog.dismiss(force=True)
