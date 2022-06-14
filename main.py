
import csv
def read_data(fichero1, fichero2):
    
    with open(fichero1, 'r') as file:
        reader = csv.reader(file)
        diccionario={}
        for row in reader:
            diccionario[row[0]]=row[2]
            print(row)


    
   

if __name__ == "__main__":
    file1 = "stops_data.csv"
    file2 = "stops.csv"

    read_data(file1,file2)