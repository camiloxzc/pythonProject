from models.student import Student

class StudentController:
    def __int__(self):
        print("Creando controlador para estudiantes")

    def index(self):
        print("Listar todos los estudiates")
        students = [
            {
                "name": "brayan",
                "lastname": "garcia",
                "age": 23
            },
            {
                "name": "luis",
                "lastname": "gomez",
                "age": 32
            }
        ]
        return students

    def create(self, info):
        print("Creando un estudiante")
        student = Student(info)
        return student.__dict__

    def show(self, id):
        print("Mostrando detalle de estudiante por id:", id)
        student = {
              "name": "brayan",
              "lastname": "garcia",
              "age": 23
            }
        return student

    def update(selfs, id, info):
        print("ACtualizando estudiante por id: ", id)
        student = {
            "name": "brayan",
            "lastname": "garcia",
            "age": 23
        }
        return student
    def delete(self, id):
        print("Eliminando estudiante por id: ", id)

        return {"deleted_count": 1}



