def valid_text(texto):
    textstrip = texto.strip()
    textfinal = textstrip.replace(' ', '')
    resultado = False
    
    if textfinal.isalpha():
        resultado = True
    
    return resultado

# import isnumber

# def valid_text(texto):
#     if (isinstance(texto, ))
#     return isinstance(texto, str)