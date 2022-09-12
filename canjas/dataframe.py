from csv import reader
from email import header
from numpy import dtype

from requests import head

class Dataframe:
    def __init__(self,data, head = True) -> None:
        self._head = head
        self.data = data
        self.n_rows = len(self.data) - head
        self.n_columns = len(self.data[0])
        if head:
            self.header = data[0]
            self.data = data[1:]

    def __str__(self) -> str:
        if self.head:
            return f"{self.header} \n {self.data}"
        return f"{self.data}"

    def _get_head(self):
        return self.header

    def explore_data(self, start = 0, end = 5, rows_and_columns=False):
        """
        Explora os dados determinas nos paramtros. 
        """
        dataset_slice = self.data[start:end]    
        for row in dataset_slice:
            print(row)
            print('\n') 
        
        if rows_and_columns:
            print('Number of rows:', self.n_rows)
            print('Number of columns:', self.n_columns)
        
    def delete_row(self,index):
        del self.data[index]
        
    def rows_with(self,label:str)->list:
        list_of_content = []
        for each_row in self.data:
            if label in each_row:
                list_of_content.append(each_row)
        return Dataframe(list_of_content,False)

    def duplicated_elements(self,element)->tuple:
        duplicate_apps = []
        unique_apps = []
        duplicate_apps.append(self.header)  
        unique_apps.append(self.header)

        for each_row in self.data:
            name = each_row[self.header.index(element)]
            if name in unique_apps:
                duplicate_apps.append(name)
            else:
                unique_apps.append(name)

        return (Dataframe(duplicate_apps), Dataframe(unique_apps))

    def drop_duplicated(self,col=None):
        

        i_max = {}

        for item in self.data:
            name = item[0]
            n_reviews = float(item[3])
            
            if name in i_max and i_max[name] < n_reviews:
                i_max[name] = n_reviews
                
            elif name not in i_max:
                i_max[name] = n_reviews

        data_clean = []
        already_added = []

        data_clean.append(self.header)

        for app in self.data:
            name = app[0]
            n_reviews = float(app[3])
            
            if (i_max[name] == n_reviews) and (name not in already_added):
                data_clean.append(app)
                already_added.append(name)

        
        return Dataframe(data_clean)
             
    def is_english(self,row):
        non_ascii = 0
        string = row[self.header.index(self._row_for_drop)]
        for character in string:
            if ord(character) > 127:
                non_ascii += 1
            
        if non_ascii > 3:
            return False
        else:
            return True
    
    def drop_non_english_rows(self,index_row:str):
        self._row_for_drop = index_row
        data = filter(self.is_english,self.data) 

        data_l = list(data)
        
        data_l.insert(0 ,self.header)
        
        return Dataframe(data_l)

    def group_by():
        pass




