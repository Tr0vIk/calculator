from tkinter import *

res = ""

#1
def but_1():
    global res
    res = res + "1"
    display["text"] = f"{res}"

def but_2():
    global res
    res = res + "2"
    display["text"] = f"{res}"

def but_3():
    global res
    res = res + "3"
    display["text"] = f"{res}"
    
def but_4():
    global res
    res = res + "4"
    display["text"] = f"{res}"
    
def but_5():
    global res
    res = res + "5"
    display["text"] = f"{res}"
    
def but_6():
    global res
    res = res + "6"
    display["text"] = f"{res}"
    
def but_7():
    global res
    res = res + "7"
    display["text"] = f"{res}"


def but_8():
    global res
    res = res + "8"
    display["text"] = f"{res}"

def but_9():
    global res
    res = res + "9"
    display["text"] = f"{res}"

def but_0():
    global res
    res = res + "0"
    display["text"] = f"{res}"

#2
def but_sum():
    global res
    res = res + "+"
    display["text"] = f"{res}"
    
def but_sub():
    global res
    res = res + "-"
    display["text"] = f"{res}"
    
def but_div():
    global res
    res = res + "/"
    display["text"] = f"{res}"
    
def but_mult():
    global res
    res = res + "*"
    display["text"] = f"{res}"

def but_brac1():
    global res
    res = res + "("
    display["text"] = f"{res}"
    
def but_brac2():
    global res
    res = res + ")"
    display["text"] = f"{res}"

#3 
def but_c():
    global res
    res = res[:-1]
    display["text"] = f"{res}"
    
def but_ce():
    global res
    res = ""
    display["text"] = f"{res}"   

def but_ravn():
    global res
    if "/0" in res:
        display["text"] = "Делить на ноль нельзя"
    try:
        s = eval(f"{res}")
        display["text"] = f"{s}"
        res = str(s)
    except SyntaxError:
        display["text"] = "Ошибка ввода"
        res = ""
    except:
        display["text"] = "Ошибка"
        res = ""
        
# положение и размер кнопок
r1 = 4 # высота
r2 = 6 # ширина
x1 = 15
y1 = 80
rx = 55
ry = 75

#тело для окна
root = Tk()
root.title("Калькулятор")
root.geometry("300x400+750+150")
#root.resizable(False,False)

#экран вывода
display = Label(text=f"{res}",
                font="Calibri 20",
                justify = LEFT)#, background = "#FFFFFF")
display.pack(ipady = 10)

#кнопки мат действий
btn_sum = Button(text="+",height=r1, width=r2, bg = "#FFFFFF", relief= GROOVE,
              activebackground = "DarkOrange", command=but_sum)
btn_sum.place(x = x1+3*rx, y = y1)

btn_sub = Button(text="-",height=r1, width=r2, bg = "#FFFFFF", relief= GROOVE,
              activebackground = "DarkOrange", command=but_sub)
btn_sub.place(x = x1+3*rx, y = y1+ry)

btn_mult = Button(text="*",height=r1, width=r2, bg = "#FFFFFF", relief= GROOVE,
              activebackground = "DarkOrange", command=but_mult)
btn_mult.place(x = x1+4*rx, y = y1)

btn_div = Button(text="/",height=r1, width=r2, bg = "#FFFFFF", relief= GROOVE,
              activebackground = "DarkOrange", command=but_div)
btn_div.place(x = x1+3*rx, y = y1+2*ry)

btn_brac1 = Button(text="(",height=r1, width=r2, bg = "#FFFFFF", relief= GROOVE,
              activebackground = "DarkOrange", command=but_brac1)
btn_brac1.place(x = x1+rx, y = y1+3*ry)

btn_brac2 = Button(text=")",height=r1, width=r2, bg = "#FFFFFF", relief= GROOVE,
              activebackground = "DarkOrange", command=but_brac2)
btn_brac2.place(x = x1+2*rx, y = y1+3*ry)

#кнопки равно, сe, с
btn_ravn = Button(text="=",height=r1, width=r2, bg = "#FFFFFF", relief= GROOVE,
              activebackground = "DarkOrange", command=but_ravn)
btn_ravn.place(x = x1+3*rx, y = y1+3*ry)

btn_ce = Button(text="ce",height=r1, width=r2, bg = "#FFFFFF", relief= GROOVE,
              activebackground = "DarkOrange", command=but_ce)
btn_ce.place(x = x1+4*rx, y = y1+ry)

btn_c = Button(text="<--",height=r1, width=r2, bg = "#FFFFFF", relief= GROOVE,
              activebackground = "DarkOrange", command=but_c)
btn_c.place(x = x1+4*rx, y = y1+2*ry)


#Кнопки для ввода цифр
btn1 = Button(text = "1",height=r1, width=r2, bg = "#FFFFFF", relief= GROOVE,
              activebackground = "DarkOrange", command=but_1)
btn1.place(x = x1, y = y1+2*ry)

btn2 = Button(text = "2",height=r1, width=r2, bg = "#FFFFFF", relief= GROOVE,
              activebackground = "DarkOrange", command=but_2)
btn2.place(x = x1+rx, y = y1+2*ry)

btn3 = Button(text = "3", height=r1, width=r2, bg = "#FFFFFF", relief= GROOVE,
              activebackground = "DarkOrange" , command=but_3)
btn3.place(x = x1+2*rx, y = y1+2*ry)

btn4 = Button(text="4",height=r1, width=r2, bg = "#FFFFFF", relief= GROOVE,
              activebackground = "DarkOrange", command=but_4)
btn4.place(x = x1, y = y1+ry)

btn5 = Button(text="5",height=r1, width=r2, bg = "#FFFFFF", relief= GROOVE,
              activebackground = "DarkOrange", command=but_5)
btn5.place(x = x1+rx, y = y1+ry)

btn6 = Button(text="6",height=r1, width=r2, bg = "#FFFFFF", relief= GROOVE,
              activebackground = "DarkOrange", command=but_6)
btn6.place(x = x1+2*rx, y = y1+ry)

btn7 = Button(text="7",height=r1, width=r2, bg = "#FFFFFF", relief= GROOVE,
              activebackground = "DarkOrange", command=but_7)
btn7.place(x = x1, y = y1)

btn8 = Button(text="8",height=r1, width=r2, bg = "#FFFFFF", relief= GROOVE,
              activebackground = "DarkOrange", command=but_8)
btn8.place(x = x1+rx, y = y1)

btn9 = Button(text="9",height=r1, width=r2, bg = "#FFFFFF", relief= GROOVE,
              activebackground = "DarkOrange", command=but_9)
btn9.place(x = x1+2*rx, y = y1)

btn0 = Button(text="0",height=r1, width=r2, bg = "#FFFFFF", relief= GROOVE,
              activebackground = "DarkOrange", command=but_0)
btn0.place(x = x1, y = y1+3*ry)

root.mainloop()