
from pathlib import Path

import tkinter as tk
from tkinter import END, Tk, Canvas, PhotoImage,messagebox
import customtkinter
from PIL import Image
import pymysql

def loginPage():
    window.destroy()
    import login

def clear():
    email.delete(0,END)
    username.delete(0,END)
    password.delete(0,END)
    againPassword.delete(0,END)
    check.set(0)
 
def connect_db():
    if email.get() == '' or username.get() == '' or password.get() == '' or againPassword == '':
        messagebox.showerror('Error','All Fields Are Required')
        
    elif password.get() != againPassword.get():
        messagebox.showerror('Error','Password Mismatch')
    elif check.get() == 0:
        messagebox.showerror('Error','Please Accept Term and Condition')
    else:
        try:
            con = pymysql.connect(host='localhost',user='root',password='33533')
            mycursor = con.cursor()
        except:
            messagebox.showerror('error','database not connected !!')
            return
        
        mycursor.execute('use python_register')       

        query = 'select * from register_account where username=%s'
        mycursor.execute(query,(username.get()))

        row=mycursor.fetchone()
        if row != None:
            messagebox.showerror('error','Username Already exists')
        else:
            query = 'insert into register_account(email,username,password) values(%s,%s,%s)'
            mycursor.execute(query,(email.get(),username.get(),password.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success','Registeration is Successfuly')
            clear()
            window.destroy()
            import login


OUTPUT_PATH = Path(__file__).parent
Login_assets_PATH = OUTPUT_PATH / Path(r"/home/sanbid/Desktop/build/Login_assets/frame0")

customtkinter.set_appearance_mode('dark')

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

image_image_9 = PhotoImage(
    file=relative_to_Login_assets("image_9.png"))
image_9 = canvas.create_image(
    800.0,
    540.0,
    image=image_image_9
)



gymImage = customtkinter.CTkImage(light_image=Image.open("./Login_assets/frame0/image_9.png"))

def create_image_label(master, image, x, y):
    image_label = customtkinter.CTkLabel(master=master,
                                         width=120,
                                         height=60,
                                         fg_color=("white", "gray75"),
                                         corner_radius=8,
                                         image=image,
                                         text="")
    image_label.place(x=x, y=y)

# Usage
image3 = customtkinter.CTkImage(light_image=Image.open("./Login_assets/frame0/image_3.png"),
                                  dark_image=Image.open("./Login_assets/frame0/image_3.png"),
                                  size=(30, 30))
create_image_label(window, image3, x=1495.0, y=712.0)

image4 = customtkinter.CTkImage(light_image=Image.open("./Login_assets/frame0/image_4.png"),
                                  dark_image=Image.open("./Login_assets/frame0/image_4.png"),
                                  size=(30, 30))
create_image_label(window, image4, x=1355.0, y=712.0)

image5 = customtkinter.CTkImage(light_image=Image.open("./Login_assets/frame0/google.png"),
                                  dark_image=Image.open("./Login_assets/frame0/google.png"),
                                  size=(30, 30))
create_image_label(window, image5, x=1215.0, y=712.0)

def create_text(canvas, x, y, anchor, text, fill, font_size, font_weight="normal"):
    font = ("Poppins " + font_weight, font_size * -1)
    canvas.create_text(x, y, anchor=anchor, text=text, fill=fill, font=font)

# Usage
create_text(canvas, 1460.0, 565.0, "nw", "Recover Password ?", "#C7C7C7", 14)
create_text(canvas, 1350.0, 670.0, "nw", "Or continue with", "#FFFFFF", 14)
create_text(canvas, 163.0, 85.0, "nw", "Home", "#FFFFFF", 17, "Medium")
create_text(canvas, 302.0, 85.0, "nw", "About", "#FFFFFF", 17, "Medium")
create_text(canvas, 441.0, 87.0, "nw", "Contact", "#FFFFFF", 17, "Medium")
create_text(canvas, 1380.925537109375, 81.51165771484375, "nw", "Sign in", "#4461F2", 17, "Bold")
create_text(canvas, 139.0, 389.0, "nw", "Welcome To\n BEST FITNESS", "#FFFFFF", 58, "Bold")
create_text(canvas, 115.0, 607.0, "nw", "“Your body can stand almost anything. \n It’s your mind that you have to convince.”", "#FFFFFF", 23, "Medium")
create_text(canvas, 1212.0, 160.0, "nw", "User/Admin Login", "#718BE7", 30, "Bold")

email = customtkinter.CTkEntry(window, placeholder_text="Email", width=400,height=52,corner_radius=11,border_width=0)
email.place(x=1210,y=220)

username = customtkinter.CTkEntry(window, placeholder_text="Username", width=400,height=52,corner_radius=11,border_width=0)
username.place(x=1210,y=300)

password = customtkinter.CTkEntry(window, placeholder_text="Pasword", width=400,height=52,corner_radius=11,border_width=0)
password.place(x=1210,y=380)

againPassword = customtkinter.CTkEntry(window, placeholder_text="Again Password", width=400,height=52,corner_radius=11,border_width=0)
againPassword.place(x=1210,y=460)

check = tk.IntVar()
termCodition = customtkinter.CTkCheckBox(window,text=" I agree to the Term & Condition",font=("JetBrainsMono",14,"bold"),cursor="hand2",variable=check)
termCodition.place(x=1220,y=535)

registerBtn = customtkinter.CTkButton(window,text="Sign up",cursor="hand2",width=400,height=60,fg_color="red" , font=("Poppins",20),command=connect_db)
registerBtn.place(
    x=1210.0,
    y=600.0,
)


button2 = customtkinter.CTkButton(window,text="Login",cursor="hand2",width=100,height=40 , font=("Poppins",18), command=loginPage)
button2.place(
    x=1474.0,
    y=79.0,
)

window.resizable(False, False)
window.mainloop()
