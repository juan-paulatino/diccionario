def calculate_frequencies(letra_cancion):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''                                         #se excluyen signos de puntuacion
    nointeresantes_palabras = [ "la", "y", "de", "en"]                     #se excluyeron los monosilabos: "la", "y", "de", "en"
    
    Contenido_Archivo = ""                                                                       #se genera una variable string
    for index, caracter in enumerate(letra_cancion):    #enumera la cantidad de caracteres e index en el archivo "letra_cancion"
        if caracter.isalpha() == True or caracter.isspace():       #metodos clave "isalpha" para palabra "isspace" para espacio  
            Contenido_Archivo += caracter                        #se van sumando las palabras en la variable "Contenido_Archivo"
        
    Contenido_Archivo = Contenido_Archivo.split()   #aqui se realiza la division de strings, porque era un string de gran tamano
    listado_palabras_buenas = []                                    #se crea un listado con la serie de strings generados arriba
    
    for palabra in Contenido_Archivo:                             #para cada uno de los elementos del string "contenido archivo"
        if palabra.lower() not in nointeresantes_palabras and palabra.isalpha() == True:                      #condicional clave
            listado_palabras_buenas.append(palabra)                             #se van sumando a la lista con el metodo append
            
    Contador_Diccionario = {}                                                                          #iniciamos el diccionario
    for palabra in listado_palabras_buenas:
        if palabra.lower() not in Contador_Diccionario:#excluimos las palabras que estan en en el archivo "de palabras no buenas"
            Contador_Diccionario[palabra.lower()] = 1                                     #agrega palabras nuevas al diccionario
        else:
            Contador_Diccionario[palabra.lower()] += 1                                          #suma uno a cada palabra repetida
    return Contador_Diccionario

print(calculate_frequencies("Real hasta la muerte, ¿oíste, bebé? Brr Aquí pensando en tu cuerpo (Cuerpo) Estas botella' están haciendo efecto (Uah; sí) Y en tu' foto' no comento (-mento) Pa' que nadie sepa de lo nuestro, no (Uah) Y ando en la Mercedes tinteá' de camino pa'llá (De camino pa'llá"))

#se divide en dos partes, la primera es generar un string gigantesco donde se puedan sumar 
#todas las palabras y espacios es decir los caracteres y 
#la segunda es generar el diccionario