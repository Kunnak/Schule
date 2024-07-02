from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
import os

#  Für die Farben
# ROT, GRÜN, BLAU, ALPHA

class MyGridApp(App):
    def build(self):
        Window.size = (800, 600)

        box_layout = BoxLayout(orientation='vertical')
        grid_layout = GridLayout(cols=2, rows=3, size_hint=(1, 0.9))

        header = Label(text='# Expertenaufgaben SD #', size_hint=(1, 0.1), font_size='24sp')

        button_width = 400
        button_height = 150

        password_generator = Button(text='Passwortgenerator', size_hint=(None, None), size=(button_width, button_height), background_color=(0, 1, 0.4, 1))
        password_generator.bind(on_press=self.open_password_generator)
        grid_layout.add_widget(password_generator)

        password_checker = Button(text=f'Passwortprüfer', size_hint=(None, None), size=(button_width, button_height), background_color=(0, 1, 0.4, 1))
        password_checker.bind(on_press=self.open_password_checker)
        grid_layout.add_widget(password_checker)

        schiffe = Button(text=f'Schiffe versenken', size_hint=(None, None), size=(button_width, button_height),background_color=(0, 0.5, 1, 1))
        schiffe.bind(on_press=self.open_schiffe_versenken)
        grid_layout.add_widget(schiffe)

        click = Button(text=f'Klick-Spiel', size_hint=(None, None), size=(button_width, button_height),background_color=(0, 0.5, 1, 1))
        click.bind(on_press=self.open_click_game)
        grid_layout.add_widget(click)

        sport = Button(text=f'Sport Aktivitäten', size_hint=(None, None), size=(button_width, button_height), background_color=(0.8, 0, 0.4, 1))
        sport.bind(on_press=self.open_sport_activities)
        grid_layout.add_widget(sport)

        lucky = Button(text=f'Glückliche Zahlen', size_hint=(None, None), size=(button_width, button_height), background_color=(0.8, 0, 0.4, 1))
        lucky.bind(on_press=self.open_lucky_numbers)
        grid_layout.add_widget(lucky)

        quit_button = Button(text='Beenden', size_hint=(1, 0.1), font_size='24sp', background_color=(1, 0.3, 0.1, 1))
        quit_button.bind(on_press=self.stop_app)

        box_layout.add_widget(header)
        box_layout.add_widget(grid_layout)
        box_layout.add_widget(quit_button)

        return box_layout

    @staticmethod
    def open_password_generator(instance):
        os.system('passwordgenerator.py')

    @staticmethod
    def open_password_checker(instance):
        os.system('passwordchecker.py')

    @staticmethod
    def open_schiffe_versenken(instance):
        os.system('schiffeversenken.py')

    @staticmethod
    def open_click_game(instance):
        os.system('clickgame.py')

    @staticmethod
    def open_sport_activities(instance):
        os.system('sportactivities.py')

    @staticmethod
    def open_lucky_numbers(instance):
        os.system('luckynumbers.py')

    @staticmethod
    def stop_app(instance):
        App.get_running_app().stop()
        Window.close()

if __name__ == '__main__':
    MyGridApp().run()
