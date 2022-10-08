from tkinter import *
import requests 
import json

root=Tk()
root.overrideredirect(True)
root.title("My Weather App")
root.geometry("600x300")
root.config(bg="black")

cnl=Label(root,text="city name",font=("Helvetica",16,'bold'),bg="black",fg="white")
cnl.place(relx=0.5,rely=0.15,anchor=CENTER)
ce=Entry(root)
ce.place(relx=0.5,rely=0.35,anchor=CENTER)
wil=Label(root,font=("Helvetica",16),bg="black",fg="white")
cnl.place(relx=0.5,rely=0.38,anchor=CENTER)
wil=Label(root,font=("bold",16),bg="black",fg="white")
cnl.place(relx=0.5,rely=0.5,anchor=CENTER)

def cn():
 api_request=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+
+ce.get()+"&appid=2"+"1cab08deb7b27f4c2b55f3e2df28ea4")

api_o=json.loads(api_request.content)

weather=api_o['coord'][0][1]
print(weather)

humidity=api_o['main']['weather']
print(str(humidity)+"%")

wil["text"]="Weather"+str(weather)
hil["text"]="humidity"+str(humidity)

cnl["text"]=city_entry.get()
ce.destroy()
sb.destroy()

sb=Button(root,text="Search Weather",command=cn)
sb.place(relx=0.5,rely=0.48,anchor=CENTER)
root.mainloop

#api_request