from models.department import Departments

class DepartmentController:
    def __int__(self):
        print("Creando controlador para departamento")

    def index(self):
        print("Listar todos los departamento")
        department = [
            {
                "name": "Ingenieria",
                "lastname": "garcia",
                "age": 23
            },
            {
                "name": "Ciencias",
                "lastname": "gomez",
                "age": 32
            }
        ]
        return department

    def create(self, info):
        print("Creando un departamento")
        student = Departments(info)
        return student.__dict__

    def show(self, id):
        print("Mostrando detalle de departamento por id:", id)
        student = {
              "name": "Ingenieria",
              "lastname": "garcia",
              "age": 23
            }
        return student

    def update(selfs, id, info):
        print("ACtualizando departamento por id: ", id)
        department = {
            "name": "Ingenieria",
            "lastname": "garcia",
            "age": 23
        }
        return department

    def delete(self, id):
        print("Eliminando departamento por id: ", id)

        return {"deleted_count": 1}



