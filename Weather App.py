from tkinter import*
#pip install requests
import requests
root=Tk()
#aaae6c3f780dcad826af617e72cffd6e
def getWeather():
    city=textField.get()#since we will get in name entry box we need to give name.get
    api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=aaae6c3f780dcad826af617e72cffd6e"
    _data=requests.get(api).json()
    condition=_data['weather'][0]['main']
    temp=int(_data['main']['temp']-273.15)
    pressure=_data['main']['pressure']
    humidity=_data['main']['humidity']
    wind_speed=_data['wind']['speed']
                                  
                                  
    final_info="sky condition:"+condition+"\n"+"Temp:"+str(temp)+"°c"+"\n"+"Pressure:"+str(pressure)
    label.config(text=final_info)
    result=".Humidity:"+str(humidity)+"/n"+"Wind Speed :"+str(wind_speed) label1.config(text=result)
                                
    
root.title("Weather App")
root.config(bg="pink")
a=Label(root,text="WEATHER APP",font=("poppins",25))
a.pack()

                                  
textField=Entry(root,justify="center",font=("poppins",20,"bold"))
textField.pack(pady=40)#Margin
textField.bind("<Return>",getWeather)
label=Label(root,font=("poppins",15))
label.pack()
label1=Label(root,font=("popppins",20))
label1.pack()
root.mainloop()
