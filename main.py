from Cosas import *

def main():
    l1=Libro.libro_planeta("El perfume", Autor("Patrick","PS"), 1980)
    #Cambiar seudonimo
    l1.autor.seudonimo = l1.autor.seudonimo.lower()
    print(l1)
    print("------------Herencia--------------")
    al2 = Alumno("Jose", 19, "318203", "ICO", 9)
    print(vars(al2))
main()