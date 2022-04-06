class Campeonato:
    __nombreCampeonato = str
    __equipos = []

    def __init__(self, nombreC, equipo):
        self.__nombreCampeonato = nombreC
        self.__equipos = equipo

    ## getters
    def getNombreCampeonato(self):
       return self.__nombreCampeonato

    def setNombreCampeonato(self, nuevo_nombreC):
        self.__nombreCampeonato = nuevo_nombreC

    def getEquipo(self):
        return self.__equipos

    def setEquipo(self, nuevo_equipo):
        self.__equipos = nuevo_equipo

    def imprimir(self):
        print("Imprimiendo listas")

class Equipo(Campeonato):
    __nombreEquipo = str
    __categoria = str
    __jugadores = []

    def __init__(self, nombreC, equipo, nombreE, cat, jug):
        Campeonato.__init__(self, nombreC, equipo)
        self.__nombreEquipo = nombreE
        self.__categoria = cat
        self.__jugadores = jug

    def getNombreEquipo(self):
       return self.__nombreEquipo

    def setNombreEquipó(self, nuevo_nombreE):
        self.__nombreEquipo = nuevo_nombreE

    def getCat(self):
        return self.__categoria

    def setCat(self, nuevo_cat):
        self.__categoria = nuevo_cat

    def getJugadores(self):
        return self.__jugadores

    def setJugadores(self, nuevo_Jugador):
        self.__jugadores = nuevo_Jugador

    def imprimirEquipo(self):
        print("Imprimiendo listas de equipo")

class Jugador(Equipo):
    __nombreCompleto = str
    __apellidos = str
    __ci = str
    __edad = int

    def __init__(self, nombreEquipo, catE, jugE, fullname, lastname, ci, edad):
        Equipo.__init__(self,nombreEquipo, catE, jugE)
        self.__nombreCompleto = fullname
        self.__apellidos = lastname
        self.__ci = ci
        self.__edad = edad

    def getNombreCompleto(self):
        return self.__nombreCompleto
    def setNombreCompleto(self, nuevoName):
        self.__nombreCompleto = nuevoName
    def getApellidos(self):
        return  self.__apellidos
    def setApellidos(self, nuevoAp):
        self.__apellidos = nuevoAp
    def getCI(self):
        return self.__ci
    def setCI(self, nuevoCI):
        self.__ci = nuevoCI
    def getEdad(self):
        return self.__edad
    def setEdad(self, nuevaEdad):
        self.__edad = nuevaEdad
    def imprimirNombre(self):
        print("Imprimiendo listas de nombre")



Jugador1 = Jugador('Pepito1',"Huiy Ter1","4553522 cbba",20)
Jugador2 = Jugador('Pepito2',"Huiy Ter2","4553522 cbba",24)
Jugador3 = Jugador('Pepito3',"Huiy Ter3","4553522 cbba",25)
Jugador4 = Jugador('Pepito4',"Huiy Ter4","4553522 cbba",18)
Jugador5 = Jugador('Pepito5',"Huiy Ter5","4553522 cbba",22)











