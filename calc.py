from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

# Set the app size
Window.size = (400, 600)

Builder.load_file('calc.kv')

class MyLayout(Widget):
	
	pending_val = '0'
	display_val = '0'
	answer = '0'
	eval_string_array = []

	# Function to clear text box
	def clear(self):
		self.display_val = '0'
		self.pending_val = '0'
		self.eval_string_array =[]
		self.ids.calc_input.text = self.display_val

	# Function to remove the last character in text box
	def remove(self):
		self.display_val = self.ids.calc_input.text
		# Remove the last item in the text box
		self.display_val = self.display_val[:-1]
		# Output back to the text box
		self.ids.calc_input.text = self.display_val

		if self.display_val == '':
			self.display_val = '0'
			self.ids.calc_input.text = self.display_val

	def button_press(self, button):
		# Create a variable that was previously in the text box
		self.display_val = self.ids.calc_input.text

		# Determine if 0 is there
		if self.display_val == '0':
			self.ids.calc_input.text = ''
			self.ids.calc_input.text = f'{button}'
			self.display_val = self.ids.calc_input.text
		else:
			self.ids.calc_input.text += f'{button}'
			self.display_val = self.ids.calc_input.text

	# Create decimal function
	def dot(self):
		
		self.display_val = self.ids.calc_input.text
		
		if '.' not in self.display_val:
			self.ids.calc_input.text = f'{self.display_val}.'

	# Create function to make input positive/negative
	def pos_neg(self):

		self.display_val = self.ids.calc_input.text

		if self.display_val == '0':
			self.ids.calc_input.text = ''
			self.ids.calc_input.text = f'-'
			self.display_val = self.ids.calc_input.text
		elif '-' in self.display_val:
			self.ids.calc_input.text = f'{self.display_val.replace("-","")}'
			self.display_val = self.ids.calc_input.text
		else:
			self.ids.calc_input.text = f'-{self.display_val}'
			self.display_val = self.ids.calc_input.text

	# Create function to convert to percentage
	def percentage(self):

		if self.answer == '0':
			pass
		else:
			self.answer = self.answer / 100
			self.ids.calc_input.text = str(self.answer)
			self.answer = '0'

	# Function to perform operations
	def operator(self, button):
		
		if button == '+':
			self.pending_val = self.display_val
			self.display_val = '0'
			self.ids.calc_input.text = self.display_val
			self.eval_string_array.append(self.pending_val)
			self.eval_string_array.append('+')

		elif button == '-':
			self.pending_val = self.display_val
			self.display_val = '0'
			self.ids.calc_input.text = self.display_val
			self.eval_string_array.append(self.pending_val)
			self.eval_string_array.append('-')

		elif button == '*':
			self.pending_val = self.display_val
			self.display_val = '0'
			self.ids.calc_input.text = self.display_val
			self.eval_string_array.append(self.pending_val)
			self.eval_string_array.append('*')

		elif button == '/':
			self.pending_val = self.display_val
			self.display_val = '0'
			self.ids.calc_input.text = self.display_val
			self.eval_string_array.append(self.pending_val)
			self.eval_string_array.append('/')

		elif button == '=':
			self.eval_string_array.append(self.display_val)
			self.answer = eval(' '.join(self.eval_string_array))
			self.ids.calc_input.text = str(self.answer)
			self.eval_string_array = []

class CalculatorApp(App):
	def build(self):
		return MyLayout()

if __name__ == '__main__':
	CalculatorApp().run()