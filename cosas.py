class Alumno:
    facultad = "FES Aragón"

    def __init__(self, nom, ed, car):
        self.__nombre = nom
        self.__edad = ed
        self.__carrera = car

    def set_nombre(self, nom):
        self.__nombre = nom
    def get_nombre(self):
        return  self.__nombre

    def set_edad(self, ed):
        if ed >= 8 and ed < 120:
            self.__edad = ed
        else:
            print("La edad es incorrecta")
            self.__edad = 0
    def get_edad(self):
        return self.__edad

    def set_carrera(self, car):
        self.__carrera = car
    def get_edad(self):
        return self.__carrera

    def __str__(self):
        cadena = "nombre " + self.__nombre
        cadena = cadena + "\nedad " + str(self.__edad)
        cadena = cadena + "\ncarrera " + self.__carrera
        cadena = cadena + "\n........................................."
        return cadena

    def estudiar(self, horas):
        print(f"El alumno {self.__nombre} esta estudiando por {horas} horas")

class Perro:
    reino = "Canino"

    def __init__(self, raza, edad, estatura):
        self.__raza = raza
        self.__edad = edad
        self.__estatura = estatura

    #Get
    @property
    def raza(self):
        return self.__raza
    #Set
    @raza.setter
    def raza(self, raza):
        self.__raza = raza

    @property
    def edad(self):
        return self.__edad
    @edad.setter
    def edad(self, edad):
        if edad > 0 and edad < 20:
            self.__edad = edad
        else:
            prin("Edad no valida")
            self.__edad = 0

    @property
    def estatura(self):
        return self.__estatura
    @estatura.setter
    def estatura(self, estatura):
        if estatura > 0.1 and estatura < 1.1:
            self.__estatura = estatura
        else:
            print("imposible")
            self.__estatura = 0

    def __str__(self):
        return f"""
        _____________________________
        |Raza: {self.__raza}
        |Edad: {self.__edad}
        |Estatura: {self.__estatura}
        |____________________________
        """

    @staticmethod
    def es_cachorro(edad):
        return edad <3

    @staticmethod
    def dormir(vueltas = 5):
        for i in range(vueltas):
            print(f"Dando vuelta {i+1}")
        print("zzzzzz")

    @classmethod
    def perro_grande(cls, est):
        if est > 0.79:
            return cls("",0,est)