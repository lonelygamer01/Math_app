from tkinter import *
from tkinter.font import BOLD
import webbrowser
import math

height = 600
width = 800

root1 = Tk()
root1.resizable(0,0)
root1.title("Math program to calculate faster or not. Idk...")

root_canvas = Canvas(root1, height=height, width=width, background="steelblue")
root_canvas.pack()

label1 = Label(root_canvas, bg="darkblue", fg="black", text="Let's do some Meth!" )
label1.place(relwidth=1, relheight=0.15)
label1.config(font=("Arial", 25, BOLD))

label2 = Label(root_canvas, fg="black", bg="steelblue", text="Under development... \nWanna updates?")
label2.place(height=50, width=222, relx=0.6, rely=0.9)
label2.config(font=("Arial", 13))



url = "https://www.instagram.com/ez_egy_masik_account/?hl=hu"
def openlink():
    webbrowser.open(url,1)

contact_me = Button(root_canvas, fg="black", bg="white", text="Contact \nhere!", command = openlink)
contact_me.place(height=55, width=100, relx=0.85, rely=0.89)
contact_me.config(font=("Arial", 12, BOLD))           

def masodfoku():
    

    root_masodfoku = Tk()
    root_masodfoku.resizable(0,0)
    root_masodfoku.title("Math program to calculate faster or not. Idk...")


    masodfoku_canvas = Canvas(root_masodfoku, height=height, width=width, background="steelblue")
    masodfoku_canvas.pack()

    label3 = Label(masodfoku_canvas, bg="darkblue", fg="black", text="Let's do some Meth!" )
    label3.place(relwidth=1, relheight=0.15)
    label3.config(font=("Arial", 25, BOLD))

    label4 = Label(masodfoku_canvas, bg="steelblue", fg="black", text="Másodfokú egyenlet megoldóprogram \nAx2 + Bx + C = 0" )
    label4.place(width=400, height=100, relx=0.25 , rely= 0.2)
    label4.config(font=("Arial", 14, BOLD))

    labelA = Label(masodfoku_canvas, bg="steelblue", fg="black", text="A: " )
    labelA.place(width=50, height=30, relx=0.15 , rely= 0.4)
    labelA.config(font=("Arial", 12, BOLD))

    labelB = Label(masodfoku_canvas, bg="steelblue", fg="black", text="B: " )
    labelB.place(width=50, height=30, relx=0.15 , rely= 0.45)
    labelB.config(font=("Arial", 12, BOLD))

    labelC = Label(masodfoku_canvas, bg="steelblue", fg="black", text="C: " )
    labelC.place(width=50, height=30, relx=0.15 , rely= 0.5)
    labelC.config(font=("Arial", 12, BOLD))


    entryA = Entry(masodfoku_canvas)
    entryA.place(width=80, height=30, relx=0.3 , rely= 0.4)
    entryA.config(font=("Arial", 12, BOLD))

    entryB = Entry(masodfoku_canvas)
    entryB.place(width=80, height=30, relx=0.3 , rely= 0.45)
    entryB.config(font=("Arial", 12, BOLD))


    entryC = Entry(masodfoku_canvas)
    entryC.place(width=80, height=30, relx=0.3 , rely= 0.5)
    entryC.config(font=("Arial", 12, BOLD))

    megjegyzes1 = Label(masodfoku_canvas, bg="steelblue", fg="black", text="(Ha a program nem csinál semmit \nvalószínűleg nem oldható meg az egyelnlet...)" )
    megjegyzes1.place(width=400, height=60, relx=0.15 , rely= 0.8)
    megjegyzes1.config(font=("Arial", 12, BOLD))
    


    def boom():

        A = float(entryA.get())
        B = float(entryB.get())
        C = float(entryC.get())

        delta  = B*B-4*A*C
        negyzetgyok = math.sqrt(delta)

        x_1 = (-B + negyzetgyok) / (2*A)
        x_2 = (-B - negyzetgyok) / (2*A)

        a = round(x_1,3)
        b = round(x_2,3)


        if delta > 0:
            X1_result = Label(masodfoku_canvas, bg="white", fg="black", text = a)
            X1_result.place(width=100, height=30, relx=0.45 , rely= 0.43)
            X1_result.config(font=("Arial", 12, BOLD))


            X2_result = Label(masodfoku_canvas, bg="white", fg="black", text = b)
            X2_result.place(width=100, height=30, relx=0.45 , rely= 0.48)
            X2_result.config(font=("Arial", 12, BOLD))

        elif delta <= 0:

            negativ = Label(masodfoku_canvas, bg="white", fg="black", text = "Negatív a gyök alatt tesó!")   
            negativ.place(width=150, height=30, relx=0.45 , rely= 0.45)
            negativ.config(font=("Arial",  12, BOLD))

        #elif negyzetgyok == ValueError:

            #error = Label(masodfoku_canvas, bg="white", fg="black", text = "Az egyenlet nem oldható meg, bocsesz!")   
            #error.place(width=150, height=30, relx=0.45 , rely= 0.45)
            #error.config(font=("Arial",  12, BOLD))    



    boom_button = Button(masodfoku_canvas, bg="Grey", fg="black", text="BOOM! ", command=boom )
    boom_button.place(width=100, height=30, relx=0.287 , rely= 0.6)
    boom_button.config(font=("Arial", 12, BOLD))

    fooldal_gomb = Button(masodfoku_canvas, bg="Grey", fg="black", text="Főoldal", command=root_masodfoku.destroy)
    fooldal_gomb.place(width=120, height=40, relx=0.03 , rely= 0.18)
    fooldal_gomb.config(font=("Arial", 14, BOLD))



