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

labels = x


fig1, ax1 = plt.subplots(num='Soal no 2')
ax1.pie(y, labels=labels, autopct='%1.1f%%',
        shadow=False, startangle=0)

plt.title('Persentase Penduduk Asean', pad=30, fontsize=15)

ax1.axis('equal')

plt.show()
