import tkinter as tk
from pathlib import Path
from tkinter import Tk, Canvas, PhotoImage
import customtkinter as ct
from PIL import Image,ImageTk
from tkinter import ttk

window = tk.Tk()
window.geometry("1800x1000")
window.configure(bg = "#14162E")
backgrounColor = "#14162E"


main_frame = ct.CTkFrame(window,width=1568,height=911)
main_frame.place(x=272,y=98)

######################################### -> Top Frame <- ######################################################################

header_frame = ct.CTkFrame(window,width=1800,height=100,fg_color=backgrounColor)
header_frame.place(x=0,y=0)

companyName_lebal = ct.CTkLabel(header_frame,font=("RalewayRoman Bold",24),text_color="#49B9C0",text="BEST FITNESS")
companyName_lebal.place(x=43.0,y=40)

companyAddress = ct.CTkLabel(header_frame,font=("RalewayRoman Bold",12),text_color="#FFFFFF",text="( hattiban,lalitpur)")
companyAddress.place(x=60.0,y=70)

UserButton = ct.CTkButton(
        header_frame, corner_radius=13, text="     Sanbid", width=150, height=50, font=("JetBrainMono", 17),
        bg_color="#14162E", fg_color="#363E52", hover_color="#2F3749", command=lambda: print("user"))
UserButton.place(x=1575, y=40)

#################################################################################################################################


######################################### -> SIDE MENU PART <- ###################################################################

side_menu_frame = ct.CTkFrame(window,width=276,height=900,fg_color=backgrounColor)
side_menu_frame.place(x=0,y=100)

################################ dashboard ###########################################################################
def dashBoard_search(parent):
    sarchAndCart_Frame = ct.CTkFrame(parent,width=1527,height=110,fg_color=backgrounColor)
    sarchAndCart_Frame.place(x=0,y=0)
    entry1 = ct.CTkEntry(sarchAndCart_Frame, placeholder_text="Search your course .......",width=452,height=45,font=("JetBrainMono",14), fg_color="#2E323C",text_color="#fff",border_width=0,corner_radius=12)
    entry1.place(x=495,y=50)
    AddCart_btn = ct.CTkButton(
        sarchAndCart_Frame, corner_radius=13, text="Add Cart   ", width=150, height=60, font=("JetBrainMono", 17),
        bg_color="#14162E", fg_color="#363E52", hover_color="#499E2C", command=lambda: print("user"))
    AddCart_btn.place(x=1300, y=40)

def create_product_frame_tab(tab, image_path, x=0, y=0, width=700, height=378, fg_color="#2E374B", corner_radius=10):
    productFrame = ct.CTkFrame(tab, width=width, height=height, fg_color=fg_color, corner_radius=corner_radius)
    productFrame.place(x=x, y=y)

    product_image = ct.CTkImage(light_image=Image.open(image_path), size=(width - 40, height - 80)) 
    product_label = ct.CTkLabel(productFrame, image=product_image, text="", fg_color="#2C3546", width=width - 40)
    product_label.place(x=-20, y=-40)

