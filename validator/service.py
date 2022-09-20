import os
import json
from curp import CURP, CURPValueError
from datetime import datetime
from crud_records.schema import *
from .utils import *



class Validator:
    def __init__(self, user:Record) -> None:
        self.nombre = user.nombre
        self.primer_apellido = user.primer_apellido
        self.segundo_apellido = user.segundo_apellido
        self.estado_de_nacimiento = user.estado_de_nacimiento
        self.curp = user.curp
        self.cp = user.cp
        self.rfc = user.rfc
        self.telefono = user.telefono
        self.fecha_de_nacimiento = user.fecha_de_nacimiento
        
        self.state_validator()
        self.curp_validator()
        self.cp_validator()
        self.rfc_validator()
        self.phone_validator()
        self.date_validation()
    
    def state_validator(self):
        with open("json/states.json", 'r',encoding="utf-8") as f:
            states = json.load(f)
            if self.estado_de_nacimiento in states.values():
                return ResponseModel(is_success = True,message = "Estado correcto")
            else:
                raise "Estado mal escrito"
            
    def curp_validator(self):
        longitud(self.curp, 18)
        try:
            c = CURP(self.curp)
            return ResponseModel(is_success = True,message = "CURP correcto")
        except CURPValueError as e:
            raise e
        
        
    def cp_validator(self):
        longitud(str(self.cp), 5)
        
    def rfc_validator(self):
        try:
            longitud(self.rfc, 13)
            if self.rfc[:-3] == self.curp[:10]:
                return ResponseModel(is_success = True,message = "RFC correcto")
        except Exception as ex:
            raise ex
            
    def phone_validator(self):
        longitud(str(self.telefono), 10)
        
    def date_validation(self):
        dt = datetime.strptime(self.fecha_de_nacimiento, '%d-%m-%Y')
        if dt.year < 1930 or dt.year > datetime.now().year:
            raise "Fechas incoherentes"
        

        

        
