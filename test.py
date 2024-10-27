from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class InstrScr(Screen):
    def init(self, **kwargs):
        super().init(**kwargs)

        lbl1 = Label(text="Введіть ім'я:", halign='right')
        lbl2 = Label(text='Введіть вік:', halign='right')

        self.btn = Button(text='Почати', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.btn.on_press = self.next

        line1 = BoxLayout(size_hint=(0.8, None), height='30sp')
        line2 = BoxLayout(size_hint=(0.8, None), height='30sp')
        line1.add_widget(lbl1)
        line1.add_widget(self.in_name)
        line2.add_widget(lbl2)
        line2.add_widget(self.in_age)

        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        outer.add_widget(line1)
        outer.add_widget(line2)
        outer.add_widget(self.btn)

        self.add_widget(outer)


class Vlad(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InstrScr(name='mnscr'))
        return sm


app = Vlad()
app.run()
