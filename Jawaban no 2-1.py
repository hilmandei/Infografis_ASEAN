import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sqlalchemy


mydb = sqlalchemy.create_engine(
        'mysql+pymysql://hilmandei:rongjelek19@localhost:3306/world')


querry = '''SELECT country.Name as Negara_Asean, country.Population as Populasi_Negara, GNP, city.Name 
          as Ibukota, city.Population  FROM world.country
          join world.city 
          on country.Capital = 
          city.ID
          where country.Region like 'Southeast Asia'
          order by country.Name
          '''
df = pd.read_sql(querry, con=mydb)

y = df['Populasi_Negara']
x = df['Negara_Asean']
warna = 'rbkgymcmkcy'

plt.figure('Nomor 1')
plt.style.use('ggplot')
plt.title('Populasi Negara ASEAN')
plt.bar(x, y,  width= 0.9, color= warna)
plt.xlabel('Negara')
plt.ylabel('Populasi (x100jt jiwa)')
plt.xticks(rotation=90)


for i in range(len(x)):
    plt.text(i, y[i]+0.2, (y[i]), fontsize=8, horizontalalignment='center', verticalalignment='bottom')




plt.tight_layout()
plt.show()
