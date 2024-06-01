from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from time import strftime
from datetime import datetime
import requests
api_key = 'db2d208f006995514c7028c748875395'

w = Tk() 
w.geometry('800x400')
w.title('Emma Weather APP')
w.resizable(0,0)

def weather_data(query):
        res = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={query}&appid={api_key}')
        return res.json()

Frame(w, width=800, height=50, bg='#353535').place(x=0,y=0)
imgSearch = ImageTk.PhotoImage(Image.open('search.png').resize((30,30)))

def on_entry(e):
    e1.delete(0,'end')
def on_leave(e):
    if e1.get()=='':
        e1.insert(0, 'Search City')

e1 = Entry(w, width=21, fg='white', bg='#353535', border=0)
e1.config(font=('Calibry',12))
e1.bind("<FocusIn>", on_entry)
e1.bind("<FocusOut>", on_leave)
e1.insert(0, 'Search City')
e1.place(x=620, y=15)

#date Format
a = datetime.today().strftime('%B')
b= (a.upper())
q = datetime.now().month

now = datetime.now()
c= now.strftime('%B')
month = c[0:3]

today = datetime.today()
date = today.strftime('%d')

def label(a):
    Frame(width=500, height=50, bg='#353535').place(x=0, y=0)
    
    l1 = Label(w, text=str(a), bg='#353535',fg='white')
    l1.config(font=('Calibry', 18))
    l1.place(x=20, y=8)

    w_data = weather_data(a)
    result = w_data
    try:
        check = '{}'.format(result['main']['temp'])
        print(check)
    except:
        messagebox.showinfo("", 'City not found!')

    c = (int(float(check)))
    print(c)
    description = ("{}".format(result['weather'][0]['description']))
    weather = ("{}".format(result['weather'][0]['main']))
    print(weather)

    global imgWeather

    if c>10 and (weather=='Haze' or weather=='Clear'):
        print('hi')
        Frame(w, width=800, height=350, bg="#f78954").place(x=0, y=50)
        
        photo = Image.open('icon\Black\Lighter Heat.png')
        canvas = Canvas(w, bg="blue", width=80, height=80)
        canvas.pack()
        canvas.create_image(0, 0, image=photo, anchor=NW)
        imgWeather = ImageTk.PhotoImage()
        
        Label(w, image=imgWeather, border=0).place(x=170, y=130)
        bcolor= "#f78954"
        fcolor= "white"

label(a='Roma')

def cmd1():
    pass

Button(w, image=imgSearch, command=cmd1, border=0).place(x=750, y=10)
