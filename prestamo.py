from datetime import datetime, timedelta
from libro import Libro

class Prestamo:
    __libros_prestados = []

    def __init__(self, lector, libro):
        if not Prestamo.disponibilidad(libro):
            raise ValueError('El libro no se encuentra disponible')
        self.__lector = lector
        self.__libro = libro
        self.__fecha_prestamo = datetime.now()
        self.__fecha_devolucion = None
        Prestamo.__libros_prestados.append(libro.get_codigo())

    def get_lector(self):
        return self.__lector

    def get_libro(self):
        return self.__libro

    def get_fecha_prestamo(self):
        return self.__fecha_prestamo

    def get_fecha_devolucion(self):
        return self.__fecha_devolucion

    def set_fecha_devolucion(self, fecha_devolucion):
        self.__fecha_devolucion = fecha_devolucion

    @staticmethod
    def disponibilidad(libro):
        """
        Devuelve True si el libro está disponible para prestar.
        Devuelve False si el libro esta prestado actualmente.
        """
        if libro.get_codigo() in Prestamo.__libros_prestados:
            return False
        else:
            return True

    def devolucion(self, year, month, day):
        #En realidad lo suyo seria no incluir los parametros year, month y day, sino usar datetime.now().
        #Pero no vamos a esperar 15 dias reales para hacer la devolucion.
        self.set_fecha_devolucion(datetime(year, month, day))
        Prestamo.__libros_prestados.remove(self.get_libro().get_codigo())
        limite_devolucion = self.get_fecha_prestamo() + timedelta(days=15)
        if self.get_fecha_devolucion() > limite_devolucion:
            self.get_lector().marcar_moroso()


    @staticmethod
    def listar_prestados():
        for i in Prestamo.__libros_prestados:
            print(Libro.get_libro(i))
