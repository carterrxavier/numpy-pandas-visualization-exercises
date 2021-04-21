from env import user, password,host
import pandas as pd
import numpy as np

#1 Create a function named get_db_url. It should accept a username, 
# hostname, password, and database name and return a url connection
#  string formatted like in the example at the start of this lesson.
def get_db_url(user,password,host,db_name):
    return f'mysql+pymysql://{user}:{password}@{host}/{db_name}'


#2
url =  get_db_url(user,password,host, 'employees')

#3 a. sqlalchemy.exc.OperationalError:
  #b. qlalchemy.exc.ProgrammingError:


#4
# Read the employees 
# and titles tables into two separate DataFrames.
df_employees = pd.read_sql('select * from employees', url)
df_titles = pd.read_sql('select * from titles', url)

#5 rows ,columns
# df_employees.shape
# df_titles.shape

#6 summary stats
# df_employees.info()
# df_titles.info()


#7 
print(len(df_titles['title'].drop_duplicates()))

#8
print(df_titles['to_date'].max())

#9
print(df_titles['to_date'].min())
