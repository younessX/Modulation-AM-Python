"""
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
"""
from tkinter import  *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
import math as m

def my():
    global text_modulant, text_porteuse, text_modulé,M
    a = entry_modulant.get()
    b = entry_porteuse.get()
    M = float(spinbox_m.get())
    text_modulant = a.replace('sin', 'm.sin')
    text_modulant = text_modulant.replace('cos', 'm.cos')
    text_modulant = text_modulant.replace('pi', 'm.pi')

    text_porteuse = b.replace('sin', 'm.sin')
    text_porteuse = text_porteuse.replace('cos', 'm.cos')
    text_porteuse = text_porteuse.replace('pi', 'm.pi')

    text_modulé = text_porteuse + " * " + "(1 + "+ str(M) + " * " + text_modulant + ")"

    debut = int(spin_debut.get())
    fin   = int(spin_fin.get())
    Val   = int(spin_Val.get())
    update_draw(canvas_1, figure_1, Porteuse, debut, fin, Val*10)

    update_draw(canvas_2, figure_2, Modulant,  debut, fin, Val)

    update_draw(canvas_3, figure_3, modulé,  debut, fin, Val)

    frequantiel()


def Modulant(x):
    return eval(text_modulant)

def Porteuse(x):
    return eval(text_porteuse)

def modulé(x):
      return eval(text_modulé)


def frequantiel():
    figure_4.clear()
    fp = int(spin_fp.get())
    fm = int(spin_fm.get())
    Am = int(spin_A.get())
    x1 = [fp-fm, fp-fm]
    y1 = [0, M*Am/2]

    x2 = [fp, fp]
    y2 = [0, Am]

    x3 = [fp+fm, fp+fm]
    y3 = [0, M*Am/2]
    figure_4.add_subplot(111).plot(x1, y1, x2, y2, x3, y3)
    canvas_4.draw_idle()

def update_draw(canvas, my_figure, func, debut, fin, Val):
    my_figure.clear()
    x = np.linspace(debut, fin, Val)
    y = [func(i) for i in x]
    my_figure.add_subplot(111).plot(x, y)
    canvas.draw_idle()

window = Tk()
window.title("Graphe")
window.geometry("800x600")

label = Label(window, text="Modulation Am", font="bold 20",bg="orange")
label.place(x=120, y=10)

label_modulant = Label(window, text="Modulant", font="bold 15")
label_modulant.place(x=10, y=70)

entry_modulant = Entry(window, width=28, font="bold 14")
entry_modulant.place(x=100, y=70)

label_porteuse = Label(window, text="Porteuse", font="bold 15")
label_porteuse.place(x=10, y=115)

entry_porteuse = Entry(window, width=28, font="bold 14")
entry_porteuse.place(x=100, y=115)

label_m = Label(window, text="Taux (m)", font="bold 14")
label_m.place(x=10, y=160)

spinbox_m =Spinbox(window, from_=0, to=100, font="bold 14")
spinbox_m.place(x=100,y=160)

#ligne 1
label_debut = Label(window, text="début", width=8, bg="orange", font="bold= 18")
label_debut.place(x=3, y=220)

label_fin = Label(window, text="fin", width=8, bg="orange", font="bold= 18")
label_fin.place(x=150, y=220)

label_Val = Label(window, text="Val", width=8, bg="orange", font="bold= 18")
label_Val.place(x=300, y=220)

spin_debut = Spinbox(window, from_=-1000, to=1000, increment=1, width=9, font="bold 14")
spin_debut.place(x=3, y=265)

spin_fin = Spinbox(window, from_=0, to=1000, increment=1, width=9, font="bold 14")
spin_fin.place(x=150, y=265)

spin_Val = Spinbox(window, from_=0, to=200000, increment=1, width=9, font="bold 14")
spin_Val.place(x=300, y=265)

#ligne 2
label_A = Label(window, text="Am", width=8, bg="orange", font="bold= 18")
label_A.place(x=3, y=335)

label_fp = Label(window, text="Fp", width=8, bg="orange", font="bold= 18")
label_fp.place(x=150, y=335)

label_fm = Label(window, text="Fm", width=8, bg="orange", font="bold= 18")
label_fm.place(x=300, y=335)

spin_A = Spinbox(window, from_=0, to=1000, increment=1, width=9, font="bold 14")
spin_A.place(x=3, y=380)

spin_fp = Spinbox(window, from_=0, to=200000, increment=1, width=9, font="bold 14")
spin_fp.place(x=150, y=380)

spin_fm = Spinbox(window, from_=0, to=1000, increment=1, width=9, font="bold 14")
spin_fm.place(x=300, y=380)

button = Button(master=window, text="Tracer", command = my, width="10", font="bold 20", bg="white")
button.place(x=140, y= 500)

#figure 1
figure_1 = Figure(figsize=(4, 3), dpi=100)
canvas_1 = FigureCanvasTkAgg(figure_1, master=window)
#toolbar = NavigationToolbar2Tk(canvas, window)
canvas_1.get_tk_widget().place(x=865, y=10)

#figure 2
figure_2 = Figure(figsize=(4, 3), dpi=100)
canvas_2 = FigureCanvasTkAgg(figure_2, master=window)
#toolbar = NavigationToolbar2Tk(canvas, window)
canvas_2.get_tk_widget().place(x=450, y=10)

#figure 3
figure_3 = Figure(figsize=(4, 3), dpi=100)
canvas_3 = FigureCanvasTkAgg(figure_3, master=window)
#toolbar = NavigationToolbar2Tk(canvas, window)
canvas_3.get_tk_widget().place(x=450, y=330)

#figure 4
figure_4 = Figure(figsize=(4, 3), dpi=100)
canvas_4 = FigureCanvasTkAgg(figure_4, master=window)
#toolbar = NavigationToolbar2Tk(canvas, window)
canvas_4.get_tk_widget().place(x=865, y=330)

#labels
Label(window, text="Modulant", font="bold 15").place(x=610, y=10)
Label(window, text="Porteuse", font="bold 15").place(x=1020, y=10)
Label(window, text="Modulé", font="bold 15").place(x=610, y=330)
Label(window, text="Spectre",font="bold 15").place(x=1020, y=330)
window.mainloop()