masodf = Button(root_canvas, fg="black", bg="white", text="Másodfokú egyenlet megoldó", command=masodfoku)
masodf.place(height=50, width=200, relx=0.04, rely=0.2)
masodf.config(font=("Arial", 10, BOLD))

def heron():

    root_heron = Tk()
    root_heron.resizable(0,0)
    root_heron.title("Math program to calculate faster or not. Idk...")

    heron_canvas = Canvas(root_heron, height=height, width=width, background="steelblue")
    heron_canvas.pack()

    label3 = Label(heron_canvas, bg="darkblue", fg="black", text="Let's do some Meth!" )
    label3.place(relwidth=1, relheight=0.15)
    label3.config(font=("Arial", 25, BOLD))

    label4 = Label(heron_canvas, bg="steelblue", fg="black", text="Heron képlet használata \nháromszög esetén." )
    label4.place(width=250, height=100, relx=0.1 , rely= 0.25)
    label4.config(font=("Arial", 14, BOLD))

    label5 = Label(heron_canvas, bg="steelblue", fg="black", text="Heron képlet használata \nhúrnégyszög esetén." )
    label5.place(width=250, height=100, relx=0.55 , rely= 0.25)
    label5.config(font=("Arial", 14, BOLD))

    labela = Label(heron_canvas, bg="steelblue", fg="black", text="a: " )
    labela.place(width=50, height=30, relx=0.05 , rely= 0.4)
    labela.config(font=("Arial", 12, BOLD))


    labelb = Label(heron_canvas, bg="steelblue", fg="black", text="b: " )
    labelb.place(width=50, height=30, relx=0.05 , rely= 0.48)
    labelb.config(font=("Arial", 12, BOLD))


    labelc = Label(heron_canvas, bg="steelblue", fg="black", text="c: " )
    labelc.place(width=50, height=30, relx=0.05 , rely= 0.56)
    labelc.config(font=("Arial", 12, BOLD))

    entry_a = Entry(heron_canvas)
    entry_a.place(width=100, height=30, relx=0.15 , rely= 0.4)
    entry_a.config(font=("Arial", 12, BOLD))

    entry_b = Entry(heron_canvas)
    entry_b.place(width=100, height=30, relx=0.15 , rely= 0.48)
    entry_b.config(font=("Arial", 12, BOLD))

    entry_c = Entry(heron_canvas)
    entry_c.place(width=100, height=30, relx=0.15 , rely= 0.56)
    entry_c.config(font=("Arial", 12, BOLD))

    def boom1():

        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())


        s = (a + b + c) / 2

        T = math.sqrt(s * (s - a) * (s - b) * (s - c))

        T_result = Label(heron_canvas, bg="white", fg="black", text=round(T,3))
        T_result.place(width=100, height=30, relx=0.15 , rely= 0.9)
        T_result.config(font=("Arial", 12, BOLD))




    boom_button1 = Button(heron_canvas, bg="Grey", fg="black", text="BOOM! ", command=boom1 )
    boom_button1.place(width=100, height=30, relx=0.15 , rely= 0.8)
    boom_button1.config(font=("Arial", 12, BOLD))

    result1 = Label(heron_canvas, bg="steelblue", fg="black", text="T: " )
    result1.place(width=50, height=30, relx=0.05 , rely= 0.9)
    result1.config(font=("Arial", 12, BOLD))







    labela2 = Label(heron_canvas, bg="steelblue", fg="black", text="a: " )
    labela2.place(width=50, height=30, relx=0.5 , rely= 0.4)
    labela2.config(font=("Arial", 12, BOLD))

    labelb2 = Label(heron_canvas, bg="steelblue", fg="black", text="b: " )
    labelb2.place(width=50, height=30, relx=0.5 , rely= 0.48)
    labelb2.config(font=("Arial", 12, BOLD))

    labelc2 = Label(heron_canvas, bg="steelblue", fg="black", text="c: " )
    labelc2.place(width=50, height=30, relx=0.5 , rely= 0.56)
    labelc2.config(font=("Arial", 12, BOLD))

    labeld2 = Label(heron_canvas, bg="steelblue", fg="black", text="d: " )
    labeld2.place(width=50, height=30, relx=0.5 , rely= 0.64)
    labeld2.config(font=("Arial", 12, BOLD))

    entry_a2 = Entry(heron_canvas)
    entry_a2.place(width=100, height=30, relx=0.6 , rely= 0.4)
    entry_a2.config(font=("Arial", 12, BOLD))

    entry_b2 = Entry(heron_canvas)
    entry_b2.place(width=100, height=30, relx=0.6 , rely= 0.48)
    entry_b2.config(font=("Arial", 12, BOLD))

    entry_c2 = Entry(heron_canvas)
    entry_c2.place(width=100, height=30, relx=0.6 , rely= 0.56)
    entry_c2.config(font=("Arial", 12, BOLD))

    entry_d2 = Entry(heron_canvas)
    entry_d2.place(width=100, height=30, relx=0.6 , rely= 0.64)
    entry_d2.config(font=("Arial", 12, BOLD))

    def boom2():
        a = float(entry_a2.get())
        b = float(entry_b2.get())
        c = float(entry_c2.get())
        d = float(entry_d2.get())

        s = (a + b + c + d) / 2

        T = math.sqrt((s - a) * (s - b) * (s - c) * (s - d))

        T_result = Label(heron_canvas, bg="white", fg="black", text=round(T,3))
        T_result.place(width=100, height=30, relx=0.6 , rely= 0.9)
        T_result.config(font=("Arial", 12, BOLD))


    boom_button2 = Button(heron_canvas, bg="Grey", fg="black", text="BOOM! ", command=boom2 )
    boom_button2.place(width=100, height=30, relx=0.6 , rely= 0.8)
    boom_button2.config(font=("Arial", 12, BOLD))

    result2 = Label(heron_canvas, bg="steelblue", fg="black", text="T: " )
    result2.place(width=50, height=30, relx=0.5 , rely= 0.9)
    result2.config(font=("Arial", 12, BOLD))

    fooldal_gomb = Button(heron_canvas, bg="Grey", fg="black", text="Főoldal", command=root_heron.destroy)
    fooldal_gomb.place(width=120, height=40, relx=0.03 , rely= 0.18)
    fooldal_gomb.config(font=("Arial", 14, BOLD))






