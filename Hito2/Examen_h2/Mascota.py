class Mascota:
    nombreMascota = None
    edadMascota = int
    tipoMascota = None

    # constructor
    def __init__(self, name, edad, tipo):
        self.nombreMascota = name
        self.edadMascota = edad
        self.tipoMascota = tipo

    def __str__(self):  ## \n salto de linea --> alt+92 = \
        return f'NombreMasctoa: {self.nombreMascota}  \nEdad: {self.edadMascota} \nTipoMascota:{self.tipoMascota}'
    # encapsulacion
    ## getters
    def get_nombre(self):
        return self.nombreMascota

    ## setters
    def set_nombre(self, nuevo_nombre):
        self.nombreMascota = nuevo_nombre
    ##instanciar

Mascota1 = Mascota('Perro',10,'Canino')
print(Mascota1)
    ### herencia
class Duenio(Mascota):
    ci_duenio = int
    nombreDuenio = None
    celularDuenio = int

    def __init__(self, nameM, edadM, tipoM, ci, nameD, celD):
        Mascota.__init__(self, nameM, edadM, tipoM)
        self.ci_duenio = ci
        self.nombreDuenio = nameD
        self.celularDuenio = celD

    def __str__(self): ## \n salto de linea --> alt+92 = \
        return f'ciD: {self.ci_duenio}  \nNombreDue: {self.nombreDuenio} \n Cel: {self.celularDuenio}\n'

Duenio1 = Duenio('PerroPrueba',12,'Felino',2132,'Antonio',321)
print(Duenio1)

class HistorialClinico(Mascota):
    nroHistorial = int
    doctorHistorial = None
    def __init__(self,nameM, edadM, tipoM, nroH, doctor):
        Mascota.__init__(self, nameM, edadM, tipoM)
        self.nroHistorial = nroH
        self.doctorHistorial = doctor
    def __str__(self):
        return f'NombreMascota: {self.nombreMascota}  \nEdad: {self.edadMascota} \nTipoMascota:{self.tipoMascota}\nNroHistorial:{self.nroHistorial}\nDoctor:{self.doctorHistorial}'


HistorialClinico1 = HistorialClinico('Perro',9,'Canino',23,'RicardoPerez')
print(HistorialClinico1)





