import httpx as http
from model.estudiantes_model import Estudiante,Alumno
class Formacion_Service:
    url="http://localhost:8000/alumnos"
    
    def alta_estudiante(self,estudiante:Estudiante):
        try:
            alumno:Alumno=Alumno(estudiante.nombre,estudiante.curso,estudiante.email,estudiante.calificacion)
            print(vars(alumno))
            respuesta = http.post(self.url,json=vars(alumno))
            respuesta.raise_for_status()
            return True
        except http.HTTPStatusError as e:
            print(e)
            return False

         
    def buscar_por_rango(self,min:float,max:float):
        resp=http.get(self.url)
        alumnos=resp.json()
        alumnos=list(filter(lambda a:a["nota"]>=min and a["nota"]<=max,alumnos)) #lista de alumnos filtrados
        return list(map(lambda a:Estudiante(nombre=a["nombre"],curso=a["curso"],email=a["email"],calificacion=a["nota"]),alumnos))
        