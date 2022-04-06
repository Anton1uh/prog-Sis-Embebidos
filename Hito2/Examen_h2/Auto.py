class Auto:
    __name = None
    __color = None
    __modelo = None
    __tamanio = None   #Ñ CAUSA ERRORES POR EXPERIENCIA
    __forma = None
    #constructor
    def __init__(self, name, color, modelo, tamanio, forma ):
        self.__name = name
        self.__color = color
        self.__modelo = modelo
        self.__tamanio = tamanio
        self.__forma = forma

    #sobreescribe al metodo self y lo imprime
    def __str__(self): ## \n salto de linea --> alt+92 = \
        return f'Nombre: {self.__name}  \nColor: {self.__color} \nModelo: {self.__modelo} \nTamaño: {self.__tamanio}\nForma: {self.__forma}'
    #encapsulacion
    ## getters
    def get_nombre(self):
            return self.__name
    ## setters
    def set_nombre(self, nuevo_nombre):
            self.__name = nuevo_nombre

    ##Métodos:
    def mover(self):
        print('Se ha movido el auto')

    def frenar(self ):
        print('Se ha frenado el auto')

    def girar_derecha(self ):
        print('Ha girado a la derecha')

    def girar_izquierda(self ):
        print('Ha girado a la izquierda')

#instanciando
auto1 = Auto('Mitsubishi','Blanco','L200','4 puertas','Camioneta')
print(auto1)
auto1.mover()
auto1.frenar()
auto1.girar_derecha()
auto1.girar_izquierda()

