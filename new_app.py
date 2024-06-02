from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from time import strftime
from datetime import datetime
import requests

api_key = 'db2d208f006995514c7028c748875395'
#date Format
month = datetime.now().strftime('%B')[0:3]
date = datetime.today().strftime('%d')

class City:
    def __init__(self, city):
        self.name = city
    
    def weather_data(self):
        res = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={self.name}&appid={api_key}', timeout=10)
        w_data = res.json()
        try:
            self.description = ("{}".format(w_data['weather'][0]['description']))
            self.weather = ("{}".format(w_data['weather'][0]['main']))
            self.temp = (int(float('{}'.format(w_data['main']['temp'])) - 273.15))
            self.h = ("Humidity: {}".format(w_data['main']['humidity']))
            self.p = ("Pressure: {}".format(w_data['main']['pressure']))
            self.tempMax = ("MAX Temp: {}".format((int(float(w_data['main']['temp_max']) - 273.15))))
            self.tempMin = ("MIN Temp: {}".format((int(float(w_data['main']['temp_min']) - 273.15))))
            self.wSpeed = ("Wind Speed: {} m/s".format(w_data['wind']['speed']))
            self.icon_id = w_data['weather'][0]['icon']
        except:
            messagebox.showinfo("", 'City not found!')

class App:
    def __init__(self):
        # self.stamps = []

        self.root = Tk()
        self.root.title("Emma Weather APP")

        self.button = Button(self.root, text="Open a new window", command=self.create_second_win)
        self.button.pack()

    # https://stackoverflow.com/questions/67540996/how-to-run-a-function-as-a-button-command-in-tkinter-from-a-2nd-window
    def create_stamp(self):
        stamp = Label(self.window2, text="Stamp")
        stamp.pack()
        self.stamps.append(stamp)

    def create_second_win(self):
        self.window2 = Toplevel(self.root)
        self.lab2 = Button(self.window2, text="Click me", command=self.create_stamp)
        self.lab2.pack()




if __name__ == "__main__":
    app = App()
    app.mainloop()