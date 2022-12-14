#from canjas import canjas as cj
import canjas as cj

arq = cj.read_csv('googleplaystore.csv')

arq.explore_data(0,3,rows_and_columns=True)

arq.delete_row(10472)

arq.explore_data(0,3,rows_and_columns=True)


data_english = arq.drop_duplicated()


data_english.explore_data(0,3,rows_and_columns=True)

data_clean = data_english.drop_non_english_rows("App")


data_clean.explore_data(0,3,rows_and_columns=True)

list_free = data_clean.group_by('Price', 0.0)

list_free.explore_data(0,3,rows_and_columns=True)

table = list_free.freq_table('Genres')

table.display_table()

table = list_free.freq_table('Genres', percent=True)

table.display_table()

table2 =list_free.freq_table('Installs')

table2.display_table()

table = list_free.freq_table('Category')

table.avarage('Installs',list_free,by='Category')

