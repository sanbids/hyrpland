
################
#    modules   #
################

from pathlib import Path
from PIL import Image
from tkinter import Tk, Canvas, PhotoImage
import customtkinter

##################################################################################



######## path for image ##########
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/home/sanbid/Desktop/assigment/pythonProject/assets/frame0")
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)



##################################
#   Tkinter (customtkinter)      #
##################################

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


#############################################
#      Image insert through                 #
#         PIL module and canvas             #   
#############################################

def create_image_on_canvas(canvas, image_path, x, y):
    image = PhotoImage(file=relative_to_assets(image_path))
    canvas.create_image(x, y, image=image)
    return image

image_definitions = [
    ("image_1.png", 636.841796875, 307.7407531738281),
    ("image_2.png", 97.0, 461.0),
    ("image_3.png", 1135.6328163146973, 517.0098876953125),
    ("image_4.png", 1270.0, -60.0),
    ("image_5.png", 554.0, 582.0),
    ("image_6.png", 1576.0, 1105.0),
    ("image_7.png", 1610.0, 901.0),
    ("image_8.png", 605.0, 1135.0),
    ("image_9.png", 571.0, 931.0),
    ("image_10.png", 1501.0, 494.0),
    ("image_11.png", 1528.0, 684.0),
    ("image_13.png", 49.9990234375, 308.17852783203125),
    ("image_15.png", 49.9990234375, 395.630615234375),
    ("image_17.png", 49.62017822265625, 483.0828857421875),
    ("image_21.png", 44.92340087890625, 222.22222900390625),
    ("image_22.png", 1465.0, 823.0),
    ("image_23.png", 1467.0, 800.0),
    ("image_24.png", 1467.0, 794.0),
]

img = []
for image_def in image_definitions:
    output = create_image_on_canvas(canvas, *image_def)
    img.append(output)
    
##########################################################################################################

##################################
#        Text making through     #
#                   canvas       #
##################################
def create_canvas_text(canvas, x, y, anchor, text, fill, font_name, font_size):
    canvas.create_text(
        x,
        y,
        anchor=anchor,
        text=text,
        fill=fill,
        font=(font_name, font_size * -1)
    )
    
create_canvas_text(canvas, 33.0, 57.348876953125, "nw", "BEST FITNESS", "#49B9C0", "RalewayRoman Bold", 24)
create_canvas_text(canvas, 57.0, 96.562744140625, "nw", "( hattiban,lalitpur)", "#FFFFFF", "RalewayRoman Regular", 12)
create_canvas_text(canvas, 430.0, 700.0, "nw", "Transform Your Life with 'BEST FITNESS'", "#6A89CC", "RalewayRoman ExtraBold", 32)
create_canvas_text(canvas, 416.0, 757.0, "nw", "Welcome to BEST FITNESS, your ultimate destination for all things fitness and wellness.\n We believe that a healthy body and mind are the cornerstones of a fulfilling life, \n and we're here to guide you on your journey towards achieving your fitness goals \n and embracing a vibrant lifestyle.", "#555555", "RalewayRoman Regular", 16)

################################################################################################################################


##################################
#        Basic Button            #
#        (logout,add cart)       #
##################################

def basic_button(window, text, width, height, font_color, bg_color, hover_color, x, y, command):
    button = customtkinter.CTkButton(
        window, corner_radius=13, text=text, width=width, height=height, font=("JetBrainMono", 17),
        bg_color=bg_color, fg_color=font_color, hover_color=hover_color, command=command
    )
    button.place(x=x, y=y)
    return button

button_definitions = [
    ("Add Cart   ", 150, 60, "#363E52", "#14162E", "#499E2C", 1560.0, 140.0, lambda: print("add cart")),
    ("Logout   󰍃 ", 216, 58, "#D24444", "#14162E", "#b23b3b", 34.0, 880.0, lambda: print("button4")),
    ("instruction", 216, 66, "#363E52", "#212D43", "#A61C4E", 411.0, 877.0, lambda: print("button1")),
    ("View features  󱐌", 216, 66, "#363E52", "#212D43", "#A61C4E", 726.0, 874.0, lambda: print("button2")),
    ("     Sanbid", 150, 50, "#363E52", "#14162E", "#2F3749", 1575.0, 40.0, lambda: print("user")),
]

buttons = []
for definition in button_definitions:
    button = basic_button(window, *definition)
    buttons.append(button)

####################################################################################################

