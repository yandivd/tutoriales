from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pickle

class Auto():
    def __init__(self,marca,modelo,color,numChapa,velMax):
        self.marca=marca
        self.modelo=modelo
        self.color=color
        self.numChapa=numChapa
        self.velMax=velMax

    def __str__(self):
        return "{} {} {} {} {}".format(self.marca, self.modelo, self.color, self.numChapa, self.velMax)

class Cochera():
    listaAutos=[]
    eliminadoAux=""

    def __init__(self):
        archivo=open("archivoAutos","ab+")
        archivo.seek(0)
        try:
            self.listaAutos=pickle.load(archivo)
            print("Se cargaron {} autos".format(len(self.listaAutos)))
        except:
            print("Archivo Vacio")
        finally:
            archivo.close()
            del(archivo)
    
    def LimpiarTabla(self):
        for row in tv.get_children():
            tv.delete(row)
    
    def MostrarAutos(self):
        self.LimpiarTabla()
        a=0
        #listaDeLabel.set("")
        for i in self.listaAutos:
            tv.insert(parent='', index=a, iid=a, text='', values=(a+1,i.marca,i.modelo, i.color, i.numChapa, i.velMax))
            #listaDeLabel.set(listaDeLabel.get()+str(i)+"\n")
            #print("| ",a, i)
            a+=1   
             
    def EliminarSeleccionado(self):
        seleccionado=tv.selection()[0]
        self.EliminarCoche(tv.index(seleccionado))
        tv.delete(seleccionado)
        self.InfoAutoEliminado(self.eliminadoAux)

    def CrearAuto(self, marca, modelo, color, chapa, velMax):
        autoAux=Auto(marca, modelo, color, chapa, velMax)
        self.AgregarAuto(autoAux)

    def AgregarAuto(self,auto):
        self.listaAutos.append(auto)
        self.AgregarAutoAlFichero()

    def AgregarAutoAlFichero(self):
        archivo=open("archivoAutos","wb")
        pickle.dump(self.listaAutos, archivo)
        archivo.close()
        del(archivo)
    
    def InfoAutoAgregado(self):
        messagebox.showinfo("Operacion realizada", "Auto agregado con exito")

    def InfoAutoEliminado(self,autoelim):
        messagebox.showinfo("Operacion realizada","Auto "+autoelim.numChapa+" marca "+autoelim.marca+" eliminado correctamente")

    def ConfirmacionVaciado(self):
        valor=messagebox.askquestion("Vaciar","Seguro desea vaiar todos los datos?")
        if valor=="yes":
            self.Vaciar()
        else:
            pass

    def Vaciar(self):
        #listaDeLabel.set("")
        self.LimpiarTabla()
        listaVacia=[]
        archivo=open("archivoAutos","wb")
        pickle.dump(listaVacia, archivo)
        archivo.close()
        del(archivo)
        archivo=open("archivoAutos","rb")
        self.listaAutos=pickle.load(archivo)
        archivo.close()
        del(archivo)

    def EliminarCoche(self,indice):
        archivo=open("archivoAutos","wb")
        autoEliminado=self.listaAutos[indice]
        self.listaAutos.pop(indice)
        pickle.dump(self.listaAutos, archivo)    
        miFramePedidos=Frame(raizPedidos)
        miFrame.pack()
        print("Auto ",autoEliminado.numChapa," eliminado")
        archivo.close()
        del(archivo)
        self.eliminadoAux=autoEliminado

    def MenuAgregarAuto(self):
        raizAgAuto=Toplevel(raiz)
        raizAgAuto.geometry("500x400")
        raizAgAuto.title("Agregar Auto")
        raizAgAuto.focus_set()
        raizAgAuto.grab_set()
        raizAgAuto.transient(master=raiz)

        ##########Formulario#####################
        Label(raizAgAuto,text="Garagcom", fg="red", font=("Comics Sans MS",20)).grid(row=0, column=0, pady=20, columnspan=3)
        Label(raizAgAuto, text="Inserte los datos del auto que desea agregar: ").grid(row=1, column=1, padx=5, pady=10, columnspan=3)
        ###Marca###
        labelMarca=Label(raizAgAuto, text="Marca:")
        labelMarca.grid(row=3, column=0, padx=20, pady=10, sticky="e")
        marca=StringVar()
        entryMarca=Entry(raizAgAuto, textvariable=marca)
        entryMarca.grid(row=3, column=1, padx=2, pady=10, sticky="w")
        ###Modelo###
        labelModelo=Label(raizAgAuto, text="Modelo:")
        labelModelo.grid(row=4, column=0, padx=20, pady=10, sticky="e")
        modelo=StringVar()
        entryModelo=Entry(raizAgAuto, textvariable=modelo)
        entryModelo.grid(row=4, column=1, padx=2, pady=10, sticky="w")
        ###Color###
        labelColor=Label(raizAgAuto, text="Color:")
        labelColor.grid(row=5, column=0, padx=20, pady=10, sticky="e")
        color=StringVar()
        entryColor=Entry(raizAgAuto, textvariable=color)
        entryColor.grid(row=5, column=1, padx=2, pady=10, sticky="w")
        ###Numero de chapa####
        labelChapa=Label(raizAgAuto, text="Matricula:")
        labelChapa.grid(row=6, column=0, padx=20, pady=10, sticky="e")
        chapa=StringVar()
        entryChapa=Entry(raizAgAuto, width=10, textvariable=chapa)
        entryChapa.grid(row=6, column=1, padx=2, pady=10, sticky="w")
        ###Velocidad Maxima####
        labelVel=Label(raizAgAuto, text="Velocidad Max:")
        labelVel.grid(row=7, column=0, padx=20, pady=10, sticky="e")
        vel=StringVar()
        entryVel=Entry(raizAgAuto, width=6, textvariable=vel)
        entryVel.grid(row=7, column=1, padx=2, pady=10, sticky="w")

        ###Boton Atras###
        botonCancel=Button(raizAgAuto, text="Atras", width=6, command=raizAgAuto.destroy)
        botonCancel.grid(row=8, column=0, padx=10, pady=10, sticky="w")
        botonCancel.config(background="red")
        ###Boton Aceptar###
        botonAcept=Button(raizAgAuto, text="Aceptar", width=6, command=lambda: [miGarage.CrearAuto(marca.get(), modelo.get(), color.get(), chapa.get(), vel.get()),miGarage.InfoAutoAgregado() ,miGarage.MostrarAutos(),raizAgAuto.destroy()])
        botonAcept.grid(row=8, column=3, padx=10, pady=10)
        botonAcept.config(justify="center")
        botonAcept.config(background="green")


