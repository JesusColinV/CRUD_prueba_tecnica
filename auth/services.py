
from sqlalchemy.orm import Session
from auth.schema import Login, ResponseModel
from sqlalchemy.orm import Session
from crud_users.model import Directory as Model

def auth_level(Fun):
    """_summary_
    Valida que el usuario pertenece al nivel de acceso para la actividad que intenta ejecutar  
    Args:
        tkn: es un token temporal que determina que este usuario puede realizar dicha acción
    """
    def auth_decorator(*args, **kwargs):
        my_json = Fun(*args, **kwargs)
        return my_json
    return auth_decorator

def validate_user(login:Login,db:Session) -> ResponseModel:
    #return login
    user = db.query(Model).filter(Model.user == login).fetchall()
    if user.password == login.password:
        return ResponseModel(True,login.user,"correct")
    else:
        return ResponseModel(False,"correct")

def generate_token(login:Login,db:Session)-> ResponseModel:
    result = validate_user(login,db)
    if result.is_success:
        return ResponseModel(True,result.result,result.message)
    else:
        return ResponseModel(False,result.message)



