from repository.alumnos_repository import AlumnoRepository
from model.alumnos_model import Alumno
class AlumnoService:
    alumno_repository=AlumnoRepository()    
    def alta_alumno(self,alumno:Alumno):
        #no puede haber alumnos con mismo email
        if self.existe_alumno(alumno.email,alumno.curso):
            return False
        else:
            self.alumno_repository.save(alumno)
            return True
    def existe_alumno(self,email:str,curso:str):
        alumno=self.alumno_repository.find_by_email_and_curso(email,curso)
        return alumno!=None
    
    def todos_alumnos(self):
        return self.alumno_repository.find_all()
    
    def alumnos_curso(self,curso:str):
        return self.alumno_repository.find_by_curso(curso)
    
    def eliminar_alumno(self, email:str):
        alumno=self.alumno_repository.find_by_email(email)
        if alumno!=None:
            self.alumno_repository.delete_by_email(email)
        return alumno
        