#######Ejecucion###############
miGarage=Cochera()

#######interfaz grafica#####################
raiz=Tk()
raiz.geometry("700x500")
raiz.title("GaragApp")

miFrame=Frame(raiz,width="600", height="450")
miFrame.pack()

labelPresentacion=Label(miFrame,text="Garagcom", fg="red", font=("Comics Sans MS",20))
labelPresentacion.grid(row=0, column=0, pady=20, columnspan=3)
labelComentario=Label(miFrame,text="Este software gestiona todos los vehiculos que se guardan en un \ndeterminado garage")
labelComentario.grid(row=1, column=0, padx=5, columnspan=3)
labelComentario.config(justify="center")

botonMostrar=Button(miFrame, text="Mostrar Autos", width=12, height=2, command=miGarage.MostrarAutos)
botonMostrar.grid(row=2, column=0, pady=5)

botonAdd=Button(miFrame, text="Agregar Auto", width=12, height=2, command=miGarage.MenuAgregarAuto)
botonAdd.grid(row=3, column=0, pady=5)

botonDel=Button(miFrame, text="Eliminar Auto", width=12, height=2, command=miGarage.EliminarSeleccionado)
botonDel.grid(row=4, column=0, pady=5)

botonClean=Button(miFrame, text="Limpiar Datos", width=12, height=2, command=miGarage.ConfirmacionVaciado)
botonClean.grid(row=5, column=0, pady=5)

botonExit=Button(miFrame, text="Salir",width=12, height=2, command=raiz.destroy)
botonExit.grid(row=6, column=0, pady=5)

#Label que deberia mostrar la informacion de los autos
#listaDeLabel=StringVar()
#labelListado=Label(miFrame, height=12, width=40, textvar=listaDeLabel)
#labelListado.grid(row=2, column=1,rowspan=4, padx=10, pady=10)
#labelListado.config(background="white")

#Creando el treeview
tv=ttk.Treeview(miFrame, height=12)
tv.grid(row=2, column=1, rowspan=4, padx=10, pady=10)

#Definiendo las columnas
tv['columns']=('ID', 'Marca', 'Modelo','Color', 'Matricula', 'VelMax')
tv.column('#0', width=0, stretch=NO)
tv.column('ID', anchor=CENTER, width=20)
tv.column('Marca', anchor=CENTER, width=80)
tv.column('Modelo', anchor=CENTER, width=80)
tv.column('Color', anchor=CENTER, width=80)
tv.column('Matricula', anchor=CENTER, width=80)
tv.column('VelMax', anchor=CENTER, width=80)

#Nombrando las columnas
tv.heading('#0', text='', anchor=CENTER)
tv.heading('ID', text='ID', anchor=CENTER)
tv.heading('Marca', text='Marca', anchor=CENTER)
tv.heading('Modelo', text='Modelo', anchor=CENTER)
tv.heading('Color', text='Color', anchor=CENTER)
tv.heading('Matricula', text='Matricula', anchor=CENTER)
tv.heading('VelMax', text='Vel Max', anchor=CENTER)

# Configurando Barra de Scroll
MiBarraDeScrolly = Scrollbar(miFrame,command=tv.yview)
MiBarraDeScrolly.grid(row=5,column=2,sticky='nsew',pady=10)
tv.config(yscrollcommand=MiBarraDeScrolly.set)

raiz.mainloop()