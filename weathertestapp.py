from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from datetime import datetime
import requests

api_key = 'db2d208f006995514c7028c748875395'
#date Format
month = datetime.now().strftime('%B')[0:3]
date = datetime.today().strftime('%d')

class City:
    def __init__(self, name=''):
        self.name = name
    
    def get_weather_data(self):
        res = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={self.name}&appid={api_key}', timeout=10)
        w_data = res.json()
        try:
            self.description = ("{}".format(w_data['weather'][0]['description']))
            self.weather = ("{}".format(w_data['weather'][0]['main']))
            self.temp = (int(float('{}'.format(w_data['main']['temp'])) - 273.15))
            self.h = ("Humidity: {}".format(w_data['main']['humidity']))
            self.p = ("Pressure: {}".format(w_data['main']['pressure']))
            self.tempFeel= ("Feel like: {}".format((int(float(w_data['main']['feels_like']) - 273.15))))
            self.tempMax = ("MAX Temp: {}".format((int(float(w_data['main']['temp_max']) - 273.15))))
            self.tempMin = ("MIN Temp: {}".format((int(float(w_data['main']['temp_min']) - 273.15))))
            self.wSpeed = ("Wind Speed: {} m/s".format(w_data['wind']['speed']))
            self.icon_id = w_data['weather'][0]['icon']
        except:
            messagebox.showinfo("", 'City not found!')

class App:
    def __init__(self):
        self.root = Tk() 
        self.root.geometry('800x400')
        self.root.title('Emma Weather APP')
        self.root.resizable(0,0)
        Frame(self.root, width=800, height=50, bg='#353535').place(x=0,y=0)
    
    def Search_bar(self):
        global imgSearch

        # entry_search_city
        def on_entry(e):
            e1.delete(0,'end')
        def on_leave(e):
            if e1.get()=='':
                e1.insert(0, 'Search City')        
        def Search():
            name = str(e1.get())
            e1.delete(0,'end')
            self.label(name)

        e1 = Entry(self.root, width=21, fg='white', bg='#353535', border=0)
        e1.config(font=('Calibry',12))
        e1.bind("<FocusIn>", on_entry)
        e1.bind("<FocusOut>", on_leave)
        e1.insert(0, 'Search City')
        e1.place(x=620, y=15)

        imgSearch = ImageTk.PhotoImage(Image.open('search.png').resize((30,30)))
        Button(self.root, image=imgSearch, command= Search, border=0).place(x=750, y=10)
 
    def label(self, name):
        global imgWeather

        city = City(name)
        city.get_weather_data()
        bcolor=  "#f78954" if city.temp>20 else "#4792b3"
        fcolor= "white"
        start_line = 50

        #Weather_Icon
        icon_data = requests.get(f'http://openweathermap.org/img/wn/{city.icon_id}@2x.png')
        with open("icon.png", "wb") as f:
            f.write(icon_data.content)
        Frame(self.root, width=800, height=350, bg=bcolor).place(x=0, y=50)
        imgWeather = ImageTk.PhotoImage(Image.open("icon.png").resize((300,300)))
        Label(self.root, bg=bcolor, image=imgWeather, border=0).place(x=30, y=50)

        l1 = Label(self.root, text=str(city.name), bg='#353535', fg='white')
        l1.config(font=('Calibry', 18))
        l1.place(x=20, y=8)

        l2 = Label(self.root, text=str(month + " " + date), bg=bcolor, fg=fcolor)
        l2.config(font=("Calibry", 25))
        l2.place(x=340, y=335)

        l3 = Label(self.root, text=str(city.h + "%"), bg=bcolor, fg=fcolor )
        l3.config(font=("Calibry", 12))
        l3.place(x=520, y= start_line + 40)

        l3 = Label(self.root, text=str(city.p + " hPa"), bg=bcolor, fg=fcolor)
        l3.config(font=("Calibry", 12))
        l3.place(x=520, y= start_line + 40*2)      

        l3 = Label(self.root, text=str(city.tempFeel + "℃"), bg=bcolor, fg=fcolor)
        l3.config(font=("Calibry", 12))
        l3.place(x=520, y= start_line + 40*3)

        l3 = Label(self.root, text=str(city.tempMax + "℃"), bg=bcolor, fg=fcolor)
        l3.config(font=("Calibry", 12))
        l3.place(x=520, y= start_line + 40*4)

        l3 = Label(self.root, text=str(city.tempMin + "℃"), bg=bcolor, fg=fcolor)
        l3.config(font=("Calibry", 12))
        l3.place(x=520, y= start_line + 40*5)

        l3 = Label(self.root, text=str(city.wSpeed), bg=bcolor, fg=fcolor)
        l3.config(font=("Calibry", 12))
        l3.place(x=520, y= start_line + 40*6)

        l4 = Label(self.root, text=str(city.temp) + "℃", bg=bcolor, fg=fcolor)
        l4.config(font=("Calibry", 50))
        l4.place(x=330, y=150)
        
        l4 = Label(self.root, text=str(city.temp) + "℃", bg=bcolor, fg=fcolor)    
        l4.config(font=("Calibry", 50))
        l4.place(x=330, y=150)

    def NoConnectPrompt(self):
        global imgNoInternet
        print("Internet is off")
        imgNoInternet = ImageTk.PhotoImage(Image.open("NoConnect.png").resize((400,400)))
        Frame(self.root, width=800, height=400, bg='white').place(x=0, y=0)
        Label(self.root, image=imgNoInternet, bg='white', border=0).pack(expand=True)
    
    def mainloop(self):
        self.root.mainloop()     

def checkConnect():
    try:
        res = requests.get(f'http://api.openweathermap.org', timeout=10)
        return True   
    except:
        return False     

#main
try:
    if __name__ == "__main__":
        app = App()
        if checkConnect() == True:
            app.Search_bar()
        else:
            app.NoConnectPrompt()
        app.mainloop()
except:
    messagebox.showinfo("", 'Error!')
