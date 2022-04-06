class Persona:
    __fullname = None
    __lastname = None
    __age = None

    def __init__(self, fullname, lastname, age):
        self.__fullname = fullname
        self.__lastname = lastname
        self.__age = age


    def __metodo_privado(self):
        print('Metodo PRIVADO!')

    def metodo_publico(self):
        print('Metodo publico')

    #sobreescribe al metodo self y lo imprime
    def __str__(self): ## \n salto de linea --> alt+92 = \
        return f'Persona: {self.__fullname}  \nApellidos: {self.__lastname} \nEdad: {self.__age} \n'

    #encapsulacion
    ## getters
    def get_nombres(self):
            return self.__fullname
    ## setters
    def set_nombres(self, nuevo_nombre):
            self.__fullname = nuevo_nombre
    ##metodo update de los 3 atributos
    def update_persona(self, nuevo_nombre, nuevo_apellido, nueva_edad):
            self.__fullname = nuevo_nombre
            self.__lastname = nuevo_apellido
            self.__age = nueva_edad

#DEFINIENDO LA HERENCIA
class Estudiante(Persona):
    __curso = None
    __email = None

    def __init__(self, fullname, lastname, age, curso, email):
        Persona.__init__(self, fullname, lastname, age )
        self.__curso = curso
        self.__email = email

    def __str__(self):
        return Persona.__str__(self) + f'\nCurso: {self.__curso} \nEmail: {self.__email}'
##ootraherencia

class Administrativo(Persona):
    __sueldo = None
 
    def __init__(self, fullname, lastname, age, sueldo):
        Persona.__init__(self, fullname, lastname, age )
        self.__sueldo = sueldo

    def __str__(self):
        return Persona.__str__(self) + f'Sueldo: {self.__sueldo}'


##instancia
persona1 = Persona('Antonio','Gonzales', 22) 
estudiante1 = Estudiante('Antonio1','Gonzales1',22,'212-LAB','correo@gmail.com')
administrativo1 = Administrativo('Antonio1','Gonzales1', 22, 2100)
#print(estudiante1)
print(administrativo1)
#GET
#print(persona1.get_nombres())
#SET
#persona1.set_nombres('NuevoNombre')
#print(persona1.get_nombres())
#print(persona1)
#persona1.update_persona('NuevoNombre','NuevoApellido',15)

#print(persona1) 







#print(persona1)
    







#persona1.metodo_publico()
#persona1.__metodo_privado()
