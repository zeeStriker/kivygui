from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

# Set the app size
Window.size = (400, 600)

Builder.load_file('calc.kv')

class MyLayout(Widget):
	def clear(self):
		self.ids.calc_input.text = '0'

	# Create a button pressing function
	def button_press(self, button):
		# Create a variable that was previously in the text box
		prior = self.ids.calc_input.text

		# Determine if 0 is there
		if prior == '0':
				self.ids.calc_input.text = ''
				self.ids.calc_input.text = f'{button}'
		else:
			self.ids.calc_input.text = f'{prior}{button}'

	# Create addition function
	def add(self):
		# Create a variable that was previously in the text box
		prior = self.ids.calc_input.text

		self.ids.calc_input.text = f'{prior}+'

	# Create subtraction function
	def subtract(self):
		# Create a variable that was previously in the text box
		prior = self.ids.calc_input.text

		self.ids.calc_input.text = f'{prior}-'

	# Create multiplication function
	def multiply(self):
		# Create a variable that was previously in the text box
		prior = self.ids.calc_input.text

		self.ids.calc_input.text = f'{prior}*'

	# Create division function
	def divide(self):
		# Create a variable that was previously in the text box
		prior = self.ids.calc_input.text

		self.ids.calc_input.text = f'{prior}/'

	# Create equals function
	def equals(self):
		# Create a variable that was previously in the text box
		prior = self.ids.calc_input.text

		# Addition
		if '+' in prior:
			num_list = prior.split("+")
			answer = 0

			# loop through our list
			for number in num_list:
				answer = answer + int(number)

			# print the answer to text box
			self.ids.calc_input.text = str(answer)
	
class CalculatorApp(App):
	def build(self):
		return MyLayout()

if __name__ == '__main__':
	CalculatorApp().run()