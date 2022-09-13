 # Project: Profitable App Profiles for the App Store and Google Play Markets
  Esta biblioteca é a Canjas na qual impleneta rafotoração da solução dada do pelo modulo Python for Data Engineering: Fundamentals Part II do curso de Data Engenier da plataforma Dataquest. Para a refatoração, foram aplicados os paradigmas de programação orientada a objetos. Obs: Muitas das soluções foram realizdas para casos particulares do problema proposto.
  
 
 
 
 # Instalação
 git clone https://github.com/VictorNGomes/Canjas.git
 cd canjas
 
 # Abrindo CSV em explorando dados
 No projeto está contido dois arquivos do formato csv para realizar as manipulações
 ```python
 import canjas as cj
arq = cj.read_csv('googleplaystore.csv')

arq.explore_data(0,3,rows_and_columns=True)
 ```
 
 

 
 
 
