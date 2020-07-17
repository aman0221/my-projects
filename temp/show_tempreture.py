import requests
import pandas as pd
import numpy as np
from tkinter import * 
root = Tk()
# setting the windows size 
root.geometry("600x400") 
   
# declaring string variable for storing unit,city name and update 
unit_var=StringVar() 
update_var=StringVar() 
city_var=StringVar() 
  
# defining a function that will get the city name, unit and update 
# and then print temperature of that city on the window and update on excel sheet as well  
def show_temp():
   unit=unit_entry.get() 
   update=update_entry.get()
   city=city_var.get()
   foot = Tk()
   foot.geometry("600x100")
   
   params = {
     'access_key': 'd429d4846c3cea55eceebf484c4f716a',
     'query': city
   }
   api_result = requests.get('http://api.weatherstack.com/current', params)
   api_response = api_result.json()
   if unit == "C" and update == "1":
      txt = ("Current temperature in " + api_response['location']['name']+" is "+str(api_response['current']['temperature']) + " degree celsius")
      label=Label(foot, text= txt)
      label.pack()
      foot.mainloop()
   elif unit == "F" and update == "1":  
      txt = ("Current temperature in " + api_response['location']['name']+" is "+str(api_response['current']['temperature']*9/5+32) + " fahrenheit")
      label=Label(foot, text= txt)
      label.pack()
      foot.mainloop()
      #print(u'Current temperature in %s is %d' % (api_response['location']['name'], api_response['current']['temperature']+32))
   elif unit == "C" and update == "0":
      txt = ("the updating process is stoped now")
      label=Label(foot, text= txt)
      label.pack()
      foot.mainloop()
   elif unit == "F" and update == "0":      
      txt = ("the updating process is stoped now")
      label=Label(foot, text= txt)
      label.pack()
      foot.mainloop()
      
# creating a label for unit using widget Label 
unit_label = Label(root, text = 'Unit', font=('calibre', 10, 'bold')) 

# creating a entry for input unit using widget Entry 
unit_entry = Entry(root, textvariable = unit_var,font=('calibre',10,'normal')) 

# creating a label for update using widget Label 
update_label = Label(root, text = 'update', font=('calibre', 10, 'bold')) 

# creating a entry for input update using widget Entry 
update_entry = Entry(root, textvariable = update_var,font=('calibre',10,'normal')) 

# creating a label for unit using widget Label 
city_label = Label(root, text = 'city name', font=('calibre', 10, 'bold')) 

# creating a entry for input unit using widget Entry 
city_entry = Entry(root, textvariable = city_var,font=('calibre',10,'normal')) 

# creating a button using the widget Button that will call the show_temp function  
show=Button(root,text = 'Show temperature', command = show_temp)

# placing the label and entry in the required position using grid method 
unit_label.grid(row=0,column=0) 
unit_entry.grid(row=0,column=1) 
update_label.grid(row=1,column=0) 
update_entry.grid(row=1,column=1) 
city_label.grid(row=2,column=0) 
city_entry.grid(row=2,column=1) 
show.grid(row=3,column=1) 
   
# performing an infinite loop for the window to display 
root.mainloop()
