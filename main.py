from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class SimpleKivyApp(App):
    def build(self):
        # A felület elrendezése
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # Gomb létrehozása
        button = Button(text='Nyomj meg!', on_press=self.on_button_press)

        # Címke létrehozása
        self.label = Label(text='Üdvözöllek a Kivy egyszerű alkalmazásában!')

        # Elemek hozzáadása a felülethez
        layout.add_widget(button)
        layout.add_widget(self.label)

        return layout

    def on_button_press(self, instance):
        # A gomb megnyomásakor frissíti a címkét
        self.label.text = 'Sikeresen megnyomtad a gombot!'


if __name__ == '__main__':
    SimpleKivyApp().run()
