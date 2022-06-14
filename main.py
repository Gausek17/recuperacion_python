
import csv
##----------------------------------------------------------------------------------------------------------------------
##----------------------------------------------------------------------------------------------------------------------
##fichero1,fichero2->read_data()->diccionario
def read_data(fichero1, fichero2):
    ##Declaramos el diccionario vacio
    diccionario={}
    ##Abrimos los ficheros y vamos guardando las variables que nos interesan
    with open(fichero1, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
              with open(fichero2, 'r') as file2:
                reader2 = csv.reader(file2)
                for row2 in reader2:
                    if(row[0]==row2[0]):
                        diccionario[row[0]]={
                            'description':row2[3],
                            'id':row2[1],
                            'lat':row[4],
                            'lon':row[5],
                            'name':row2[2]}

    print("---Diccionario----")
    print(diccionario)
    ##Devolvemos el diccionario
    return diccionario

##----------------------------------------------------------------------------------------------------------------------
##----------------------------------------------------------------------------------------------------------------------
##Clave,diccionario->get_name_desciption()->{'name':'','description':''}
def get_name_description(clave, diccionario):
    ##Booleano para saber si hemos encontrado el elemento
    existe = False
    
    ##Recorremos el diccionario
    for element in diccionario:
        if(element == clave):
            ##Si existe el elemento, lo guardamos
            existe = True
    
    ##Devolvemos el nombre y la descripcion
    if(existe):
        print("Name: ")
        print(diccionario[clave]['name'])
        print("Description: ")
        print(diccionario[clave]['description'])
    ##Si no existe, devolvemos un mensaje
    else:
        raise ValueError("No se encontró esa clave")
    
##----------------------------------------------------------------------------------------------------------------------
##----------------------------------------------------------------------------------------------------------------------
##Longitud,diccionario->search_by_lon()->id
def search_by_lon(longitud_a_buscar,diccionario):
    ##Declaramos booleano e id inicial
    existe = False
    id = -1
    ##Si no es de tipo float:
    if(not isinstance(longitud_a_buscar, float)):
        raise ValueError("No es de tipo float")
    ##Si lo es:
    else:
        ##Recorremos el diccionario y guardamos su id
        for element in diccionario:
            if(diccionario[element]['lon'] == longitud_a_buscar):
                existe = True
                id = element
        ##Cuando existe imprimimos los datos de su id
        if(existe):
            print("Name: ")
            print(diccionario[id]['name'])
            print("Description: ")
            print(diccionario[id]['description'])
            ##Devolvemos su id
            return id
        ##Si no está mostramos el mensaje de error
        else:
            raise ValueError("No se ha encontrado la clave")




##--------------------------------MAIN-----------------------------------------------------
###############################################################################
if __name__ == "__main__":
    ##Declaramos los archivos a leer
    file1 = "stops_data.csv"
    file2 = "stops.csv"
    ##Leemos los archivos
    diccionario = read_data(file1,file2)
    try:
        ##PRUEBAS SEARCH BY LON
        lon = 728257.03
        id = search_by_lon(lon, diccionario)
        print("Id encontrada: "+id)
        ##PRUEBAS GET NAME DESCRIPTION
        get_name_description('1080', diccionario)
        get_name_description('100800', diccionario)
    except ValueError as err:
        print("Se ha producido un error:"+str(err))
