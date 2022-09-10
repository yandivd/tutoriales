import pickle
class Autos():
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

    def __init__(self):
        archivo=open("fileAutos","ab+")
        archivo.seek(0)
        try:
            self.listaAutos=pickle.load(archivo)
            print("Se cargaron {} autos".format(len(self.listaAutos)))
        except:
            print("Archivo Vacio")
        finally:
            archivo.close()
            del(archivo)
    
    def AgregarAuto(self,auto):
        self.listaAutos.append(auto)
        self.AgregarAutoAlFichero()

    def Eliminar(self):
        listaVacia=[]
        archivo=open("fileAutos","wb")
        pickle.dump(listaVacia, archivo)
        archivo.close()
        del(archivo)
        archivo=open("fileAutos","rb")
        self.listaAutos=pickle.load(archivo)
        archivo.close()
        del(archivo)

    def EliminarCoche(self,indice):
        archivo=open("fileAutos","wb")
        autoEliminado=self.listaAutos[indice]
        self.listaAutos.pop(indice)
        pickle.dump(self.listaAutos, archivo)
        print("Auto ",autoEliminado.numChapa," eliminado")
        archivo.close()
        del(archivo)

    def AgregarAutoAlFichero(self):
        archivo=open("fileAutos","wb")
        pickle.dump(self.listaAutos, archivo)
        archivo.close()
        del(archivo)

    def MostrarAutos(self):
        a=1
        for i in self.listaAutos:
            print("| ",a, i)
            a+=1

def Mostrar():
    x=input("\nDesea ver todos los coches almacenados? (y/n): ")
    print("------------------------------------------------------------------------")
    if x=='y':
        miCuchera.MostrarAutos()
        print("------------------------------------------------------------------------")
    else:
        pass

def Pintar():
    print("  ______ \n"
 "/|_||_\`.__ \n"
"(   _    _ _\  \n"
"=`-(_)--(_)-' \n"
)

def MostrarMenu():
    print("1----> Mostrar Lista de Autos")
    print("2----> Agregar Auto")
    print("3----> Sacar Auto")
    print("4----> Vaciar Cochera")
    print("99---> Salir")
    variable=input("Inserte una opcion para continuar: \n")
    return variable

def Start():
    confirm='n'
    option=MostrarMenu()
    if option=='1':
        print("------------------------------------------------------")
        miCuchera.MostrarAutos()
        print("------------------------------------------------------")
        Start()

    elif option=='2':
        n=int(input("Inserte la cantidad de autos que quiere agregar a la cochera(inserte 0 para ir atras): "))
        if n==0:
            Start()
        else:
            a=1
            while a<=n:
                print("\nDatos del coche {} ".format(a))
                marca=input("Marca: ")
                modelo=input("Modelo: ")
                color=input("Color: ")
                numChapa=input("Matricula: ")
                velMax=input("Maxima Velocidad que Alcanza en km/h: ")
                autoAux=Autos(marca, modelo, color, numChapa, velMax)
                miCuchera.AgregarAuto(autoAux)
                a+=1
            Start()
    
    elif option=='3':
        aEliminar=int(input("Inserte el numero del auto a eliminar: "))
        indiceValido=aEliminar
        if indiceValido<=int(len(miCuchera.listaAutos)):
            confirm=input("seguro que desea eliminar este vehiculo?(y/n) ")
            if confirm=='y':
                miCuchera.EliminarCoche(aEliminar-1)
                Mostrar()
                confirm='n'
                Start()
            else:
                print("Operacion Cancelada")
                Start()
        else:
            print("Ese indice no es valido")
            Start()

    elif option=='4':
        confirm=input("Seguro que desea vaciar todo el garaje? (y/n)")
        if confirm=='y':
            miCuchera.Eliminar()
            Mostrar()
            confirm='n'
            Start()
        else:
            print("Operacion Cancelada")
            Start()
    
    elif option=="99":
        pass


#####Ejecucion del Programa Principal
miCuchera=Cochera()
Pintar()
Start()


