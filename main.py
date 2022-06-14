
import csv
def read_data(fichero1, fichero2):
    diccionario={}

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
    return diccionario

def get_name_description(clave, diccionario):
    try:

        print("Name: ")
        print(diccionario[clave]['name'])
        print("Description: ")
        print(diccionario[clave]['description'])

    except IndexError as err:
         print("se ha producido una excepción: "+str(err))
    
    
    
   
if __name__ == "__main__":
    file1 = "stops_data.csv"
    file2 = "stops.csv"

    diccionario = read_data(file1,file2)
    get_name_description('1080', diccionario)
