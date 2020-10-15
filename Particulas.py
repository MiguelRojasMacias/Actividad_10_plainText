from particula import Particula

class Particulas:
    def __init__(self):
        self.__particulas = []
    
    def agregar_final(self, particula:Particula):
        self.__particulas.append(particula)
    
    def agregar_inicio(self, particula:Particula):
        self.__particulas.insert(0, particula)

    def mostrar(self):
        for particulas in self.__particulas:
            print(particulas)

    def __str__(self):
        return "".join(
            str(particulas) + '\n'for particulas in self.__particulas #añade cada particula como si fuera un string
        )#con las comillas creamos un string vacio y join recibe N cantidad de elementos
