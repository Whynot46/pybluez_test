from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
#import bluetooth

mac_addr = '' # mac-адрес компа
#bd_addr = "B8:27:EB:97:86:BF"
port = 1

class test_screen(Screen):
    def send_data(self, *args):
        try:
            sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            sock.connect((mac_addr, port))
            sock.send(
                f"s_temp:{int(self.temp_slider.value)}||s_incline:{int(self.engine_turn_slider.value)}")
            sock.close()

            '''
            s_temp, s_incline = map(str, data.split("||"))
            s_temp = int(s_temp.partition('s_temp:')[-1])
            s_incline = int(s_incline.partition('s_incline:')[-1])
            '''
        except:
            print('No bluetooth connection')


class test_app(MDApp):
    def build(self):
        self.load_kv('test.kv')
        self.theme_cls.theme_style = 'Dark'
        sm = ScreenManager()
        sm.add_widget(test_screen(name='screen'))
        return sm


if __name__ == "__main__":
    test_app().run()