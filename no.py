from tkinter import*
import phonenumbers
from phonenumbers import geocoder,carrier,timezone
root=Tk()
root.geometry("1400x700")
root["bg"]="GREY"
def runcodee():
    phonenumber1 = e_name.get()
    phn=phonenumbers(phonenumber1)
    country_name.config(text=f"Country Name:{geocoder.country_name_for_number(phn,lang='en')}")
    carrier_name.config(text=f"Carrier Name:{carrier.name_for_number(phn,lang='en')}")
    time_zone.config(text=f"Time Zone:{timezone.time_zones_for_number(phn)}")

lbl1= Label(root,text="NUMBER FINDER",bg="GREY",fg="white",font="arial 46 italic bold")
lbl1.pack()

lbl_name=Label(root,text="ENTER YOUR NUMBER:",font="arial 35 bold",fg="black",bg="GREY")
lbl_name.place(x=103,y=200)

e_name=Entry(root,font="arial 28 bold",bg="white",fg="cyan")
e_name.place(x=920,y=200)

s_btn=Button(root,text="SUBMIT",font="arial 40 bold ",fg="black",bg="cyan",bd="10",command=runcodee)
s_btn.place(x=650,y=400)

country_name=Label(root,font="arial 30 bold",bg="GREY",fg="cyan")
country_name.place(x=400,y=330)

carrier_name=Label(root,font="arial 30 bold",bg="GREY",fg="cyan")
carrier_name.place(x=580,y=690)

time_zone=Label(root,font="arial 30 bold",bg="GREY",fg="cyan")
time_zone.place(x=990,y=600)

mainloop()