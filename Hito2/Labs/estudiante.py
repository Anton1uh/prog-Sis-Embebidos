class Estudiante:
    __curso = None
    __email = None

    def __init__(self, curso, email):
        self.__curso = curso
        self.__email = email

    def __str__(self):
        return f'Curso: {self.__curso}, Email: {self.__email}'
