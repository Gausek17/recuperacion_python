import csv
def read_data(fichero1, fichero2):
    
    with open(fichero1, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

    with open(fichero2, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)


if __name__ == "__main__":
    file1 = "stops_data.csv"
    file2 = "stops.csv"

    read_data(file1,file2)