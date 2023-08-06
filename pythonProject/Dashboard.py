
import tkinter as tk
import customtkinter as ct
from PIL import Image



ct.set_appearance_mode("dark")
window = tk.Tk()
window.geometry("1800x1000")
window.configure(bg = "#14162E")
backgrounColor = "#14162E"


main_frame = ct.CTkFrame(window,width=1568,height=911)
main_frame.place(x=272,y=98)

######################################### -> Top Frame <- ######################################################################

def header(parent):
    header_frame = ct.CTkFrame(parent, width=1800, height=100, fg_color=backgrounColor)
    header_frame.place(x=0, y=0)
    
    company_name_label = ct.CTkLabel(header_frame, font=("RalewayRoman Bold", 24), text_color="#49B9C0", text="BEST FITNESS")
    company_name_label.place(x=43.0, y=40)
    company_address = ct.CTkLabel(header_frame, font=("RalewayRoman Bold", 12), text_color="#FFFFFF", text="(hattiban, lalitpur)")
    company_address.place(x=60.0, y=70)

    def user_button_clicked():
        print("User button clicked")

    user_button = ct.CTkButton(
        header_frame, corner_radius=13, text="     Sanbid", width=150, height=50, font=("JetBrainMono", 17),
        bg_color="#14162E", fg_color="#363E52", hover_color="#2F3749", command=user_button_clicked
    )
    user_button.place(x=1575, y=40)
    
header(window)
#################################################################################################################################


############################################################# checkout sidebar #################################################
class SlidePanel(ct.CTkFrame):
	def __init__(self, parent, start_pos, end_pos):
		super().__init__(master = parent)
		self.start_pos = start_pos + 0.04
		self.end_pos = end_pos - 0.03
		self.width = abs(start_pos - end_pos)
		self.pos = self.start_pos
		self.in_start_pos = True
		self.place(relx = self.start_pos, rely = 0.05, relwidth = self.width, relheight = 0.9)

	def animate(self):
		if self.in_start_pos:
			self.animate_forward()
		else:
			self.animate_backwards()

	def animate_forward(self):
		if self.pos > self.end_pos:
			self.pos -= 0.008
			self.place(relx = self.pos, rely = 0.05, relwidth = self.width, relheight = 0.9)
			self.after(10, self.animate_forward)
		else:
			self.in_start_pos = False

	def animate_backwards(self):
		if self.pos < self.start_pos:
			self.pos += 0.008
			self.place(relx = self.pos, rely = 0.05, relwidth = self.width, relheight = 0.9)
			self.after(10, self.animate_backwards)
		else:
			self.in_start_pos = True


#### checkout panel Items List frame #################

def ItemsList(parent):
    itemsFrame = ct.CTkScrollableFrame(parent, width=525, height=330, fg_color="red")
    itemsFrame.grid(row=1, column=0)

    product_frame_info = [
    ("Product A", 520, 100, "purple"),
    ("Product B", 520, 100, "purple"),
    ("Product C", 520, 100, "purple"),
    ("Product D", 520, 100, "purple"),
    ("Product E", 520, 100, "purple"),
    ("Product E", 520, 100, "green"),
    ]

    for row, (product_name, width, height, fg_color) in enumerate(product_frame_info):
        products_items = ct.CTkFrame(itemsFrame, width=width, height=height, fg_color=fg_color)
        products_items.grid(row=row * 2, column=0, pady=10)

        product_name_label = ct.CTkLabel(products_items, text=product_name, font=("JetBrainMono", 18), text_color="white")
        product_name_label.place(x=10, y=10)
    

##################### bill selection ##########################
def create_billing_section(parent_frame, x, y):
    billing_frame = ct.CTkFrame(parent_frame, width=525, height=270, fg_color="yellow")
    billing_frame.place(x=x, y=y)

    heading_bill = ct.CTkLabel(billing_frame, text="Billing Summary", font=("JetBrainMono", 23, "bold"), text_color="black")
    heading_bill.place(x=10, y=10)

    billing_info = [
        ("Subtotal:", "NRP 3000", 60),
        ("Discount:", "NRP -200", 100),
        ("Grand Total:", "NRP 2800", 143),
    ]

    for row, (label_text, value_text, y_offset) in enumerate(billing_info):
        label = ct.CTkLabel(billing_frame, text=label_text, font=("JetBrainMono", 18), text_color="black")
        label.place(x=10, y=y_offset)

        value_label = ct.CTkLabel(billing_frame, text=value_text, font=("JetBrainMono", 18), text_color="black")
        value_label.place(x=160, y=y_offset)

    comment = ct.CTkTextbox(billing_frame, width=500, height=100, font=("JetBrainMono", 16), text_color="white")
    payButton = ct.CTkButton(parent_frame,text="Pay NRP 5000.00",font=("JetBrainMono",20,"bold"),width=210,height=50,text_color="white")
    payButton.place(x=180,y=840)
    comment.place(x=10, y=150)
    