def dashboard_product(parent):
    product_frame = ct.CTkFrame(parent,width=1527,height=420,fg_color=backgrounColor)
    product_frame.place(x=0,y=109)

    #### tab #####
    notebook = ct.CTkTabview(product_frame,width=1510,height=410,fg_color=backgrounColor,segmented_button_fg_color=backgrounColor,text_color="black")
    notebook.place(x=5,y=15)

    ### making tab #####
    tab1 = notebook.add("Gym course and Private trainer")
    tab2 = notebook.add("Swimming session")
    tab3 = notebook.add("sunana session")

    productFrame = ct.CTkFrame(tab1,width=700,height=378,fg_color="#2E374B",corner_radius=10)
    productFrame.place(x=30,y=5)

    product1_image = ct.CTkImage(light_image=Image.open("./assets/frame0/firstorder.png"),size=(310,500)) 
    procduct1_label = ct.CTkLabel(productFrame,image=product1_image,text="",fg_color="#2C3546",width=360)
    procduct1_label.place(x=-20,y=-90)


    productFrame2 = ct.CTkFrame(tab1,width=700,height=378,fg_color="#2E374B")
    productFrame2.place(x=740,y=5)

    product1_image2 = ct.CTkImage(light_image=Image.open("./assets/frame0/co.png"),size=(300,300)) 
    procduct1_label2 = ct.CTkLabel(productFrame2,image=product1_image2,text="",fg_color="#2C3546",height=380,width=360)
    procduct1_label2.place(x=0,y=0)

    productFrame_tab2 = ct.CTkFrame(tab2,width=1100,height=378,fg_color="#2E374B")
    productFrame_tab2.place(x=200,y=5)

    product1_image2 = ct.CTkImage(light_image=Image.open("./assets/frame0/swimming.png"),size=(500,300)) 
    procduct1_label2 = ct.CTkLabel(productFrame_tab2,image=product1_image2,text="",fg_color="#2C3546",width=560,height=380)
    procduct1_label2.place(x=0,y=0)


    productFrame_tab3 = ct.CTkFrame(tab3,width=900,height=378,fg_color="#2E374B")
    productFrame_tab3.place(x=300,y=5)

    product1_image3 = ct.CTkImage(light_image=Image.open("./assets/frame0/suna.png"),size=(400,400)) 
    procduct1_label3 = ct.CTkLabel(productFrame_tab3,image=product1_image3,text="",width=410,height=410,fg_color="#2C3546")
    procduct1_label3.place(x=0,y=0)



def dashBoard_foot(parent):
    foot_frame = ct.CTkFrame(parent,width=1527,height=380,fg_color=backgrounColor)
    foot_frame.place(x=0,y=520)
    design_frame = ct.CTkFrame(foot_frame,width=1320,height=340,fg_color="#2E374B",corner_radius=30)
    design_frame.place(x=100,y=25)
    foot_heading = ct.CTkLabel(design_frame,font=("RalewayRoman ExtraBold",32),text_color="#6A89CC",text="Transform Your Life with 'BEST FITNESS'")
    foot_heading.place(x=140,y=40)
    foot_paragraph = ct.CTkLabel(design_frame,font=("RalewayRoman Regular",16),text_color="#C9C1C1",text="Welcome to BEST FITNESS, your ultimate destination for all things fitness and wellness.\n We believe that a healthy body and mind are the cornerstones of a fulfilling life, \n and we're here to guide you on your journey towards achieving your fitness goals \n and embracing a vibrant lifestyle.")
    foot_paragraph.place(x=120,y=100)
    Instruction_btn = ct.CTkButton(
        design_frame, corner_radius=13, text="instruction", width=216, height=66, font=("JetBrainMono", 17),
        bg_color="#2E374B", fg_color="#22262F", hover_color="#A61C4E", command=lambda: print("user"))
    Instruction_btn.place(x=180, y=230)
    
    Instruction_btn = ct.CTkButton(
        design_frame, corner_radius=13, text="View features  󱐌", width=216, height=66, font=("JetBrainMono", 17),
        bg_color="#2E374B", fg_color="#22262F", hover_color="#A61C4E", command=lambda: print("user"))
    Instruction_btn.place(x=500, y=230)

    
    foot_Image = ct.CTkImage(light_image=Image.open('./assets/frame0/image_24.png'),size=(250,250))
    foot_Image_label = ct.CTkLabel(design_frame,image=foot_Image,text="",fg_color="#274250",corner_radius=37)
    foot_Image_label.place(x=970,y=50)

    

def dashboardPage():
    dashbaordframe = ct.CTkFrame(main_frame,width=1568,height=911,fg_color="black")
    dashbaordframe.place(x=0,y=0)
    heading = ct.CTkLabel(dashbaordframe,text="Dashboard", font=("",20),text_color="white")
    heading.place(x=200,y=50)
    dashBoard_search(dashbaordframe)
    dashboard_product(dashbaordframe)
    dashBoard_foot(dashbaordframe)
    
