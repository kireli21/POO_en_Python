class Alumno:
    facultad = "FES Aragon"
    def __init__(self, nom, ed, car):

        self.__nombre = nom
        self.__edad = ed
        self.__carrera = car
        print(type(self))