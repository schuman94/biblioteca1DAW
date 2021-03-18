from lector import Lector
from libro import Libro
from prestamo import Prestamo

#Creamos libros:
op1 = Libro('One Piece Volume 1', 'Eiichiro Oda', 'Shueisha')
op2 = Libro('One Piece Volume 2', 'Eiichiro Oda', 'Shueisha')
ds1 = Libro('Dr Stone Volume 1', 'Riichiro Inagaki', 'Shueisha')

#Creamos lectores:
ana = Lector(1, 'Ana', 'Garcia')
roberto = Lector(2, 'Roberto', 'Sanchez')

#Prestamos
p1 = Prestamo(ana, op1)
p2 = Prestamo(ana, op2)

Prestamo.listar_prestados()
print(ana.es_moroso())
p1.devolucion(2021, 3, 19)
print(ana.es_moroso())
Prestamo.listar_prestados()

print(p1.get_fecha_prestamo())
print(p1.get_fecha_devolucion())

print(ana)

p3 = Prestamo(roberto, op1)
print(op1)
print(p3.get_fecha_devolucion())
