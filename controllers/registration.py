

class RegistrationController:
    def index(self):
        print("Creando controlador de registros")
        register = [
            {
                "registro": "brayan"
            },
            {
               "registro": "antonio"
            }
        ]
        return register
