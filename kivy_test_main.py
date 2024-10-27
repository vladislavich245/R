from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class main_screen(Screen):
    def init(self, **kwargs):
        super().init(**kwargs)

        lbl = Label(text='TEXT', halign='right')
        line1 = BoxLayout(size_hint=(1, None), height='600sp')
        line1.add_widget(lbl)
        btn1 = Button(text='Почати',  size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        btn2 = Button(text='Почати',  size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        btn3 = Button(text='Почати',  size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        vert1 = BoxLayout(size_hint=(1, None), height='600sp')
        vert1.add_widget(btn1)
        vert1.add_widget(btn2)
        vert1.add_widget(btn3)
class Vlad(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(main_screen(name='mnscr'))
        return sm


app = Vlad()
app.run()
