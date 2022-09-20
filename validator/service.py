from crud_records.schema import User
from .utils import *

class Validator:
    def __init__(self, user:User) -> None:
        self.nombre = user.nombre
        self.primer_apellido = user.primer_apellido
        self.segundo_apellido = user.segundo_apellido
        self.estado_de_nacimiento = user.estado_de_nacimiento
        self.curp = user.curp
        self.cp = user.cp
        self.rfc = user.rfc
        self.telefono = user.telefono
        self.fecha_de_nacimiento = user.fecha_de_nacimiento

    def curp_validator(self):
        longitud(self.curp, 18)
        
    def cp_validator(self):
        longitud(self.cp, 5)
        
    def rfc_validator(self):
        longitud(self.rfc, 13)
    
    def phone_validator(self):
        longitud(self.telefono, 10)
        
    def date_validator(self):
        longitud(self.fecha_de_nacimiento, 10)
        

        
