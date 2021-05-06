from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

import time

class MyApp(App):

	text_output = " "
	errors_count = 0
	time_spent = 0

	def build(self):
		self.Interface = AnchorLayout()
		MenuButtons = BoxLayout(spacing = 3,
								orientation = 'vertical',
								size_hint = [.4, .4])

		self.text_input = TextInput()

		MenuButtons.add_widget(Label(text = "Print text down below (only english lowercase letters)"))
		MenuButtons.add_widget(self.text_input)
		MenuButtons.add_widget(Button(text = "start",
									  on_press = self.game))

		self.Interface.add_widget(MenuButtons)
		return self.Interface

	def game(self, instance):

		self.time_start = time.time()

		if self.text_input.text != "":
			self.text_output = self.text_input.text

		# print(self.text_output)
		self.Interface.clear_widgets()
		
		self.GameInterface = AnchorLayout()
		GameButtons = BoxLayout(spacing = 3,
								orientation = 'vertical',
								size_hint = [.4, .4])

		self.text_typed = TextInput()

		GameButtons.add_widget(Label(text = self.text_output))
		GameButtons.add_widget(self.text_typed)

		GameButtons.add_widget(Button(text = "to end menu, instead of keyboard train",
		 							  on_press = self.end))

		self.GameInterface.add_widget(GameButtons)

		self.Interface.add_widget(self.GameInterface)

		

	def end(self, instance):
		self.time_spent = time.time() - self.time_start

		self.Interface.clear_widgets()
		self.EndInterface = AnchorLayout()
		EndButtons = BoxLayout(spacing = 3,
								orientation = 'vertical',
								size_hint = [.4, .4]) 
		EndButtons.add_widget(Label(text = 'speed: ' +
										    str(round(len(self.text_output) / (self.time_spent / 60))) +
										    ' letters per minute'))
		EndButtons.add_widget(Label(text = 'number of errors: ' + str(self.errors_count)))
		EndButtons.add_widget(Button(text = 'back to menu',
									 on_press = self.rebuild))

		self.EndInterface.add_widget(EndButtons)

		self.Interface.add_widget(self.EndInterface)

	def rebuild(self, instance):
		self.Interface.clear_widgets()
		self.NewInterface = AnchorLayout()
		NewMenuButtons = BoxLayout(spacing = 3,
								orientation = 'vertical',
								size_hint = [.4, .4])

		self.text_input = TextInput()

		NewMenuButtons.add_widget(Label(text = "Print text down below"))
		NewMenuButtons.add_widget(self.text_input)
		NewMenuButtons.add_widget(Button(text = "start",
									  on_press = self.game))

		self.NewInterface.add_widget(NewMenuButtons)
		self.Interface.add_widget(self.NewInterface)


if __name__ == "__main__":
	MyApp().run()
