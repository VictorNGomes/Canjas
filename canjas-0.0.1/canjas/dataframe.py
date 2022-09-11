from csv import reader
from email import header

from requests import head

class Dataframe:
    def __init__(self,data, head) -> None:
        self.data = data
        if head:
            self.header = data[0]
            self.data = data[1:]

    def __str__(self) -> str:
        return f"{self.header} \n {self.data}"

    def explore_data(self, start, end, rows_and_columns=False):
        dataset_slice = self.data[start:end]    
        for row in dataset_slice:
            print(row)
            print('\n') 
        
        if rows_and_columns:
            print('Number of rows:', len(self.data))
            print('Number of columns:', len(self.data[0]))
        
        
        
