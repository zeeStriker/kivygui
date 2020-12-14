from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

# Set the app size
Window.size = (750, 500)

Builder.load_file('audiotruth.kv')

class MyLayout(Widget):
	pass

class AudioTruthApp(App):
	def build(self):
		return MyLayout()

if __name__ == '__main__':
	AudioTruthApp().run()