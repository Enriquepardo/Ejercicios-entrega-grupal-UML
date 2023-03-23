class Animal:
    def __init__(self, nombre, dieta, cuidador, requerimiento_alimenticio):
        self.nombre = nombre
        self.dieta = dieta
        self.cuidador = cuidador
        self.requerimiento_alimenticio = requerimiento_alimenticio

    def alimentar(self, comida):
        print(f"{self.nombre} está comiendo {comida}.")

class Herbivoro(Animal):
    def __init__(self, nombre, cuidador, requerimiento_alimenticio):
        super().__init__(nombre, "herbívoro", cuidador, requerimiento_alimenticio)

class Carnivoro(Animal):
    def __init__(self, nombre, cuidador, requerimiento_alimenticio):
        super().__init__(nombre, "carnívoro", cuidador, requerimiento_alimenticio)

class Insectivoro(Animal):
    def __init__(self, nombre, cuidador, requerimiento_alimenticio):
        super().__init__(nombre, "insectívoro", cuidador, requerimiento_alimenticio)

class Cuidador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.animales_asignados = []

    def asignar_animal(self, animal):
        self.animales_asignados.append(animal)
        animal.cuidador = self.nombre

    def tomar_vacaciones(self):
        for animal in self.animales_asignados:
            animal.cuidador = None
        self.en_vacaciones = True

    def regresar_vacaciones(self):
        self.en_vacaciones = False

class Comida:
    def __init__(self, nombre, tipo_alimento):
        self.nombre = nombre
        self.tipo_alimento = tipo_alimento
        self.cantidad = 0
        self.animales_asignados = []

    def reabastecer(self, cantidad):
        self.cantidad += cantidad

    def asignar_comida(self, animal):
        if animal.dieta == self.tipo_alimento:
            self.animales_asignados.append(animal)
            animal.cuidador.comida_asignada = self.nombre
        else:
            print(f"{animal.nombre} no come {self.tipo_alimento}.")