def checkoutFrame():
    ########## side panel ##################
    checkout_panel = SlidePanel(window, 1.0, 0.7)
    checkout_panel.configure(fg_color="#212121")

    ############# close button for side panel ###############
    closebtn = ct.CTkButton(checkout_panel,text=" X ",width=30,height=30,text_color="white",fg_color="black",hover_color="red",command=lambda: checkout_panel.animate_backwards())
    closebtn.place(x=490,y=30)

    ######### heading/sub-heading of checkout ###############
    order_heading = ct.CTkLabel(checkout_panel,text="Order Review",font=("JetBrainMono",25),text_color="#FFFFFF")
    order_heading.place(x=40,y=50)
    itemsNumber = ct.CTkLabel(checkout_panel,text="3 item in card",font=("JetBrainMono",18),text_color="#FFFFFF")
    itemsNumber.place(x=40,y=80)

    checkout_panel.columnconfigure(0,weight=1)
    row_weights = [1, 1, 1, 1, 3]
    for row, weight in enumerate(row_weights):
        checkout_panel.rowconfigure(row, weight=weight)
        
    ItemsList(checkout_panel)
    discount_label = ct.CTkLabel(checkout_panel,text="Discount Codes",font=("JetBrainMono",24,"bold"),text_color="white")
    discount_label.place(x=40,y=470)
    discount_input = ct.CTkEntry(checkout_panel,placeholder_text="Discount code ....",width=350,height=40,border_width=0)
    discount_input.place(x=40,y=510)
    create_billing_section(checkout_panel,x=10,y=560)
    return checkout_panel 

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
        sarchAndCart_Frame, corner_radius=13, text="Checkout", width=150, height=60, font=("JetBrainMono", 17),
        bg_color="#14162E", fg_color="#499E2C", hover_color="red", command=checkoutFrame().animate)
    AddCart_btn.place(x=50, y=60)


def radiobutton_event(var, total_var, values, prices):
    index = var.get() - 1
    if 0 <= index < len(values):
        total_var.set(f"Total: NPR {prices[index]}")

def apply_product(product_name, var, total_var):
    if var.get() == 0:
        total_var.set("Not Selected !!")
        print("select data")
    else:
        print(f"sent to checkout {total_var.get()}")

def create_product_tab(tab, image,product_name,time, values, prices,x,y,imagex,imagey,size,headx,heady,parax,paray,radiox,raidoy,totalx,totaly,subx,suby):
    product_frame = ct.CTkFrame(tab, width=850, height=378, fg_color="green")
    product_frame.place(x=x, y=y)

    product_image = ct.CTkImage(light_image=Image.open(image), size=size)
    product_label = ct.CTkLabel(product_frame, image=product_image, text="", fg_color="#2C3546", width=360)
    product_label.place(x=imagex, y=imagey)

    heading = ct.CTkLabel(product_frame, text=product_name.upper(), font=("JetBrainMono", 32, 'bold'), text_color="#fff")
    heading.place(x=headx, y=heady)

    label_para = ct.CTkLabel(product_frame, text=time, font=("JetBrainMono", 22),
                          text_color="#fff")
    label_para.place(x=parax, y=paray)

    var = tk.IntVar(value=0)
    total_var = tk.StringVar(value="Total: NPR 0")

    radiobuttons = []
    for i, value in enumerate(values):
        radiobutton = ct.CTkRadioButton(product_frame, variable=var, text=value, value=i + 1, font=("JetBrainMono",18),
                                     command=lambda: radiobutton_event(var, total_var, values, prices))
        radiobutton.place(x=radiox, y=raidoy + i * 50)
        radiobuttons.append(radiobutton)

    total_label = ct.CTkLabel(product_frame, text="", font=("JetBrainMono", 20), textvariable=total_var)
    total_label.place(x=totalx, y=totaly)

    apply_button = ct.CTkButton(product_frame, text="Apply",
                             command=lambda: apply_product(product_name, var, total_var), height=40,
                             font=("JetBrainMono", 19))
    apply_button.place(x=subx, y=suby)


def create_body(parent):
    dashboard_frame = ct.CTkFrame(parent, width=1568, height=911, fg_color=backgrounColor)
    dashboard_frame.place(x=0, y=110)
    
    notebook = ct.CTkTabview(dashboard_frame, width=1510, height=410, fg_color=backgrounColor,segmented_button_fg_color=backgrounColor, text_color="black")
    notebook.place(x=5, y=15)

    tab1 = notebook.add("Gym course and Private trainer")
    tab2 = notebook.add("Swimming Session")
    tab3 = notebook.add("Sunana Session")

    products = [
        (tab1, 
         "./assets/frame0/firstorder.png",
         "GYM COURSE",
         "Select Your Course (Weekly)", 
         ["Beginner ( 2 sessions )", "Intermediate ( 3 sessions )","Elite ( more than 5 sessions )"],
         [1000, 2000, 3000],30,5,-20,-90,(310,500),420,30,360,100,360,150,355,300,530,293),
        
        (tab1,"./assets/frame0/co.png", "Private trainer","Select Hour ( per day)", ["1 hour", "2 hours", "3 hours"], [500, 1000, 1500],740,5,0,0,(300,350),420,30,390,100,390,150,380,300,600,293),
        (tab2,"./assets/frame0/swimming.png","swimming","Select Sessions ( Monthly )", ["4 Sessions", "8 Sessions", "12 Sessions"], [2000, 4000, 6000],300,5,0,0,(430,350),530,30,480,100,490,150,460,300,680,293),
        (tab3,"./assets/frame0/suna.png", "suna","Select Sessions (Monthly)", ["1 Session", "2 Sessions", "3 Sessions", "4 Sessions"], [1500, 3000, 4500, 6000],300,5,0,0,(400,400),520,5,465,50,465,100,460,300,680,293)
    ]

    for tab,image,product_name,time,value,price,x,y,imagex,imagey,size,headx,heady,parax,paray,radiox,radioy,totalx,totaly,subx,suby in products:
        create_product_tab(tab,image,product_name,time,value,price,x,y,imagex,imagey,size,headx,heady,parax,paray,radiox,radioy,totalx,totaly,subx,suby)


def dashboardPage():
    dashbaordframe = ct.CTkFrame(main_frame,width=1568,height=911,fg_color="black")
    dashbaordframe.place(x=0,y=0)
    dashBoard_search(dashbaordframe)
    create_body(dashbaordframe)
    dashBoard_foot(dashbaordframe)
    














    
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
