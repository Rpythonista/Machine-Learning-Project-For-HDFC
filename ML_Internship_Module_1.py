#!/usr/bin/env python
# coding: utf-8

# # MODULE 1

# # Problem statement 1.1

# Import the csv file of the stock you have been allotted using 'pd.read_csv()' function into a dataframe.
# Shares of a company can be offered in more than one category. The category of a stock is indicated in the ‘Series’ column. If the csv file has data on more than one category, the ‘Date’ column will have repeating values. To avoid repetitions in the date, remove all the rows where 'Series' column is NOT 'EQ'.
# Analyze and understand each column properly.
# You'd find the head(), tail() and describe() functions to be immensely useful for exploration. You're free to carry out any other exploration of your own.

# In[1]:


#Importing libraries
import pandas as pd
import numpy as np
import datetime


# In[2]:


#Reading data
raw_data=pd.read_csv("HDFC.csv")
raw_data.head() #use to display initial few rows of dataset


# In[3]:


raw_data.tail() #use to display last few rows of dataset


# In[4]:


raw_data.describe() #use to display description and features of dataset


# In[5]:


data = raw_data[raw_data.Series == 'EQ'] #drops the W2 entries from the dataset
data


# # Problem statement 1.2

# Calculate the maximum, minimum and mean price for the last 90 days. (price=Closing Price unless stated otherwise)

# In[6]:


data.tail(90)['Close Price'].max() #Calculates maximum price for last 30 days.


# In[7]:


data.tail(90)['Close Price'].min() #Calculates minimum price for last 30 days.


# In[8]:


data.tail(90)['Close Price'].mean() #Calculates mean price for last 30 days.


# # Problem statement 1.3

# Analyse the data types for each column of the dataframe. Pandas knows how to deal with dates in an intelligent manner. But to make use of Pandas functionality for dates, you need to ensure that the column is of type 'datetime64(ns)'. Change the date column from 'object' type to 'datetime64(ns)' for future convenience. See what happens if you subtract the minimum value of the date column from the maximum value.

# In[9]:


data.dtypes


# In[10]:


data['Date'] = data['Date'].astype('datetime64[ns]')


# In[11]:


data.dtypes


# In[12]:


max_date = max(data["Date"]) #Calculate max date
min_date = min(data["Date"]) #calculate min date
sub_date= max_date-min_date #Subtraction of min date from max date
sub_date


# # Problem Statement 1.4

# In a separate array , calculate the monthwise VWAP (Volume Weighted Average Price ) of the stock.
# ( VWAP = sum(price*volume)/sum(volume) )
# {Hint : Create a new dataframe column ‘Month’. The values for this column can be derived from the ‘Date” column by using appropriate pandas functions. Similarly, create a column ‘Year’ and initialize it. Then use the 'groupby()' function by month and year. Finally, calculate the vwap value for each month (i.e. for each group created).

# In[13]:


data['Month'] = pd.DatetimeIndex(data['Date']).month #A new dataframe column ‘Month’.
data['Year'] = pd.DatetimeIndex(data['Date']).year #A new dataframe column ‘Year’.
#Calculation of VWAP value
data['VWAP'] = (np.cumsum(data['Close Price'] * data['Total Traded Quantity'])/(np.cumsum(data['Total Traded Quantity'])))
data_vwap = data[['Month','Year','VWAP']]
#Data grouping
group = data_vwap.groupby(['Month','Year'])
group.first()


# # Problem Statement 1.5

# Write a function to calculate the average price over the last N days of the stock price data where N is a user defined parameter. Write a second function to calculate the profit/loss percentage over the last N days.
# Calculate the average price AND the profit/loss percentages over the course of last -
# 1 week, 2 weeks, 1 month, 3 months, 6 months and 1 year.
# {Note : Profit/Loss percentage between N days is the percentage change between the closing prices of the 2 days }

# In[14]:


def avgerage_price(N): #N refers to number of days.
    return (data['Average Price'].tail(N).sum())/N
print("Average prices for last N days are as follows:")
print("Last 1 week",avgerage_price(5))
print("Last 2 weeks",avgerage_price(10))
print("Last 1 month",avgerage_price(20))
print("Last 3 months",avgerage_price(60))
print("Last 6 months",avgerage_price(120))
print("Last 1 year",avgerage_price(240))


# In[15]:


data['Close Price'].tail(4)
data['Close Price'].tail(4).iloc[3]


