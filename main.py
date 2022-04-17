from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.core.window import Window

# from kivy.config import Config
# Config.set('graphics', 'width', '700')
# Config.set('graphics', 'height', '800')
# Config.set('graphics', 'resizable', True)
# Config.write()
# Window.size = (600, 500)

import time


class MyApp(App):

	text_output = " "
	errors_count = 0
	time_spent = 0
	width = 50
	written_text_length = 0
	text_written = ""
	text_input = TextInput()
	def build(self):
		self.Interface = AnchorLayout()
		MenuButtons = BoxLayout(spacing = 3,
								orientation = 'vertical',
								size_hint = [.4, .4])
		self.text_input.text = ""
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

		self.Interface.clear_widgets()
		
		self.GameInterface = AnchorLayout(anchor_x = 'center', anchor_y = 'center')
		self.GameInterface.add_widget(Label(text = self.text_output,
											markup = True,
											font_size = 20))

		TestKeyboard = Window.request_keyboard(None, self)
		if self.text_input.text!="":
			TestKeyboard.bind(on_key_down = self.end)

		self.Interface.add_widget(self.GameInterface)

		

	def end(self, keyboard, keycode, text, modifiers):
		print ('input ',self.text_input.text, ' my',self.text_written)
		if (self.written_text_length<len(self.text_input.text)):
			if keycode[1] == self.text_input.text[self.written_text_length]:
				self.written_text_length += 1
				self.text_written += keycode[1]
				if len(self.text_input.text) == len(self.text_written):
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

					self.errors_count = 0
					EndButtons.add_widget(Button(text = 'back to menu',
												 on_press = self.rebuild))

					self.EndInterface.add_widget(EndButtons)

					self.Interface.add_widget(self.EndInterface)
			else:
				self.errors_count += 1

	def rebuild(self, instance):
		self.Interface.clear_widgets()
		
		NewMenuButtons = BoxLayout(spacing = 3,
								orientation = 'vertical',
								size_hint = [.4, .4])
		self.text_input.text = ""
		NewMenuButtons.add_widget(Label(text = "Print text down below (only english lowercase letters)"))
		text_input2 =TextInput()
		self.text_input = text_input2
		NewMenuButtons.add_widget(text_input2)
		NewMenuButtons.add_widget(Button(text = "start",
									  on_press = self.game))
		self.Interface.add_widget(NewMenuButtons)
		
		written_text_length=0
		self.written_text_length = 0
		self.text_written= ""
		self.text_output =" "
		self.errors_count = 0


if __name__ == "__main__":
	MyApp().run()
