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

	# Create a function to remove the last character in text box
	def remove(self):
		prior = self.ids.calc_input.text
		# Remove the last item in the text box
		prior = prior[:-1]
		# Output back to the text box
		self.ids.calc_input.text = prior

	# Create a function for pos/neg
	def pos_neg(self):
		prior = self.ids.calc_input.text
		# Search prior for a negative number
		if '-' in prior:
			self.ids.calc_input.text = f'{prior.replace("-", "")}'
		else:
			self.ids.calc_input.text = f'-{prior}'

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

	# Create decimal function
	def dot(self):
		prior = self.ids.calc_input.text

		if '.' in prior:
			pass
		else:
			# Add a decimal to the end of the text
			prior = f'{prior}.'
			# Add message to text box
			self.ids.calc_input.text = prior

	# Create function for all signs
	def math_sign(self, sign):
		# Create a variable that was previously in the text box
		prior = self.ids.calc_input.text

		self.ids.calc_input.text = f'{prior}{sign}'

	# Create equals function
	def equals(self):
		# Create a variable that was previously in the text box
		prior = self.ids.calc_input.text

		# Addition
		if '+' in prior:
			num_list = prior.split("+")
			answer = 0.0

			# loop through our list
			for number in num_list:
				answer = answer + float(number)

			# print the answer to text box
			self.ids.calc_input.text = str(answer)

		# # Subtraction
		# if '-' in prior:
		# 	num_list = prior.split("-")
		# 	answer = 0

		# 	# loop through our list
		# 	for number in num_list:
		# 		answer = answer - int(number)

		# 	# print the answer to text box
		# 	self.ids.calc_input.text = str(answer)

		# # Multiplication
		# if '*' in prior:
		# 	num_list = prior.split("*")
		# 	answer = 0

		# 	# loop through our list
		# 	for number in num_list:
		# 		answer = answer * int(number)

		# 	# print the answer to text box
		# 	self.ids.calc_input.text = str(answer)

		# # Division
		# if '/' in prior:
		# 	num_list = prior.split("/")
		# 	answer = 0

		# 	# loop through our list
		# 	for number in num_list:
		# 		answer = answer / int(number)

		# 	# print the answer to text box
		# 	self.ids.calc_input.text = str(answer)
	
class CalculatorApp(App):
	def build(self):
		return MyLayout()

if __name__ == '__main__':
	CalculatorApp().run()