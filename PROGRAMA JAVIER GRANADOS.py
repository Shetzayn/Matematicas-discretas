from doctest import master
from tkinter import *
from cProfile import label
from cgitb import text
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from turtle import heading
import itertools

ventanaI = Tk(className="Ventanaaaa")

ventanaI.configure(background='black')

ventanaI.geometry("800x600")

Texto = Label(ventanaI, text="PROGRAMA JAVIER GRANADOS")

Texto.config(font=("Calibri",24))

l = Text(ventanaI,height=100,width=100)

T2 = """"""



def ventanaP():

    ventanaP = tk.Toplevel()

    ventanaI.destroy()

    ventanaP = Tk(className="Ventana primos")

    ventanaP.configure(background='red')

    ventanaP.geometry("400x400")

    Texto = Label(ventanaP, text="Ventana de Primos")

    Texto.config(font=("Calibri",16))

    

    l = Text(ventanaP,height=2,width=35)

    T2 = """Programa para hallar números primos"""


    def primo(n): 

        if n<2:

            return False 

    
        for i in range(2,n): 

            if n % i == 0:

             return False 

        return True


   
    def cadena_primos():

        n1 = int(r.get())

        n2 = int(r2.get())

        counter=0

        lista=[]

        for k in range(n1,n2):

            if primo(k) == True:

                counter+=1

                lista.append(k)

        messagebox.showinfo(lista," " ,"PRIMOS:",counter)


    r = ttk.Entry()

    r.place(x=60,y=80,width=30,height=30)

    r2 = ttk.Entry()

    r2.place(x=110,y=80,width=30,height=30)


    boton = ttk.Button(text="Mostrar primos:",command=cadena_primos)

    boton.place(x=200,y=80)

    Texto.pack()

    l.pack()

    l.insert(tk.END, T2)


def ventanaB():

    ventanaB = tk.Toplevel()

    ventanaI.destroy()

    ventanaB = Tk(className="Ventana Bases")

    ventanaB.configure(background='red')

    ventanaB.geometry("400x400")

    Texto = Label(ventanaB, text="Ventana de Bases")

    Texto.config(font=("Calibri",16))

    Texto2= Label(ventanaB, text="Ingrese un número y después la base a convertir.",bg=None)

    Texto2.place(x= 50, y= 130)

    
    

    def B10_a_Bx():

        num = int(r.get())

        x = int(r2.get())

        Basex = "" 

        while num > 0: 

            residuo = num % x 

            Basex = str(residuo) + Basex 

            num = int(num / x)

        messagebox.showinfo(message=Basex)

        return Basex

    r = ttk.Entry()

    r.place(x=60,y=80,width=30,height=30)

    r2 = ttk.Entry()

    r2.place(x=110,y=80,width=30,height=30)


    boton = ttk.Button(text="Convertir a base elegida:",command=B10_a_Bx)

    boton.place(x=200,y=80)


    Texto.pack()

    l.pack()

    l.insert(tk.END, T2)



def ventanaF():

    ventanaF = tk.Toplevel()

    ventanaI.destroy()

    ventanaF = Tk(className="Ventana Fibonacci")

    ventanaF.configure(background='red')

    ventanaF.geometry("400x400")

    Texto = Label(ventanaF, text="Ventana de Fibonacci")

    Texto.config(font=("Courier",16))

    Texto2= Label(ventanaF, text="Ingrese el número inicial y el final.",bg=None)

    Texto2.place(x= 50, y= 130)

    

    def fibonacci():

        lista = []

        num = int(r.get())

        num2 = int(r2.get())

        a,b=0,1

        while a < num2:
            
            a,b=b,a+b

            if a>=num:

                lista.append(a)

        messagebox.showinfo(message=lista)


    r = ttk.Entry()

    r.place(x=60,y=80,width=30,height=30)

    r2 = ttk.Entry()

    r2.place(x=110,y=80,width=30,height=30)


    boton = ttk.Button(text="Secuencia Fibonacci:",command=fibonacci)

    boton.place(x=200,y=80)


    Texto.pack()

    l.pack()

    l.insert(tk.END, T2)



def VentanaC():

    VentanaC = tk.Toplevel()

    ventanaI.destroy()

    VentanaC = Tk(className="Combinaciones")

    VentanaC.configure(background='red')


    VentanaC.geometry("400x400")

    Texto = Label(VentanaC, text="Ventana Combinaciones")

    Texto.config(font=("Calibri",16))

   
    Comblist = []
    

    def combi():

        combinacion_numero = int(r.get())


        Comblist.append(combinacion_numero)


    def CombResult():

        numlist = int(r2.get())

        resultado = list(itertools.combinations(Comblist, numlist))

        messagebox.showinfo(message = resultado)

    
    r = ttk.Entry()

    r.place(x=60,y=80,width=30,height=30)


    r2= ttk.Entry()

    r2.place(x=60,y=120,width=30,height=30)


    
    
    Addbtn = ttk.Button(text="añadir numero a lista",command=combi)

    Addbtn.place(x=200, y =80)

    Resultbtn = ttk.Button(text="Hacer combinación",command=CombResult)

    Resultbtn.place(x=200, y =120)
        
    Texto.pack()

    l.pack()

    l.insert(tk.END, T2)



    
    Texto.pack()
    
       
    
    
botonP = ttk.Button(text="¿Es primo?",command=ventanaP)

botonB = ttk.Button(text="Base 10-x",command=ventanaB)

botonF = ttk.Button(text="Fibonacci",command=ventanaF)

botonC= ttk.Button(text="Combinaciones",command=VentanaC)

botonP.place(x=150, y =130)

botonB.place(x=250, y =130)

botonF.place(x=350, y =130)

botonC.place(x=30, y =130)


Texto.pack()

l.pack()

l.insert(tk.END, T2)



ventanaI.mainloop()