heron_keplet = Button(root_canvas, fg="black", bg="white", text="Heron képlet megoldó", command=heron)
heron_keplet.place(height=50, width=200, relx=0.04, rely=0.3)
heron_keplet.config(font=("Arial", 10, BOLD))


#--------------------------------------------------------------------------------------
szamtani = Button(root_canvas, fg="black", bg="white", text="Számtani sorozat megoldó")
szamtani.place(height=50, width=200, relx=0.35, rely=0.2)
szamtani.config(font=("Arial", 10, BOLD))

mertani = Button(root_canvas, fg="black", bg="white", text="Mértani sorozat megoldó")
mertani.place(height=50, width=200, relx=0.66, rely=0.2)
mertani.config(font=("Arial", 10, BOLD))
#--------------------------------------------------------------------------------------




heron = Button(root1, fg="black", bg="white", text="Heron képlet megoldó")
heron.place(height=50, width=200, relx=0.04, rely=0.4)
heron.config(font=("Arial", 10, BOLD))

heron = Button(root1, fg="black", bg="white", text="Heron képlet megoldó")
heron.place(height=50, width=200, relx=0.04, rely=0.5)
heron.config(font=("Arial", 10, BOLD))

heron = Button(root1, fg="black", bg="white", text="Heron képlet megoldó")
heron.place(height=50, width=200, relx=0.04, rely=0.6)
heron.config(font=("Arial", 10, BOLD))

