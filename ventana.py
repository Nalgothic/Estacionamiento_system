import tkinter
from tkinter import messagebox
from tkinter import *
import datetime
import calendar

class Ventana_Principal(Frame):
    def __init__(self,ppal):
        super().__init__()
        self.ppal=ppal
        
        self.configuro_ventana()
        self.bienvenida()
        self.menu_principal()
        
        self.patente=StringVar()
        self.cochera=StringVar()
        self.hora=StringVar()
        self.fecha=StringVar()
        
        
        
    def bienvenida(self):
        if self.configuro_ventana:
            messagebox.showinfo('Hola!', 'Bienvenido!')
        else:
            pass
        
        
        
        
    def configuro_ventana(self):
        self.ppal.geometry('600x600')
        self.ppal.title('Estacionamiento')
        self.ppal.config(bg='Blue')
        
        
    def menu_principal(self):
        self.menu_bar=Menu()
        self.menu_ppal=Menu(self.menu_bar, tearoff=0)
        
        self.menu_bar.add_cascade(label='Ingresos', menu=self.menu_ppal)
        self.menu_ppal.add_command(label='Nuevo Ingreso')
        self.menu_ppal.add_command(label='Listar Ingresados')
        
        self.menu_eg=Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label='Egresos', menu=self.menu_eg)
        self.menu_eg.add_command(label='Nuevo Egreso')
        self.menu_eg.add_command(label='Listar Egresos')
        
        self.menu_tar=Menu(self.menu_bar, tearoff=0)        
        self.menu_bar.add_cascade(label='Tarifas', menu=self.menu_tar) 
        self.menu_tar.add_command(label='Ajuste Tarifario')
        self.menu_tar.add_command(label='Control de tarifas')
        
        self.menu_cont=Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label='Contabilidad', menu=self.menu_cont)
        self.menu_cont.add_command(label='Cobros efectivo')
        self.menu_cont.add_command(label='Cobros electronicos')
        self.menu_cont.add_command(label='Cobros Posnet')
        self.menu_cont.add_command(label='Cierre Diario')
        
        self.ppal.config(menu=self.menu_bar)
        
    def nuevo_ingreso(self):
        self.ven_in=Toplevel()
        self.ven_in.geometry('400x400')
        self.ven_in.config(bg='Blue')
        self.ven_in.title('Nuevo Ingreso')
        self.label1=Label(self.ven_in,text='Patente' ).place(x=5, y=50)
        self.text_patente=Entry(self.ven_in, textvariable=self.patente, font=16).place(x=60, y=50)
        self.label2=Label(self.ven_in, text='Hora').place(x=5,y=80 )
        self.text_hora=Entry(self.ven_in, textvariable=self.hora, font=16).place(x=60, y=80) 
           
        
    