################################################################################################################################# 
def statisticsPage():
    statisticsFrame = ct.CTkFrame(main_frame,width=1568,height=911,fg_color="black")
    statisticsFrame.place(x=0,y=0)
    heading = ct.CTkLabel(statisticsFrame,text="statistics", font=("",20),text_color="white")
    heading.place(x=200,y=50)


def settingPage():
    ScheduleFrame = ct.CTkFrame(main_frame,width=1568,height=911,fg_color="black")
    ScheduleFrame.place(x=0,y=0)
    heading = ct.CTkLabel(ScheduleFrame,text="settings", font=("",20),text_color="white")
    heading.place(x=200,y=50)
    

def dashboardbtn(event,clearColor,page):
    clearColor()
    event.configure(fg_color="#1A3290",text_color="#FFFFFF")
    page()

def statisticsbtn(event,clearColor,page):
    clearColor()
    event.configure(fg_color="#1A3290",text_color="#FFFFFF")
    page()

    
def Settingbtn(event,clearColor,page):
    clearColor()
    event.configure(fg_color="#1A3290",text_color="#FFFFFF")
    page()
    
def Schedulebtn(event,clearColor):
    clearColor()
    event.configure(fg_color="#1A3290",text_color="#FFFFFF")
    
def ReportBtn(event,clearColor):
    clearColor()
    event.configure(fg_color="#1A3290",text_color="#FFFFFF")
    
def MessageBtn(event,clearColor):
    clearColor()
    event.configure(fg_color="#1A3290",text_color="#FFFFFF")

def clearColor():
    for button in buttons_menu:
        button.configure(fg_color="transparent",text_color="#8B8C91")
    
def side_menu_button(window, text, width, height, font_color, bg_color, hover_color, x, y, command,images,text_col):
    images = ct.CTkImage(light_image=Image.open(images),size=(28,28))
    button = ct.CTkButton(
        window, corner_radius=10, text=text, width=width, height=height, font=("JetBrainMono", 20),
        bg_color=bg_color, fg_color=font_color, hover_color=hover_color, command=command,image=images,anchor="center",text_color=text_col
    )
    button.place(x=x, y=y)
    return button

button_definitions_sidebar= [
    ("   Dashboard", 220, 50, "transparent", "transparent", "#1A3290", 20, 100, lambda: dashboardbtn(buttons_menu[0],clearColor,dashboardPage),"./assets/frame0/image_20.png","#8B8C91"),
    ("   Statistics", 220, 50, "transparent", "transparent", "#1A3290", 20, 200, lambda: statisticsbtn(buttons_menu[1],clearColor,statisticsPage),"./assets/frame0/image_12.png","#8B8C91"),
    ("   Schedule", 220, 50, "transparent", "transparent", "#1A3290", 20, 400, lambda: Schedulebtn(buttons_menu[2],clearColor),"./assets/frame0/image_19.png","#8B8C91"),
    ("   Settings", 220, 50, "transparent", "transparent", "#1A3290", 20, 300, lambda: Settingbtn(buttons_menu[3],clearColor,settingPage),"./assets/frame0/image_16.png","#8B8C91"),
    ("   Reports", 220, 50, "transparent", "transparent", "#1A3290", 20, 500, lambda: ReportBtn(buttons_menu[4],clearColor),"./assets/frame0/image_14.png","#8B8C91"),
    ("   Message", 220, 50, "transparent", "transparent", "#1A3290", 20, 600, lambda: MessageBtn(buttons_menu[5],clearColor),"./assets/frame0/image_18.png","#8B8C91"),

]

buttons_menu= []
for definition in button_definitions_sidebar:
    button = side_menu_button(side_menu_frame, *definition)
    buttons_menu.append(button)

################################################################################################################################################################################################################

dashboardPage()




window.mainloop()
