from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

class Pedido():
    def __init__(self,nombre, direccion, propietario):
        self.nombre=nombre
        self.direccion=direccion
        self.propietario=propietario

class PedidoCompletado():
    def __init__(self,pedido,nombreMensajero):
        self.pedido=pedido
        self.mensajero=nombreMensajero

def MenuAgregarPedido():
    raizAdd=Toplevel(raiz)
    raizAdd.focus_set()
    raizAdd.grab_set()
    raizAdd.title("Agregar pedido")
    raizAdd.transient(master=raiz)

    miFrame2=Frame(raizAdd)
    miFrame2.pack()

    logo=Label(miFrame2,image=imagen)
    logo.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

    #formulario
    labelNombre=Label(miFrame2, text="Nombre: ")
    labelNombre.grid(row=1, column=0, padx=5, pady=10, sticky="e")

    nombre=StringVar()
    entryNombre=Entry(miFrame2, textvariable=nombre)
    entryNombre.grid(row=1, column=1, padx=5, pady=10, sticky='w')

    labelDireccion=Label(miFrame2, text="Direccion: ")
    labelDireccion.grid(row=2, column=0, padx=5,pady=10, sticky="e")

    direccion=StringVar()
    entryDireccion=Entry(miFrame2, textvariable=direccion)
    entryDireccion.grid(row=2, column=1, padx=5, pady=10, sticky="w")

    labelPropietario=Label(miFrame2, text="A nombre de: ")
    labelPropietario.grid(row=3, column=0, padx=5, pady=10, sticky='e')

    propietario=StringVar()
    entryProp=Entry(miFrame2,textvariable=propietario)
    entryProp.grid(row=3, column=1, padx=5, pady=10, sticky='w')

    ##########Botones de aceptar y cancel######################
    



#def AgregarPedido():
#    pedidoAux=Pedido(nombre, direccion, propietario)
    


#-----GUI--------------------------------------
def MOstrarFormPedidos():
    #Aqui voy a desarrollar el formulario para agregar un pedido
    pass

def MostrarMenuPedidos():
    raizPedidos=Toplevel(raiz)
    raizPedidos.focus_set()
    raizPedidos.grab_set()
    raizPedidos.transient(master=raiz)
    #raizPedidos.geometry("400x200")

    tv=ttk.Treeview(raizPedidos,height=12)
    tv.grid(row=0, column=0, padx=10, pady=10, columnspan=3)

    tv['columns']=('ID', 'Pedido', 'Direccion','Propietario')
    tv.column('#0', width=0, stretch=NO)
    tv.column('ID', anchor=CENTER, width=20)
    tv.column('Pedido', anchor=CENTER, width=80)
    tv.column('Direccion', anchor=CENTER, width=80)
    tv.column('Propietario', anchor=CENTER, width=80)

    tv.heading('#0', text='', anchor=CENTER)
    tv.heading('ID', text='ID', anchor=CENTER)
    tv.heading('Pedido', text='Pedido', anchor=CENTER)
    tv.heading('Direccion', text='Direccion', anchor=CENTER)
    tv.heading('Propietario', text='Propietario', anchor=CENTER)

    botonAgregarPedido=Button(raizPedidos, text="Agregar Pedido", command=MenuAgregarPedido)
    botonAgregarPedido.grid(row=1, column=0, pady=10, padx=10)

    botonEliminarPedido=Button(raizPedidos, text="Eliminar Pedido")
    botonEliminarPedido.grid(row=1, column=1, padx=10, pady=10)

    botonAtras=Button(raizPedidos, text="Atras", command=raizPedidos.destroy)
    botonAtras.grid(row=1, column=2, padx=10, pady=10)

    miConexion=sqlite3.connect("pedidos")
    miCursor=miConexion.cursor()

    miCursor.execute("SELECT * FROM PEDIDOS")

    infoUser=miCursor.fetchall()
    a=0
    for i in infoUser:
        tv.insert(parent='', index=a, iid=a, text='', values=(i[0], i[1], i[2],i[3]))




def ConeccionDDBB():
    miConexion=sqlite3.connect("pedidos")
    miCursor=miConexion.cursor()

    try:
        miCursor.execute('''
        CREATE TABLE PEDIDOS(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NAME VARCHAR(20),
        ADDRESS VARCHAR(60),
        PROPIETARIO VARCHAR(20) )
        ''')

    except:
        pass

def NoHacerNada():
    pass

raiz=Tk()
raiz.title("Rustica")

miFrame=Frame(raiz)
miFrame.pack()

imagen=PhotoImage(file="index.png")
logo=Label(miFrame,image=imagen)
logo.grid(row=0, column=1, padx=10, pady=10)

botonPedidos=Button(miFrame, text="Pedidos Pendientes", width=14, height=2, command=MostrarMenuPedidos)
botonPedidos.grid(row=1, column=1, padx=10, pady=10)

botonPedidos=Button(miFrame, text="Pedidos Terminados", width=14, height=2, command=NoHacerNada)
botonPedidos.grid(row=2, column=1, padx=10, pady=10)

botonExit=Button(miFrame, text="Salir", width=8, height=2, command=raiz.destroy)
botonExit.grid(row=3, column=1, padx=10, pady=10)

ConeccionDDBB()

raiz.mainloop()