######### Dashboard button ################
def dashboard_button(window, text, width, height, font_color, bg_color, hover_color, x, y, command,images,text_col):
    images = customtkinter.CTkImage(light_image=Image.open(images),size=(28,28))
    button = customtkinter.CTkButton(
        window, corner_radius=10, text=text, width=width, height=height, font=("JetBrainMono", 20),
        bg_color=bg_color, fg_color=font_color, hover_color=hover_color, command=command,image=images,anchor="center",text_color=text_col
    )
    button.place(x=x, y=y)
    return button

button_definitions_dashboard = [
    ("   Dashboard", 220, 50, "#1A3290", "#1A3245", "#1A3287", 20, 200, lambda: print("dashboard"),"./assets/frame0/image_20.png","#FFFFFF"),
    ("   Statistics", 220, 50, "transparent", "transparent", "#1A3290", 20, 300, lambda: print("Statistics"),"./assets/frame0/image_12.png","#8B8C91"),
    ("   Schedule", 220, 50, "transparent", "transparent", "#1A3290", 20, 400, lambda: print("Schedule"),"./assets/frame0/image_16.png","#8B8C91"),
    ("   Settings", 220, 50, "transparent", "transparent", "#1A3290", 20, 500, lambda: print("Settings"),"./assets/frame0/image_19.png","#8B8C91"),
    ("   Reports", 220, 50, "transparent", "transparent", "#1A3290", 20, 600, lambda: print("Reports"),"./assets/frame0/image_14.png","#8B8C91"),
    ("   Message", 220, 50, "transparent", "transparent", "#1A3290", 20, 700, lambda: print("Message"),"./assets/frame0/image_18.png","#8B8C91"),

]

buttons_dashboard = []
for definition in button_definitions_dashboard:
    button = dashboard_button(window, *definition)
    buttons_dashboard.append(button)

########### search input ##################
entry1 = customtkinter.CTkEntry(window, placeholder_text="Search your course .......",width=452,height=45,font=("JetBrainMono",14), fg_color="#2E323C",text_color="#fff",border_width=0,corner_radius=12)
entry1.place(x=677.6499996185303,y=160)


##############################
#    making theme for        #
#           product          #
##############################

def create_product_label(window,text, image_path, x, y,sizex,sizey,ach):
    product_image = customtkinter.CTkImage(light_image=Image.open(image_path), size=(sizex, sizey))
    product_label = customtkinter.CTkLabel(window,text=text,compound="bottom",corner_radius=14, text_color="#C7D2CE", font=("JetBrainMono",24,"bold"), image=product_image, width=343, height=378, bg_color="#2E374B",anchor=ach,pady=10)
    product_label.place(x=x, y=y)
    return product_label


product1 = create_product_label(window,"GYM course", "./assets/frame0/image_25.png", 295, 243,330,295,"n")
product2 = create_product_label(window,"Private Trainer", "./assets/frame0/co.png", 666, 243,290,260,"n")
product3 = create_product_label(window,"Swimming \n", "./assets/frame0/swimming.png", 1029, 243,280,190,"n")
product4 = create_product_label(window,"Sauna", "./assets/frame0/suna.png", 1391, 243,300,270,"nw")


################################################################################################################################

############ button for profuct ################
def create_button(window, x, y, text, font_color, bg_color, hover_color, command):
    button = customtkinter.CTkButton(
        window, width=114, height=51, text=text, font=("JetBrainMono", 18),
        corner_radius=13, bg_color=bg_color, border_width=0,
        fg_color=font_color, hover_color=hover_color, command=command
    )
    button.place(x=x, y=y)
    return button

button_positions = [
    (316, 557, "See Info   ", "#077E71", "#2E374B", None, lambda: print("info")),
    (513, 557, "Buy", "#BD1313", "#2E374B", "#8A1414", lambda: print("buy")),
    (872, 557, "Buy", "#BD1313", "#2E374B", "#8A1414", lambda: print("buy")),
    (1230, 557, "Buy", "#BD1313", "#2E374B", "#8A1414", lambda: print("buy")),
    (1598, 557, "Buy", "#BD1313", "#2E374B", "#8A1414", lambda: print("buy")),
    (689, 557, "See Info   ", "#077E71", "#2E374B", None, lambda: print("info")),
    (1051, 557, "See Info   ", "#077E71", "#2E374B", None, lambda: print("info")),
    (1413, 557, "See Info   ", "#077E71", "#2E374B", None, lambda: print("info")),
]

buttons = []
for position in button_positions:
    button = create_button(window, *position)
    buttons.append(button)


image_image_25 = PhotoImage(
    file=relative_to_assets("image_25.png"))
image_25 = canvas.create_image(
    473.0,
    426.0,
    image=image_image_25
)


window.resizable(False, False)
window.mainloop()
