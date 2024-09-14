# === [ MainFile ] === #

from tkinter import *
from tkinter import messagebox
# ==================== #
root = Tk() # ایجاد یک پنجره
root.title("Calculater") # نامگذاری پنجره
root.geometry("500x600") # تعین سایز پنجره
root.resizable(0,0) # غیرفعالسازی دکمه تغیر سایز
root.config( # پیکربندی پنجره 
    bg="gray" , # تعین رنگ پس زمینه
)
# ==================== #



# === [ Display ] === #
def get_display() :
    text = display.cget("text") # گرفتن مقداری که در صفحه نمایش وجود دارد 
    return text
# ================= #

def clear_display() : # پاکسازی مقادیر صفحه نمایش
    display.config(text="")
    display.update()
# ================= #
def update_display(n) :
    displayText = display.cget("text")
    displayText = displayText+n
    display.config(text=displayText)



# =============== #

def eq() :
    displayText = display.cget("text")
    if len(list(displayText)) != 0 :
        result = eval(displayText) # محاسبه مقدار وارد شده در صفحه نمایش
        display.config(text=result)
    else :
        messagebox.showerror("Error","مقداری برای محاسبه وجود ندارد")


def remove_last_char() :
    displayText = display.cget("text") # گرفتن مقدار صفحه نمایش
    displayText = list(displayText)
    if len(displayText) != 0 :
        displayText.pop() # حذف اخرین مقدار 
        display.config(text="".join(displayText))  # تنظیم صفحه نمایش بروز شده
    else :
        messagebox.showerror("Error","مقداری برای حذف وجود ندارد")
# ============================= #
display = Label(  # ایجاد یک صفحه نمایش 
    root ,
    text="" ,
    bg="white" ,
    font=("Arial",40) ,
    state="disabled"
)
display.place(height=100,width=500,y=2)
# ============== #
# === [ Buttons ] === #
# percent key: کلید های ردیف اول 
button = Button( # دکمه %
    root ,
    text = "%" ,
    font = ("Arial",20) ,
    command = lambda n="%": update_display(n)
)
button.place(
    height = 100 ,
    width = 120 ,
    x = 0 ,
    y = 110
)
# =============== #
button = Button( # دکمه C
    root,
    text = "C" ,
    font = ("Arial",20) ,
    command = clear_display
)
button.place(
    height = 100 ,
    width = 120 ,
    x = 125 ,
    y = 110
)
# =============== #
button = Button( # دکمه حذف
    root,
    text = "Del" ,
    font = ("Arial",20) ,
    command = remove_last_char
)
button.place(
    height = 100 ,
    width = 120 ,
    x = 250 ,
    y = 110
)
# =============== #
button = Button( # دکمه تنظیم
    root,
    text = "/" ,
    font = ("Arial",20) ,
    command = lambda n="/": update_display(n)
)
button.place(
    height = 100 ,
    width = 120 ,
    x = 375 ,
    y = 110
)
# =============== #
button = Button( # دکمه شماره 7
    root ,
    text = "7" ,
    font = ("Arial",20) ,
    command = lambda n="7": update_display(n)
)
button.place(
    height = 100 ,
    width = 120 ,
    x = 0 ,
    y = 210
)
# =============== #
button = Button( # دکمه شماره 8
    root,
    text = "8" ,
    font = ("Arial",20) ,
    command = lambda n="8": update_display(n)
)
button.place(
    height = 100 ,
    width = 120 ,
    x = 125 ,
    y = 210
)
# =============== #
button = Button( # دکمه شماره 9
    root,
    text = "9" ,
    font = ("Arial",20) ,
    command = lambda n="9": update_display(n)
)
button.place(
    height = 100 ,
    width = 120 ,
    x = 250 ,
    y = 210
)
# =============== #
button = Button( # دکمه ضرب 
    root,
    text = "X" ,
    font = ("Arial",20) ,
    command = lambda n="*": update_display(n)
)
button.place(
    height = 100 ,
    width = 120 ,
    x = 375 ,
    y = 210
)
# =============== #
button = Button( # دکمه شماره 4
    root ,
    text = "4" ,
    font = ("Arial",20) ,
    command = lambda n="4": update_display(n)
)
button.place(
    height = 100 ,
    width = 120 ,
    x = 0 ,
    y = 310
)
# =============== #
button = Button(  # دکمه شماره 5
    root,
    text = "5" ,
    font = ("Arial",20) ,
    command = lambda n="5": update_display(n)
)
button.place(
    height = 100 ,
    width = 120 ,
    x = 125 ,
    y = 310
)
# =============== #
button = Button( # دکمه شماره 6
    root,
    text = "6" ,
    font = ("Arial",20) ,
    command = lambda n="6": update_display(n)
)
button.place(
    height = 100 ,
    width = 120 ,
    x = 250 ,
    y = 310
)
# =============== #
button = Button( # دکمه منفی
    root,
    text = "-" ,
    font = ("Arial",20) ,
    command = lambda n="-": update_display(n)
)
button.place(
    height = 100 ,
    width = 120 ,
    x = 375 ,
    y = 310
)
# =============== #
button = Button(  # دکمه شماره 1
    root ,
    text = "1" ,
    font = ("Arial",20) ,
    command = lambda n="1": update_display(n)
)
button.place(
    height = 100 ,
    width = 120 ,
    x = 0 ,
    y = 410
)
# =============== #
button = Button(  # دکمه شماره 2
    root,
    text = "2" ,
    font = ("Arial",20) ,
    command = lambda n="2": update_display(n)
)
button.place(
    height = 100 ,
    width = 120 ,
    x = 125 ,
    y = 410
)
# =============== #
button = Button( # دکمه شماره 3
    root,
    text = "3" ,
    font = ("Arial",20) ,
    command = lambda n="3": update_display(n)
)
button.place(
    height = 100 ,
    width = 120 ,
    x = 250 ,
    y = 410
)
# =============== #
button = Button(# دکمه مجموع
    root,
    text = "+" ,
    font = ("Arial",20) ,
    command = lambda n="+": update_display(n)
)
button.place(
    height = 100 ,
    width = 120 ,
    x = 375 ,
    y = 410
)
# =============== #
button = Button(  # دکمه شماره  0
    root,
    text = "0" ,
    font = ("Arial",20) ,
    command = lambda n="0": update_display(n)
)
button.place(
    height = 100 ,
    width = 245 ,
    x = 0 ,
    y = 510
)
# =============== #
button = Button( # دکمه ممیز
    root,
    text = "." ,
    font = ("Arial",20) ,
    command = lambda n=".": update_display(n)
)
button.place(
    height = 100 ,
    width = 120 ,
    x = 250 ,
    y = 510
)
# =============== #
button = Button( # دکمه عملگر مساوی
    root,
    text = "=" ,
    font = ("Arial",20) ,
    command=eq
)
button.place(
    height = 100 ,
    width = 120 ,
    x = 375 ,
    y = 510
)
# =============== #
root.mainloop() # ران کردن پنحره 