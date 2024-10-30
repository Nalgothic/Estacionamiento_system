
from tkinter import messagebox
from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk
from datetime import datetime

from modelo import ingreso_vehiculo, egreso_vehiculo
from modelo import listar_ingresos,listar_egresos

class Ventana_Principal(Frame):
    def __init__(self,ppal):
        super().__init__()
        self.ppal=ppal
        
        self.configuro_ventana()
        self.bienvenida()
        self.menu_principal()
        
        self.patente=StringVar()
        self.cochera=StringVar()
        self.hora_actual=StringVar()
        
        self.fecha_hoy=StringVar()
        self.fecha_hoy.set(datetime.now().strftime("%d/%m/%Y")) 
        
        
        
    def bienvenida(self):
        if self.configuro_ventana:
            messagebox.showinfo('Hola!', 'Bienvenido!')
        else:
            pass
        
        
        
        
    def configuro_ventana(self):
        self.ppal.geometry('600x600')
        self.ppal.title('Estacionamiento')
        self.ppal.config(bg='Blue')
        image_path = 'imagen.png'
        
        try:
            self.bg_image = Image.open(image_path)
            self.bg_photo = ImageTk.PhotoImage(self.bg_image)
            self.bg_label = Label(self.ppal,bg='Blue', image=self.bg_photo)
            self.bg_label.place(relwidth=1, relheight=1)
        except Exception as e:
            print(f'Error cargando la imagen: {e}')
            self.ppal.config(bg='Blue')
        
        
        
        
        
    def menu_principal(self):
        self.menu_bar=Menu()
        self.menu_ppal=Menu(self.menu_bar, tearoff=0)
        
        self.menu_bar.add_cascade(label='Ingresos', menu=self.menu_ppal)
        self.menu_ppal.add_command(label='Nuevo Ingreso', command=self.nuevo_ingreso)
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
        self.text_patente=Entry(self.ven_in, textvariable=self.patente, font=16).place(x=100, y=50)
        
        self.label2=Label(self.ven_in, text='Hora').place(x=5,y=80 )
        self.entry_hora = Entry(self.ven_in, textvariable=self.hora_actual, font=16)
        self.entry_hora.config(state='readonly') 
        self.entry_hora.place(x=100, y=80)
        
        self.label_fecha = Label(self.ven_in, text="Fecha de hoy:").place(x=5, y=110)
        self.entry_fecha = Entry(self.ven_in, textvariable=self.fecha_hoy, font=16) 
        self.entry_fecha.config(state='readonly')  
        self.entry_fecha.place(x=100, y=110)
        
        btn_guardar=Button(self.ven_in, text='Guardar', command=self.grabar_ingreso)
        btn_guardar.place(x=100, y=150)
        self.actualizar_hora()
        
                 
            
    def actualizar_hora(self):
        # Actualiza la hora cada segundo
        self.hora_actual.set(datetime.now().strftime("%H:%M:%S"))
        self.ven_in.after(1000, self.actualizar_hora)    
        
    
            
    def grabar_ingreso(self):
        try:
            
            if ingreso_vehiculo(self.entry_fecha.get(), self.patente.get(), self.hora.get()):
                messagebox.showinfo("Grabar Ingreso", "El ingreso se ha grabado correctamente")
                self.ven_in.destroy()
            
            else:
                messagebox.showerror("Grabar Ingreso", "No se pudo guardar el ingreso...")
        except Exception as e:
            print(e)
    
    
            
            
    def listar_ingresos(self):
        self.ven_lista = Toplevel(self.ppal)
        self.ven_lista(bg='#89F08C')
        self.ven_lista.grab_set()
        self.ven_lista.resizable(0, 0)
        self.ven_lista.geometry('450x450')
        self.ven_lista.title("Listado de Ingresos")

        self.grilla = ttk.Treeview(self.ven_lista, columns=('col1', 'col2', 'col3', 'col4'))
        self.grilla.place(x=5, y=5, width=400, height=400)

        self.grilla.column('#0', width=20, anchor='ne')
        for col in range(1, 4):
            self.grilla.column(f'col{col}', width=80, anchor='nw')

        self.grilla.heading('#0', text='ID Planta')
        for i, text in enumerate(['Especie', 'Cajon','Cantidad Plantines'], start=1):
            self.grilla.heading(f'col{i}', text=text)

        btn_cerrar = Button(self.ven_lista, text='Cerrar', command=self.ven_lista.destroy)
        btn_cerrar.place(x=200, y=360)

        respuesta, plantas = listar_ingresos()
        if respuesta:
            if plantas:
                for fila in plantas:
                    print(fila)  
                    self.grilla.insert("", END, text=fila[0], values=fila[1:])
            else:
                print("No se encontraron plantas")
        else:
            print("Error al obtener las plantas")

                
        
    def salir(self):
        if messagebox.askyesno("Cerrar", "Confirma cerrar?"):
            self.ppal.destroy()
     
           
        
    
