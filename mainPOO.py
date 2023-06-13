from cosas import Alumno

def main():
    # noinspection PyInterpreter
    """
        al1 = Alumno()
        print(al1)
        al2 = Alumno()
        print(al1.facultad)
        print(al2.facultad)
        print(Alumno.facultad)
        print("--------------------------")
        Alumno.facultad = "FES Aragon EDOMEX"
        print(al1.facultad)
        print(al2.facultad)
        print(Alumno.facultad)
        print("----un vistazo al objeto")
        print(vars(al1))
        print(vars(al2))
        print("---modificar atributos publicos")
        al1.edad = 999
        print(vars(al1))
        print(vars(al2))
        """
    al1=Alumno("Diego", 19, "ICO")
    al2 = Alumno("Monse", 20, "Derecho")

    al1.__edad=2465

    print(al1.__edad)
    print(vars(al1))

main()