"""
Clase Estudiante base para el Examen Convocatoria Ordinaria de la UD4
:author: Jaime Rabasco
Refactorización
Extrae una superclase con los campos
	nombre
	apellidos
	nif
:author: Belen Maria Leon Fernandez
"""


class Persona:
    """
    Superclase Persona
    """
    @property
    def apellidos(self):
        """
        Metodo get de apellidos
        :author: Belen Leon
        :parameter:
        :return:
        """
        return self.__apellidos

    @apellidos.setter
    def apellidos(self, value):
        """
        Metodo setter de apellidos
        :author: Belen Leon
        :param value:
        :return:
        """
        self.__apellidos = value

    @property
    def nif(self):
        """
        Metodo get de nif
        :author: Belen Leon
        :parameter:
        :return:
        """
        return self.__nif

    @nif.setter
    def nif(self, value):
        """
        Metodo setter de nif
        :author: Belen Leon
        :param value:
        :return:
        """
        self.__nif = value

    @property
    def nombre(self):
        """
        Metodo get de nombre
        :author: Belen Leon
        :parameter:
        :return:
        """
        return self.__nombre

    @nombre.setter
    def nombre(self, value: int):
        """
        Metodo setter de nombre
        :author: Belen Leon
        :param value:
        :return:
        """
        self.__nombre = value


class Estudiante(Persona):
    """
    Clase estudiante
    :author: Belen Leon
    """
    nif = "11111111Z";
    curso = "Primaria";
    nombre = "Nombre";
    apellidos = "Apellidos";

    def __init__(self):
        pass;

    def __init__(self, nif, curso, nombre, apellidos):
        """
        Constructor de la clase Estudiante
        :author: Belen Leon
        :param nif:
        :param curso:
        :param nombre:
        :param apellidos:
        """
        self.nif = nif;
        self.curso = curso;
        self.nombre = nombre;
        self.apellidos = apellidos;

    @property
    def curso(self):
        """
        Metodo get de curso
        :author: Belen Leon
        :parameter:
        :return:
        """
        return self.__curso

    @curso.setter
    def curso(self, value):
        """
        Metodo setter de curso
        :author: Belen Leon
        :param value:
        :return:
        """
        self.__curso = value

