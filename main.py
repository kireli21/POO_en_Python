from cosas import Alumno, Perro

def main():
    al1 = Alumno("Jose", 19, "ICO")
    print(vars(al1))
    al1.__nombre ="Diego"
    print(vars(al1))
    al1.set_nombre("Maria")
    print(vars(al1))
    print("----------------toString------------------")
    print(al1)
    al1.set_edad(999)
    print(al1)
    al1.estudiar(4)

    print("-----Perro---------")

    perro1 = Perro("poddle", 6, 0.35)
    print(vars(perro1))
    perro1.raza = "de la calle"
    print(vars(perro1))
    perro1.__raza = "otro"
    print(vars(perro1))
    perro1.edad = 2
    perro1.estatura = 0.45
    print(perro1)
    cachorro = Perro.es_cachorro(perro1.edad)
    print(cachorro)
    perro1.dormir()
    danes = Perro.perro_grande(0.8)
    print(danes)
main()