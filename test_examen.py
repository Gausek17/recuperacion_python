import main as f
import pytest
def test_search_by_lon():
    file1 = "stops_data.csv"
    file2 = "stops.csv"

    diccionario = f.read_data(file1,file2)
    assert f.search_by_lon(725915.428, diccionario) == '1060'



def test_excepction_get_name_description():
    with pytest.raises(ValueError) as exc:
        file1 = "stops_data.csv"
        file2 = "stops.csv"
        diccionario = f.read_data(file1,file2)

        f.get_name_description('108585', diccionario)        

    assert "No se ha encontrado la clave" == str(exc.value)