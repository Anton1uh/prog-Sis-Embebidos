class Persona:
    __name = None
    __email = None
    __gender = None
    __nationality = None

    def __init__(self, name, email, gender, nationality):
        self.__name = name
        self.__email = email
        self.__gender = gender
        self.__nationality = nationality

    #sobreescribe al metodo self y lo imprime
    def __str__(self): ## \n salto de linea --> alt+92 = \
        return f'Nombre: {self.__name}  \nEmail: {self.__email} \nGénero: {self.__gender} \nNacionalidad: {self.__nationality}'
    #encapsulacion
    ## getters
    def get_nombre(self):
            return self.__name
    ## setters
    def set_nombre(self, nuevo_nombre):
            self.__name = nuevo_nombre

    ##Métodos:
    def write_book(self, name ):
        print('Ha escrito un libro')

    def write_movie(self, name ):
        print('Ha escrito una película')

    def change_nationality(self, new_nationality ):
        self.__nationality = new_nationality
        print('Se ha cambiado de nacionalidad')

    def change_email(self, new_email ):
        self.__email = new_email
        print('Se ha cambiado el Email.')


persona1 = Persona('Antonio', 'AntGonz@gmail.com', 'Masculino','Boliviano')
print(persona1)
persona1.change_nationality('Cubano')
print(persona1)
persona1.change_email('EmailNuevo@gmail.com')
print(persona1)










