# # 4.8_pandas_exercises

# When the instructions say to load a dataset, you can pass the name of the dataset as a string to the data function to load the dataset. You can also view the documentation for the data set by passing the show_doc keyword argument.
# 
# df = data('mpg') # load the dataset and store it in a variable
# 
# data('mpg', show_doc=True) # view the documentation for the dataset

get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib as plt
import numpy as np
import pandas as pd

from pydataset import data


# ## Use pandas to convert the following list to a numeric series:

prices = ['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23']

##OR pd.Series(prices)
df = pd.DataFrame(prices)

clean_numbers = df.replace('[\$,]', '', regex=True).astype(float)
clean_numbers

# ## Load the mpg dataset. Read the documentation for it, and use the data to answer these questions:

df = data('mpg') # load the dataset and store it in a variable
data('mpg', show_doc=True) # view the documentation for the dataset

# ## How many rows and columns are there?

df.shape #234 rows; 11 columns

# ## What are the data types?
df.dtypes

# ## Do any cars have better city mileage than highway mileage?

df[df.cty > df.hwy] #No, all cars have better hwy mileage
##OR (df.cty > df.hwy).any() --> True
##OR (df.cty > df.hwy).sum() --> 0 #number of trues

# ## Create a column named milelage_difference this column should contain the difference between highway and city milelage for each car.

df_new = df.assign(mileage_difference=df.hwy-df.cty)
df_new

# ## On average, which manufacturer has the best miles per gallon?

# df_avg_mpg = df.assign(avg_mpg=(df.hwy+df.cty)/2)
# df_avg_mpg.sort_values(by='avg_mpg', ascending=False)

df[['manufacturer', 'hwy', 'cty']].groupby('manufacturer').mean().sort_values(by='hwy', ascending=False)

# ## How many different manufacturers are there?

# df[['manufacturer']].groupby('manufacturer').count()
df.manufacturer.nunique()

# ## How many different models are there?

# df[['model']].groupby('model').count()
df.model.nunique()

# ## Do automatic or manual cars have better miles per gallon?

autos = df_avg_mpg[['trans','avg_mpg']].groupby('trans').mean().head(8)
manuals = df_avg_mpg[['trans','avg_mpg']].groupby('trans').mean().tail(2)

autos.mean()

manuals.mean()

# manuals have better miles per gallon

# ## Load the Mammals dataset. Read the documentation for it, and use the data to answer these questions:

df3 = data('Mammals') # load the dataset and store it in a variable
data('Mammals', show_doc=True) # view the documentation for the dataset

# ## How many rows and columns are there?

df3.shape #107 rows, 4 columns

# ## What are the data types?

df3.dtypes

# ## What is the the weight of the fastest animal?

df3.sort_values(by='speed').tail(1) #weight is 55.0
##OR df3.loc[mammals.speed.idxmax()]['weight']

# ## What is the overal percentage of specials?

total = df3.specials.count()
sum_true = df3.specials.sum()
specials_percent = ((sum_true/total)*100)
print('Overall percentage of specials is', round(specials_percent, 2), '%')

# ## How many animals are hoppers that are above the median speed? What percentage is this?

med_speed = df3.speed.median()
med_speed

df3.hoppers.sum()

df3_speed = df3[df3.speed > med_speed]
df3_speed.hoppers.sum()

hoppers=df3[df3.hoppers]
med_speed = df3.speed.median()
n_hoppers = hoppers[hoppers.speed > med_speed].shape[0]
percent_hoppers = n_hoppers / df3.shape[0]
print('There are {} hoppers, which is {:.2%} of the total'.format(n_hoppers, percent_hoppers))

# ## Getting data from SQL databases

# ## Create a function named get_db_url. It should accept a username, hostname, password, and database name and return a url formatted like in the examples in this lesson.

def get_db_url(user, host, password, db, driver='pymysql'):
    return f'mysql+{driver}://{user}:{password}@{host}/{db}'

# ## Use your function to obtain a connection to the employees database.

# import env
# url = get_db_url(env.username, env.hostname, env.password, db='employees')
# from sqlalchemy import create_engine
# connection = create_engine(url)

from sqlalchemy import create_engine
from env import user, password, host
url = 'mysql+pymysql://{}:{}@{}/employees'.format(user, password, host)
dbc = create_engine(url)

# ## Read the employees and titles tables into two separate data frames

emp = pd.read_sql('SELECT * FROM employees', dbc)
titles = pd.read_sql('SELECT * FROM titles', dbc)

# ## Visualize the number of employees with each title.

# emp_title = titles[['title', 'emp_no']].groupby('title').count()
# import matplotlib as plt
# emp_title.plot.bar(rot=45)

get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt

titles.title.value_counts()
titles.title.value_counts().plot()
titles.title.value_counts().plot.bar()
plt.xticks(rotation=30)
plt.subplots_adjust(left=0.15, right=0.95, top=0.95, bottom=0.2)
plt.show()

#only current employees
from datetime import datetime
datetime.now()
current_titles = titles[titles.to_date > datetime.now().date()]
current_titles.title.value_counts().plot.bar()

# ## Visualize how frequently employees change titles.

# how many titles does each employee have?
titles.emp_no.value_counts()
titles.emp_no.value_counts().value_counts()
titles.emp_no.value_counts().value_counts().plot.bar()

# titles.emp_no.value_counts().value_counts()

# ## Use the .join method to join the employees and titles data frames together

joined_df = emp.set_index('emp_no').join(titles.set_index('emp_no'))
joined_df

#OR employees_with_titles = employees.join(titles, on='emp_no', lsuffix='_emp', how='inner')
#inner join will exclude nulls

# ## For each title, find the hire date of the employee that was hired most recently with that title.

joined_df[['hire_date', 'title']].groupby('title').max()

# ## Explore the data from the chipotle database. Write a python script that will use this data to answer the following questions:

from sqlalchemy import create_engine
from env import user, password, host
url = 'mysql+pymysql://{}:{}@{}/chipotle'.format(user, password, host)
dbc = create_engine(url)

# ## What is the total price for each order?

chipotle = pd.read_sql('SELECT * FROM orders', dbc)

chipotle

clean_chipotle = chipotle.item_price.replace('[\$,]', '', regex=True).astype(float)

chipotle.item_price = clean_chipotle

chipotle

chipotle[['order_id', 'item_price']].groupby('order_id').sum()

#order_prices.describe() --> count, mean, std, min, max, 25%, 50%, 75%

# ## What are the most popular 3 items?

item_numbers = chipotle[['item_name', 'quantity']].groupby('item_name').sum()

item_numbers.sort_values(by='quantity', ascending=False).head(3)

# ## Which item has produced the most revenue?

revenue = ((chipotle.quantity * chipotle.item_price)/chipotle.quantity)

chipotle['revenue'] = revenue

rev_items = chipotle[['item_name', 'revenue']].groupby('item_name').sum()

rev_items.sort_values(by='revenue', ascending=False).head(1)
