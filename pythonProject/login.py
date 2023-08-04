
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import customtkinter
from PIL import Image



OUTPUT_PATH = Path(__file__).parent
Login_assets_PATH = OUTPUT_PATH / Path(r"/home/sanbid/Desktop/build/Login_assets/frame0")


def relative_to_Login_assets(path: str) -> Path:
    return Login_assets_PATH / Path(path)


window = Tk()

window.geometry("1800x1000")
window.configure(bg = "#14162E")


canvas = Canvas(
    window,
    bg = "#14162E",
    height = 1000,
    width = 1800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)



canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_Login_assets("image_1.png"))
image_1 = canvas.create_image(
    334.0,
    684.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_Login_assets("image_2.png"))
image_2 = canvas.create_image(
    252.0,
    455.0,
    image=image_image_2
)

button1 = customtkinter.CTkButton(window,text="Sign In",width=400,height=60 , font=("Poppins",20), command=lambda: print("clicked"))
button1.place(
    x=1210.0,
    y=571.0,
)

canvas.create_text(
    1460.0,
    535.0,
    anchor="nw",
    text="Recover Password ?",
    fill="#C7C7C7",
    font=("Poppins Medium", 14 * -1)
)

canvas.create_text(
    1350.0,
    663.0,
    anchor="nw",
    text="Or continue with",
    fill="#FFFFFF",
    font=("Poppins Medium", 14 * -1)
)

gymImage = customtkinter.CTkImage(light_image=Image.open("./Login_assets/frame0/image_9.png"))

image3 = customtkinter.CTkImage(light_image=Image.open("./Login_assets/frame0/image_3.png"),
                                  dark_image=Image.open("./Login_assets/frame0/image_3.png"),
                                  size=(30, 30))

image_label3 = customtkinter.CTkLabel(master=window,
                                     width=120,
                                     height=60,
                                     fg_color=("white", "gray75"),
                                     corner_radius=8,
                                     image=image3,
                                     text="")
image_label3.place(x=1495.0,y=712.0)


image4 = customtkinter.CTkImage(light_image=Image.open("./Login_assets/frame0/image_4.png"),
                                  dark_image=Image.open("./Login_assets/frame0/image_4.png"),
                                  size=(30, 30))

image_label4 = customtkinter.CTkLabel(master=window,
                                     width=120,
                                     height=60,
                                     fg_color=("white", "gray75"),
                                     corner_radius=8,
                                     image=image4,
                                     text="")
image_label4.place(x=1355.0,y=712.0)


image5 = customtkinter.CTkImage(light_image=Image.open("./Login_assets/frame0/google.png"),
                                  dark_image=Image.open("./Login_assets/frame0/google.png"),
                                  size=(30, 30))

image_label5 = customtkinter.CTkLabel(master=window,
                                     width=120,
                                     height=60,
                                     fg_color=("white", "gray75"),
                                     corner_radius=8,
                                     image=image5,
                                     text="")
image_label5.place(x=1215.0,y=712.0)

canvas.create_text(
    163.0,
    85.0,
    anchor="nw",
    text="Home",
    fill="#FFFFFF",
    font=("Poppins Medium", 17 * -1)
)

canvas.create_text(
    302.0,
    85.0,
    anchor="nw",
    text="About",
    fill="#FFFFFF",
    font=("Poppins Medium", 17 * -1)
)

canvas.create_text(
    441.0,
    87.0,
    anchor="nw",
    text="Contact",
    fill="#FFFFFF",
    font=("Poppins Medium", 17 * -1)
)


image_image_9 = PhotoImage(
    file=relative_to_Login_assets("image_9.png"))
image_9 = canvas.create_image(
    800.0,
    540.0,
    image=image_image_9
)
canvas.create_rectangle(
    1388.3013916015625,
    116.0,
    1419.4053344726562,
    119.0,
    fill="#4461F2",
    outline="")

canvas.create_text(
    1380.925537109375,
    81.51165771484375,
    anchor="nw",
    text="Sign in",
    fill="#4461F2",
    font=("Poppins Bold", 17 * -1)
)

canvas.create_text(
    139.0,
    389.0,
    anchor="nw",
    text="Welcome To\n BEST FITNESS",
    fill="#FFFFFF",
    font=("Poppins Bold", 58 * -1)
)

canvas.create_text(
    115.0,
    607.0,
    anchor="nw",
    text="“Your body can stand almost anything. \n It’s your mind that you have to convince.”",
    fill="#FFFFFF",
    font=("Poppins Medium", 23 * -1)
)

canvas.create_text(
    1212.0,
    265.0,
    anchor="nw",
    text="User/Admin Login",
    fill="#718BE7",
    font=("Inter Bold", 30 * -1)
)

entry1 = customtkinter.CTkEntry(window, placeholder_text="Email", width=400,height=52,corner_radius=11,border_width=0)
entry1.place(x=1210,y=350)


entry2 = customtkinter.CTkEntry(window, placeholder_text="Password", width=400,height=52,corner_radius=11,border_width=0)
entry2.place(x=1210,y=440)

button2 = customtkinter.CTkButton(window,text="Register",fg_color="#E83A3A",hover_color="#D75D5D",width=100,height=40 , font=("Poppins",18), command=lambda: print("clicked"))
button2.place(
    x=1474.0,
    y=79.0,
)

window.resizable(False, False)
window.mainloop()
