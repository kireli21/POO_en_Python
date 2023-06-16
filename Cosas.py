class Autor:
    def __init__(self, nom, seudo):
        self.__nombre = nom
        self.__seudonimo = seudo

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,nom):
        self.__nombre = nom

    @property
    def seudonimo(self):
        return self.__seudonimo

    @nombre.setter
    def seudonimo(self, seudo):
        self.__seudonimo = seudo

    def __str__(self):
        return f"Nombre {self.__nombre}, pseudonimo: {self.__seudonimo}"

    def escribir(self):
        print(f"{self.__seudonimo} esta escribiendo su siguiente obra")

class Libro:
    def __init__(self, titulo, aut, anio, edi):
        self.__titulo = titulo
        self.__autor = aut
        self.__anio = anio
        self.__editorial = edi

    @property
    def titulo(self):
        return self.__titulo
    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def autor(self):
        return self.__autor
    @autor.setter
    def autor(self,aut):
        self.__autor = aut

    @property
    def anio(self):
        return self.__anio
    @anio.setter
    def anio(self, anio):
        self.__anio = anio

    @property
    def editorial(self):
        return self.__editorial
    @editorial.setter
    def editorial(self, edi):
        self.__editorial = edi

    def __str__(self):
        return f"""
        Titulo: {self.__titulo}
        Autor: {self.__autor}
        Editorial: {self.__editorial}
        Año: {self.__anio}
        """

    @classmethod
    def libro_planeta(cls, titulo, autor, anio):
        return cls(titulo, autor, anio, "planeta")

    def leer(self, minutos):
        print(f"leyendo por {minutos} minutos")

class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nom):
        self.__nombre = nom

class Alumno(Persona):
    def __init__(self, nombre, edad, cuenta, carrera, promedio):
        super().__init__(nombre, edad)
        self.__numero_cuenta = cuenta
        self.__carrera = carrera
        self.__promedio = promedio