# In[16]:


print("Profit/Loss % for N days are as follows:")
def profit_loss(N): #N refers to number of days.
    difference = (data['Close Price'].tail(N).iloc[N-1] - data['Close Price'].tail(N).iloc[0])
    if difference < 0 :
        loss = -(difference)
        loss_percentage = (loss/data['Close Price'].tail(N).iloc[N-1])*100
        return loss_percentage
    if difference > 0 :
        profit = difference
        profit_percentage = (profit/data['Close Price'].tail(N).iloc[N-1])*100
        return profit_percentage
print("Loss/Profit percentage for last N days are as follows:")
print("Last 1 week",profit_loss(5))
print("Last 2 weeks",profit_loss(10))
print("Last 1 month",profit_loss(20))
print("Last 3 months",profit_loss(60))
print("Last 6 months",profit_loss(120))
print("Last 1 year",profit_loss(240))


# # Problem Statement 1.6

# Add a column 'Day_Perc_Change' where the values are the daily change in percentages i.e. the percentage change between 2 consecutive day's closing prices. Instead of using the basic mathematical formula for computing the same, use 'pct_change()' function provided by Pandas for dataframes. You will note that the first entry of the column will have a ‘Nan’ value. Why does this happen? Either remove the first row, or set the entry to 0 before proceeding.

# In[17]:


data['Day_Perc_Change'] = data['Close Price'].pct_change().fillna(0) #Adds a column Day_Perc_Change.
data


# # Problem Statement 1.7

# Add another column 'Trend' whose values are:
# 1. 'Slight or No change' for 'Day_Perc_Change' in between -0.5 and 0.5
# 2. 'Slight positive' for 'Day_Perc_Change' in between 0.5 and 1
# 3. 'Slight negative' for 'Day_Perc_Change' in between -0.5 and -1
# 4. 'Positive' for 'Day_Perc_Change' in between 1 and 3
# 5. 'Negative' for 'Day_Perc_Change' in between -1 and -3
# 6. 'Among top gainers' for 'Day_Perc_Change' in between 3 and 7
# 7. 'Among top losers' for 'Day_Perc_Change' in between -3 and -7
# 8. 'Bull run' for 'Day_Perc_Change' >7
# 9. 'Bear drop' for 'Day_Perc_Change' <-7

# In[18]:


if ((data['Day_Perc_Change'] >= -0.5) & (data['Day_Perc_Change'] <= 0.5)).all():
    data['Trend'] = 'Slight or No change'
if ((data['Day_Perc_Change'] >= 0.5) & (data['Day_Perc_Change'] <= 1)).all():
    data['Trend'] = 'Slight positive'
if ((data['Day_Perc_Change'] <= -0.5) & (data['Day_Perc_Change'] >= -1)).all():
    data['Trend'] = 'Slight negative'
if ((data['Day_Perc_Change'] >= 1) & (data['Day_Perc_Change'] <= 3)).all():
    data['Trend'] = 'Positive' 
if ((data['Day_Perc_Change'] <= -1) & (data['Day_Perc_Change'] >= -3)).all():
    data['Trend'] = 'Negative'
if ((data['Day_Perc_Change'] >= 3) & (data['Day_Perc_Change'] <= 7)).all():
    data['Trend'] = 'Among top gainers'
if ((data['Day_Perc_Change'] <= -3) & (data['Day_Perc_Change'] >= -7)).all():
    data['Trend'] = 'Among top losers'
if (data['Day_Perc_Change'] > 7).all():
    data['Trend'] = 'Bull run' 
if (data['Day_Perc_Change'] < -7).all():
    data['Trend'] = 'Bear drop' 
data


# # Problem Statement 1.8

# Find the average and median values of the column 'Total Traded Quantity' for each of the types of 'Trend'.
# {Hint : use 'groupby()' on the 'Trend' column and then calculate the average and median values of the column 'Total Traded Quantity'}

# In[19]:


data.groupby(data.Trend).mean()['Total Traded Quantity'] #Calculation of mean value for Total Traded Quantity
data.groupby(data.Trend).median()['Total Traded Quantity'] #Calculation of median value for Total Traded Quantity


# # Problem Statement 1.9

# SAVE the dataframe with the additional columns computed as a csv file week2.csv. In Module 2, you are going to get familiar with matplotlib, the python module which is used to visualize data.

# In[20]:


data.to_csv('week2.csv') #Save the dataset.

