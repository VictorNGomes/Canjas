import re
class Table:
    def __init__(self,dict_table) -> None:
        self.table = dict_table

    def display_table(self):
            table_display = []
            for key in self.table:
                key_val_as_tuple = (self.table[key], key)
                table_display.append(key_val_as_tuple)
                
            table_sorted = sorted(table_display, reverse = True)
            for entry in table_sorted:
                print(entry[1], ':', entry[0])

    def avarage(self,col,dataframe,by):
        for genre in self.table:
            total = 0
            len_genre = 0
            for app in dataframe.data:
                genre_app = app[dataframe.header.index(by)]
                if genre_app == genre:            
                    n_ratings = float(re.sub('[^0-9]', '', app[dataframe.header.index(col)]))
                    total += n_ratings
                    len_genre += 1
            avg_n_ratings = total / len_genre
            print(genre, ':', avg_n_ratings)