heron = Button(root1, fg="black", bg="white", text="Heron képlet megoldó")
heron.place(height=50, width=200, relx=0.04, rely=0.7)
heron.config(font=("Arial", 10, BOLD))

#---------------------------------------------------------------------------------------
szamtani = Button(root1, fg="black", bg="white", text="Számtani sorozat megoldó")
szamtani.place(height=50, width=200, relx=0.35, rely=0.3)
szamtani.config(font=("Arial", 10, BOLD))

szamtani = Button(root1, fg="black", bg="white", text="Számtani sorozat megoldó")
szamtani.place(height=50, width=200, relx=0.35, rely=0.4)
szamtani.config(font=("Arial", 10, BOLD))

szamtani = Button(root1, fg="black", bg="white", text="Számtani sorozat megoldó")
szamtani.place(height=50, width=200, relx=0.35, rely=0.5)
szamtani.config(font=("Arial", 10, BOLD))

szamtani = Button(root1, fg="black", bg="white", text="Számtani sorozat megoldó")
szamtani.place(height=50, width=200, relx=0.35, rely=0.6)
szamtani.config(font=("Arial", 10, BOLD))

szamtani = Button(root1, fg="black", bg="white", text="Számtani sorozat megoldó")
szamtani.place(height=50, width=200, relx=0.35, rely=0.7)
szamtani.config(font=("Arial", 10, BOLD))

#--------------------------------------------------------------------------------------
mertani = Button(root1, fg="black", bg="white", text="Mértani sorozat megoldó")
mertani.place(height=50, width=200, relx=0.66, rely=0.3)
mertani.config(font=("Arial", 10, BOLD))

mertani = Button(root1, fg="black", bg="white", text="Mértani sorozat megoldó")
mertani.place(height=50, width=200, relx=0.66, rely=0.4)
mertani.config(font=("Arial", 10, BOLD))

mertani = Button(root1, fg="black", bg="white", text="Mértani sorozat megoldó")
mertani.place(height=50, width=200, relx=0.66, rely=0.5)
mertani.config(font=("Arial", 10, BOLD))

mertani = Button(root1, fg="black", bg="white", text="Mértani sorozat megoldó")
mertani.place(height=50, width=200, relx=0.66, rely=0.6)
mertani.config(font=("Arial", 10, BOLD))

mertani = Button(root1, fg="black", bg="white", text="Mértani sorozat megoldó")
mertani.place(height=50, width=200, relx=0.66, rely=0.7)
mertani.config(font=("Arial", 10, BOLD))
































root1.mainloop()