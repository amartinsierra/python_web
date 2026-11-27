import httpx as http
from model.libro_model import Libro,Ejemplar
class Ejemplares_Service:
    url="http://localhost:8000/libro"
    
    def buscar_ejemplar(self,isbn:str):
        resp=http.get(self.url+"/"+str(isbn))
        libro=Libro(**resp.json())
        if libro.paginas>400:
            dificultad="alta"
        elif libro.paginas<=400 and libro.paginas>250:
            dificultad="media"
        else:
            dificultad="baja"
        return Ejemplar(isbn=libro.isbn,titulo=libro.titulo,dificultad=dificultad)