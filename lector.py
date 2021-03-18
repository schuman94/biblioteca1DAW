class Lector:
    def __init__(self, numero, nombre, apellidos):
        self.__numero = numero
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__moroso = False

    def marcar_moroso(self):
        self.__moroso = True

    def es_moroso(self):
        return True if self.__moroso == True else False

    def __str__(self):
        return 'ID:' + str(self.__numero) + ' ' + self.__nombre + ' ' + self.__apellidos + (' -> MOROSO' if self.es_moroso() else '')
