from classroom.asignatura import Asignatura

class Grupo:
    grado = 'Grado 12'

    def __init__(self, grupo="grupo predeterminado", asignaturas=[], estudiantes=[]):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes
        
    def listadoAsignaturas(self, **kwargs):
        if self._asignaturas==None:
            self._asignaturas=[]
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista=None): 
        if self.listadoAlumnos == []:
            nvlista = []; self.listadoAlumnos = nvlista;
        if lista!=None:
            lista.append(alumno)
            self.listadoAlumnos.extend(lista)
            return
        self.listadoAlumnos.append(alumno)

    def __str__(self):
        return 'Grupo de estudiantes: '+self._grupo;

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

"""     @ classmethod
    def asignarNombre(cls, nombre="Grado 10"):
        cls.grado = nombre
 """
"""     @ classmethod
    def asignarNombre(cls, nombre="Grado 4"):
        cls.grado = nombre """
