class Libro:
    __id = 0
    __coleccion_libros = {}

    def __init__(self, titulo, autor, editorial):
        Libro.__id += 1
        self.__codigo = Libro.__id
        self.__titulo = titulo
        self.__autor = autor
        self.__editorial = editorial
        Libro.__coleccion_libros[self.get_codigo()] = self

    def __str__(self):
        return f'ID{self.get_codigo()}: ' + self.__titulo + ' (' + self.__autor + ', ' + self.__editorial + ')'

    def get_codigo(self):
        return self.__codigo

    def __eq__(self, otro):
        if not otro.isinstance(self):
            return NotImplemented
        else:
            return self.get_codigo() == otro.get_codigo()

    @staticmethod
    def get_libro(codigo):
        return Libro.__coleccion_libros[codigo]
