# import all the requirt libraries
from tkinter import *  
import os
import pydicom
import numpy as np
from pydicom.data import get_testdata_files
import PIL
from io import BytesIO 
from PIL import ImageTk,Image,ImageEnhance  
root = Tk()  

# declear variables
angle=0  # degree to rotate the image
change_in_width=0
change_in_height=0
change_in_brightness=1
change_in_contrast=1
cnt=0
starter = 0
iterator=0
# path to direcrories 
directory = (r'E:\setup\series-000001')
list_dir = os.listdir(r'E:\setup\series-000001')

# defining functions
def loadimg1():
   load_img(iterator=1)

def loadimg2():
   load_img(iterator=-1)
    
def load_img(iterator=iterator):
   global canvas
   global imgtk,img,gl,gw,cnt,starter
   if starter==0:
      canvas = Canvas(root, width = 600, height = 600)
   canvas.delete("all")
   starter = 1
   img = pydicom.dcmread(os.path.join(directory,list_dir[cnt])).pixel_array
   img = PIL.Image.fromarray(img)         
   cnt+=iterator                                 
   print(cnt)
   img.mode = 'L'
   b = BytesIO()
   img.save(b,format="jpeg")
   img = Image.open(b)
   #print(type(img))
   gw = img.size[0]
   gl = img.size[1]
   imgtk = ImageTk.PhotoImage(img)  
   canvas.create_image(0, 0, anchor=NW, image=imgtk)
   canvas.pack()   
   
def zoomin():
   global imgtk,change_in_width,change_in_height
   change_in_height+=5
   change_in_width+=5
   newsize = (gw+change_in_width,gl+change_in_height)
   canvas.delete("all")
   #img.show()
   imgtk = ImageTk.PhotoImage(img.resize(newsize,0))
   canvas.create_image(20, 20, anchor=NW, image=imgtk)
   
def zoomout():
   global imgtk,change_in_width,change_in_height
   change_in_width-=5
   change_in_height-=5
   newsize = (gw+change_in_width,gl+change_in_height)
   canvas.delete("all")
   #img.show()
   imgtk = ImageTk.PhotoImage(img.resize(newsize,0))
   canvas.create_image(20, 20, anchor=NW, image=imgtk)

def rotate_right():
   global imgtk,angle
   angle+=5
   #img.show()
   canvas.delete("all")
   imgtk = ImageTk.PhotoImage(img.rotate(angle))  
   canvas.create_image(20, 20, anchor=NW, image=imgtk)   

def rotate_left():
   global imgtk,angle
   angle-=5
   #img.show()
   canvas.delete("all")
   imgtk = ImageTk.PhotoImage(img.rotate(360+angle))  
   canvas.create_image(20, 20, anchor=NW, image=imgtk) 
   
def highbrightness():
   global imgtk,change_in_brightness
   change_in_brightness+=.1
   enhancer = ImageEnhance.Brightness(img)
   enhanced_img = enhancer.enhance(change_in_brightness)
   imgtk = ImageTk.PhotoImage(enhanced_img)
   canvas.delete("all")
   canvas.create_image(20, 20, anchor=NW, image=imgtk)
   
def lowbrightness():
   global imgtk,change_in_brightness
   change_in_brightness-=.1
   enhancer = ImageEnhance.Brightness(img)
   enhanced_img = enhancer.enhance(change_in_brightness)
   imgtk = ImageTk.PhotoImage(enhanced_img)
   canvas.create_image(20, 20, anchor=NW, image=imgtk)
   
def contrastup():
   global imgtk,change_in_contrast
   change_in_contrast+=.1
   enhancer = ImageEnhance.Contrast(img)
   enhanced_img = enhancer.enhance(change_in_contrast)
   imgtk = ImageTk.PhotoImage(enhanced_img)
   canvas.create_image(20, 20, anchor=NW, image=imgtk)
   
def contrastlow():
   global imgtk,change_in_contrast
   change_in_contrast-=.1
   enhancer = ImageEnhance.Contrast(img)
   enhanced_img = enhancer.enhance(change_in_contrast)
   imgtk = ImageTk.PhotoImage(enhanced_img)
   canvas.create_image(20, 20, anchor=NW, image=imgtk)
   
   
# button to give command
a = Button(root, text ="zoom in", command = zoomin)
a.pack( side = RIGHT )
b = Button(root, text ="zoom out", command = zoomout)
b.pack( side = LEFT )
c = Button(root, text ="rotate right", command = rotate_right)   
c.pack( side = RIGHT )
d = Button(root, text ="rotate left", command = rotate_left)
d.pack( side = LEFT )
e = Button(root, text ="contrastup", command = contrastup)
e.pack( side = RIGHT )
f = Button(root, text ="contrastlow", command = contrastlow)
f.pack( side = LEFT )
g = Button(root, text ="lowbrightness", command = lowbrightness)
g.pack( side = LEFT )
h = Button(root, text ="highbrightness", command = highbrightness)
h.pack( side = RIGHT )
i = Button(root, text ="next image", command = loadimg1)
i.pack( side = LEFT )
j = Button(root, text ="previous image", command = loadimg2)
j.pack( side = RIGHT )

root.mainloop()
