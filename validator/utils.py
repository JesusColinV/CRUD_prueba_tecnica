def longitud(txt:str,lg:int):
    """_validador de longitud_

    Args:
        txt (str): _texto_
        lg (int): _cantidad que debe medir el texto_

    Raises:
        ValueError: _levanta un error cuando no se cumple_
    """
    if len(txt) != lg:
        raise ValueError