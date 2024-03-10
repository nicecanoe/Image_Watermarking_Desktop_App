# import Pillow
import tkinter
from tkinter import filedialog
from PIL import ImageTk, Image, ImageGrab
import time



def treat_image():
#首先显读取用户上传图片并显示
    #确保图片在函数运行完后不会被清除，保证图片正常显示
    global img
    file_path = filedialog.askopenfilename()
    print(file_path)
    orig_image = Image.open(file_path)
    img = ImageTk.PhotoImage(orig_image)
    img_width = img.width()
    img_height = img.height()
    print(img_width, img_height)
    canvas.config(width=img_width, height=img_height)
    #第一设定后，后续要更改时使用canvas.coords(canvas_img, new_x, new_y)
    canvas.coords(canvas_img, img_width/2, img_height/2)
    canvas.itemconfig(canvas_img,image=img)
#开始做水印
    canvas.coords(canvas_title,img_width, img_height)
    windows.update()
#储存图片
    canvas.postscript(file="canvas.ps", colormode='color')

    img_save = Image.open("canvas.ps")
    img_save.save("canvas.png", 'png')





windows = tkinter.Tk()
windows.title("Image Colour Palette Generator")
windows.config(padx=20,pady=20)


the_title = tkinter.Label(windows, text="Image Colour Palette", font=("Arial",24))
the_title.grid(row=0, column=1)



canvas = tkinter.Canvas(highlightthickness=0)
orig_image = Image.open("yangweili.jpeg")
resized_image = orig_image.resize((500, 707), Image.ANTIALIAS)
img = ImageTk.PhotoImage(resized_image)
img_width = img.width()
img_height = img.height()
canvas.config(width=img_width, height=img_height)
canvas_img = canvas.create_image(img_width/2, img_height/2,image=img)
canvas_title = canvas.create_text(img_width, img_height, text="Copyright © 2024 yangweili. All rights reserved.",
                                  font=("Courier", 16), anchor="se", fill="white")

canvas.grid(row=1, column=1)

the_upload_button = tkinter.Button(text="upload the image", command=treat_image,width=20,height=2)
the_upload_button.grid(row=2, column=1)

windows.mainloop()