
from lib2to3.pgen2 import token
from sqlalchemy.orm import Session
from auth.schema import Login, ResponseModel
from sqlalchemy.orm import Session
from crud_users.model import Directory as Model


#def auth_level(Fun): 
#    """_summary_
#    Valida que el usuario pertenece al nivel de acceso para la actividad que intenta ejecutar 
#    Agregamos más complejidad usando una clase que permite validar los niveles de acceso
#    """
#    def auth_decorator(*args, **kwargs):
#        my_json = Fun(*args, **kwargs)
#        return my_json
#    return auth_decorator

class auth_level(object):
    
    
    "Un decorador a partir de una clase"
    def __init__(self, level:list):
        self.level = level


    def __call__(self, Fun):
        def auth_decorator(*args, **kwargs):
            token = int(args[-1][-1])
            if token in self.level:
                f = Fun(*args, **kwargs)
                return f
            else:
                raise NotADirectoryError
        return auth_decorator


async def validate_user(login:Login,db:Session) -> ResponseModel:
    try:
        user = db.query(Model).filter(Model.user == login.user).first()
        if user.password == login.password:
            return ResponseModel(
                is_succes = True,
                result = user.level,
                token= f"lvl_{user.level}",
                message="correct")
        else:
            raise "Contraseña incorrecta"
    except:
        return ResponseModel(is_succes = False,message = "contraseña incorrecta")


async def generate_token(login:Login,db:Session)-> ResponseModel:
    result = await validate_user(login,db)
    return result



