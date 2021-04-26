from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

class MyApp(App):

	textoutput = " "

	def build(self):
		Interface = AnchorLayout()
		Buttons = BoxLayout(spacing = 3, orientation = 'vertical', size_hint=[.4, .4])

		self.textinput = TextInput()

		Buttons.add_widget(Label(text = "Print your text to type down below"))
		Buttons.add_widget(self.textinput)
		Buttons.add_widget(Button(text = "start", on_press = self.start))

		Interface.add_widget(Buttons)
		return Interface

	def start(self, instance):
		if self.textinput.text != "":
			textoutput = self.textinput.text

		print(textoutput)

if __name__ == "__main__":
	MyApp().run()
