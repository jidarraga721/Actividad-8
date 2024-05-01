from carro_compra import CarroCompras

from libro import Libro
from excepciones import LibroExistenteError  # type: ignore

from excepciones import LibroAgotadoError, ExistenciasInsuficientesError # type: ignore

class TiendaLibros:
    def __init__(self):
        self.catalogo = {}
        self.carrito = CarroCompras()

    def adicionar_libro_a_catálogo(self, isbn, titulo, precio, existencias):
        if isbn in self.catalogo:
            raise LibroExistenteError(titulo, isbn)
        else:
            libro = Libro(isbn, titulo, precio, existencias)
            self.catalogo[isbn] = libro
            return libro

    def agregar_libro_a_carrito(self, libro, cantidad):
        if libro.existencias == 0:
            raise LibroAgotadoError(libro.titulo, libro.isbn)
        elif cantidad > libro.existencias:
            raise ExistenciasInsuficientesError(libro.titulo, libro.isbn, cantidad, libro.existencias)
        else:
            self.carrito.agregar_item(libro, cantidad)
    
    def retirar_item_de_carrito(self, isbn):
        self.carrito.quitar_item(isbn)
