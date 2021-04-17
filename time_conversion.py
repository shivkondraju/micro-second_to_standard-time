#Importing Pandas and Datetime
import pandas as pd
from datetime import datetime

#Reading Ticker data CSV file
data=pd.read_csv(r"tick_data.csv")
data.shape
data.head()

#Creating a copy
data_eg=data

#data_time is the new column to host the new updated time
data_eg['data_time']=data_eg['Date'].astype(str)+data_eg['Time'].astype(str)
data_eg['data time']=pd.to_datetime(data_eg['data_time'],format='%Y%m%d%H%M%S%f')
data_eg['data time']=data_eg['data time'].values.astype('datetime64[s]')

#Replacing data of Date column with the updated date time
data_eg['Date']=data_eg['data time']
