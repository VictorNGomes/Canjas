from .dataframe import Dataframe
from csv import reader

def read_csv(file_path,header = True):
    opened_file = open(file_path)
    read_file = reader(opened_file)
    data = list(read_file)

    data = Dataframe(data,header)
    
    return data