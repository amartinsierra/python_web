from repository.libros_repository import Libros_Repository
from model.libros_model import Libro
class LibrosService:
    repo=Libros_Repository()
    def alta_libro(self,libro:Libro):
        if self.repo.find_by_isbn(libro.isbn):
            return None ##informamos al controlador de que no se ha podido dar de alta
        return self.repo.save(libro)
    def buscar_libro(self,isbn:int):
        libro=self.repo.find_by_isbn(isbn)
        if libro:
            """return Libro(isbn=libro["isbn"],
                         titulo=libro["titulo"],
                         autor=libro["autor"],
                         precio=libro["precio"],
                         paginas=libro["paginas"],
                         idTema=libro["idTema"])
                         """
            return Libro(**libro)
        return None
    def eliminar_libro(self,isbn:int):
        self.repo.delete_by_isbn(isbn)