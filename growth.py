import pandas as pd;
import sqlite3
import numpy as np;
import math

query = "select * from facts;"
conn=sqlite3.connect('factbook.db');
data=pd.read_sql_query(query,conn);
data=data.dropna(axis=0);

#print(data);
def population_estimate(x):
    pop_int=x['population'];
    rate=x['population_growth']/100;
    years=2050-2015;
    y=pop_int*np.exp(rate*years);
    return y;

data['2050_population']=data.apply(population_estimate,axis=1);
data=data.sort_values('2050_population',ascending=0);
print(data["name"].head(10));

# Extra part: which countries will lost population after 35 years?
print(data[data["2050_population"]<data["population"]])
print(data[data["population_growth"]<0])

# Which countries have the lowest/highest population density?
data['density']=data['population']/data['area'];
data=data.sort_values('density',ascending=1);
print(data["name"].head(10));

data=data.sort_values('migration_rate',ascending=0);
print(data["name"].head(10));
data=data.sort_values('migration_rate',ascending=1);
print(data["name"].head(10));
