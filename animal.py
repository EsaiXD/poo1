"""
1. qué palabra reservada se utiliza en lugar de animal  (nombre de la clase) para acceder al atributo patas 

2. que palabra reserbada hay que utilizar para crear un nuevo objeto
"""


class animal:
    patas = 0

    def caminar(self):
        print("caminando con", self.patas "patas")


def main():
    vaca = animal()
    vaca.patas = 4
    vaca.caminar()

    pato = animal()
    pato.patas = 2
    pato.caminar()

if __name__ == "__main__":
    main()