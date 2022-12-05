def calculate_frequencies(file_contents):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = [ "la", "y", "de", "en"]
    
    Contenido_Archivo = ""
    for index, caracter in enumerate(file_contents):
        if caracter.isalpha() == True or caracter.isspace():
            Contenido_Archivo += caracter #se van a
        
    Contenido_Archivo = Contenido_Archivo.split()
    file_without_uninteresting_words = [] 
    
    for palabra in Contenido_Archivo:
        if palabra.lower() not in uninteresting_words and palabra.isalpha() == True:
            file_without_uninteresting_words.append(palabra) 
            
    Contador_Diccionario = {}
    for palabra in file_without_uninteresting_words:
        if palabra.lower() not in Contador_Diccionario:
            Contador_Diccionario[palabra.lower()] = 1  
        else:
            Contador_Diccionario[palabra.lower()] += 1
    return Contador_Diccionario

print(calculate_frequencies("atari pal palche snes yo se quien te rompio y quien te coce la ley seca snes atari"))


    