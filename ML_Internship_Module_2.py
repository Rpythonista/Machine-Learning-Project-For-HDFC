#!/usr/bin/env python
# coding: utf-8

# # Module 2 (Data visualization and Technical Analysis)

# # Problem Statement 2.1
# Load the week2.csv file into a dataframe. What is the type of the Date column? Make sure it is of type datetime64. Convert the Date column to the index of the dataframe.
# Plot the closing price of each of the days for the entire time frame to get an idea of what the general outlook of the stock is.
# 1. Look out for drastic changes in this stock, you have the exact date when these took place, try to fetch the news for this day of this stock
# 2. This would be helpful if we are to train our model to take NLP inputs.

# In[2]:


#import libraries
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from functools import partial
import matplotlib.pyplot as plt


# In[3]:


data = pd.read_csv("week2.csv")#loading week2.csv file
del data['Unnamed: 0']
raw_data = data 
data.head()#loading first few lines of week2.csv file


# In[4]:


data['Date'] = data['Date'].astype('datetime64[ns]')
data.Date.dtype


# In[5]:


data.set_index('Date', inplace = True)
data


# In[6]:


get_ipython().run_line_magic('matplotlib', 'inline')
data['Close Price'].plot(label='HDFC',figsize=(20,10),title="Closeing Price with respect to Date")
plt.legend()


# In[7]:


data['Close Price'].diff().abs().sort_values(ascending= False)


# In[8]:


import bs4
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests 
# On finding dates, the news were availabe for following dates. 
# 1. Jan 15, 2018
# 2. Jul 27, 2018
# 3. Oct 19, 2018  

news_url_15_01 = 'https://www.moneycontrol.com/news/business/stocks/buy-hdfc-bank-says-mitessh-thakkar-2483539.html'
news = requests.get(news_url_15_01) 
#Printing news content 
soup = BeautifulSoup(news.content,"html.parser")
News_title = soup.find('div',class_ = 'article_box')
News_subhead = soup.find('div',class_ = 'brk_wraper clearfix')
News_body = soup.find('div',class_ = 'arti-flow')
print("News for Jan 15, 2018")
print('\n')
print("Title:")
print (News_title.h1.text)
print('\n')
print("Subject:")
print (News_subhead.h2.text)
print('\n')
print("Report:")
for p in News_body:
    Report = soup.find('p').text
print(Report)
print('\n')
print("///////////////////////////////////////////////////////////////////////////////////////////////////////////////")
print('\n')
news_url_27_07 = 'https://www.moneycontrol.com/news/business/companies/ihh-open-offer-for-fortis-to-commence-on-sept-7-2773941.html'
news = requests.get(news_url_27_07) 
#Printing news content 
soup = BeautifulSoup(news.content,"html.parser")
News_title = soup.find('div',class_ = 'article_box')
News_subhead = soup.find('div',class_ = 'brk_wraper clearfix')
News_body = soup.find('div',class_ = 'arti-flow')
print("News for Jul 27, 2018")
print('\n')
print("Title:")
print (News_title.h1.text)
print('\n')
print("Subject:")
print (News_subhead.h2.text)
print('\n')
print("Report:")
for p in News_body:
    Report = soup.find('p').text
print(Report)
print('\n')
print("///////////////////////////////////////////////////////////////////////////////////////////////////////////////")
print('\n')
news_url_19_10 = 'https://www.moneycontrol.com/news/business/markets/hdfc-bank-q2-earnings-preview-watch-out-for-these-5-key-factors-3065021.html'
news = requests.get(news_url_19_10) 
#Printing news content 
soup = BeautifulSoup(news.content,"html.parser")
News_title = soup.find('div',class_ = 'article_box')
News_subhead = soup.find('div',class_ = 'brk_wraper clearfix')
News_body = soup.find('div',class_ = 'arti-flow')
print("News for Oct 19, 2018")
print('\n')
print("Title:")
print (News_title.h1.text)
print('\n')
print("Subject:")
print (News_subhead.h2.text)
print('\n')
print("Report:")
for p in News_body:
    Report = soup.find('p').text
print(Report)
print('\n')


# # Problem Statement 2.2
# A stem plot is a discrete series plot, ideal for plotting daywise data. It can be plotted using the plt.stem() function.
# 
# Display a stem plot of the daily change in of the stock price in percentage. This column was calculated in module 1 and should be already available in week2.csv. Observe whenever there's a large change.

# In[9]:


import matplotlib.pyplot as plt 
data = pd.read_csv("week2.csv")
plt.figure(figsize=(20,10))
plt.stem(data.Date,data['Day_Perc_Change'])


# # Problem Statement 2.3 
# 
# Plot the daily volumes as well and compare the percentage stem plot to it. Document your analysis of the relationship between volume and daily percentage change.

# In[10]:


plt.figure(figsize=(20,10))
plt.stem(data.Date,data['Total Traded Quantity'])


# In[11]:


plt.figure(figsize=(20,10))
plt.stem(data.Date,data['Total Traded Quantity'])
plt.show()


# In[12]:


plt.figure(figsize=(20,10))
plt.stem(data.Date,data['Day_Perc_Change'])
plt.show()


# In[13]:


plt.figure(figsize=(20,10))
plt.stem(data['Day_Perc_Change'],data['Total Traded Quantity'])
plt.show()


# In[14]:


plt.figure(figsize=(20,10))
plt.stem(data['Total Traded Quantity'],data['Day_Perc_Change'])
plt.show()


# In[15]:


plt.figure(figsize=(20,10))
plt.plot(data['Day_Perc_Change'],data['Total Traded Quantity'])
plt.show()


# In[16]:


plt.figure(figsize=(20,10))
plt.plot(data['Total Traded Quantity'],data['Day_Perc_Change'])
plt.show()


# # Problem Statement 2.4
# 
# We had created a Trend column in module 1. We want to see how often each Trend type occurs. This can be seen as a pie chart, with each sector representing the percentage of days each trend occurs. Plot a pie chart for all the 'Trend' to know about relative frequency of each trend. You can use the groupby function with the trend column to group all days with the same trend into a single group before plotting the pie chart. From the grouped data, create a BAR plot of average & median values of the 'Total Traded Quantity' by Trend type.

# In[17]:


import matplotlib.pyplot as plt
from collections import Counter

Trendsare = ['Postive','Negative','Breakout Bull','Breakout Bear','Among top losers','Among top gainers','Slight or No Change','Slight Positive','Slight Negative']
Trend_to_list = data['Trend'].tolist()
counts = Counter(Trend_to_list)
counts


# In[18]:


# So we only have 1 trend so there will be only 1 color pie chart 
counter = [494]
labels= ['Slight or No change']
colors = ['r']
plt.figure(figsize=(20,10))
plt.pie(counter, labels=labels,colors=colors,startangle=90, autopct='%.1f%%')
plt.show()


# In[19]:


# We will find the average of each trend type
# here we only have 1 trend which is Slight or No change hence only 1 bar graph
import matplotlib.pyplot as plt

gk = data.groupby(['Trend'])['Total Traded Quantity']
gk.describe()


# In[20]:


plt.figure(figsize=(20,10))
data.groupby(['Trend'])['Total Traded Quantity'].mean().plot.bar()


# In[21]:


plt.figure(figsize=(20,10))
data.groupby(['Trend'])['Total Traded Quantity'].median().plot.bar()


# # Problem Statement 2.5
# 
# Plot the daily return (percentage) distribution as a histogram.
# Histogram analysis is one of the most fundamental methods of exploratory data analysis. In this case, it'd return a frequency plot of various values of percentage changes .

# In[22]:


plt.figure(figsize=(20,10))
plt.hist(data['Day_Perc_Change'])
plt.show()


# # Problem Statement 2.6
# 
# We next want to analyse how the behaviour of different stocks are correlated. The correlation is performed on the percentage change of the stock price instead of the stock price. 
# 
# Load any 5 stocks of your choice into 5 dataframes. Retain only rows for which ‘Series’ column has value ‘EQ’. Create a single dataframe which contains the ‘Closing Price’ of each stock. This dataframe should hence have five columns. Rename each column to the name of the stock that is contained in the column. Create a new dataframe which is a percentage change of the values in the previous dataframe. Drop Nan’s from this dataframe.
# Using seaborn, analyse the correlation between the percentage changes in the five stocks. This is extremely useful for a fund manager to design a diversified portfolio. To know more, check out these resources on correlation and diversification. 

# In[23]:


import pandas as pd
mindtree_data = pd.read_csv('mindtree.csv')
tcs_data = pd.read_csv('tcs.csv')
itc_data = pd.read_csv('itc.csv')
reliance_data = pd.read_csv('reliance.csv')
voltas_data = pd.read_csv('voltas.csv')


# In[24]:


mindtree_data


# In[25]:


tcs_data


# In[26]:


itc_data


# In[27]:


reliance_data


# In[28]:


voltas_data


# In[29]:


mindtree = mindtree_data[mindtree_data.Series == 'EQ']
mindtree


# In[30]:


tcs = tcs_data[tcs_data.Series == 'EQ']
tcs


# In[31]:


itc = itc_data[itc_data.Series == 'EQ']
itc


# In[32]:


reliance = reliance_data[reliance_data.Series == 'EQ']
reliance


# In[33]:


voltas = voltas_data[voltas_data.Series == 'EQ']
voltas


# In[34]:


import pandas as pd

columns = ['Mindtree','TCS','ITC','Reliance','Voltas']
close_prices_dataFrame = pd.DataFrame(columns = columns)
close_prices_dataFrame['Mindtree'] = mindtree['Close Price']
close_prices_dataFrame['TCS'] = tcs['Close Price']
close_prices_dataFrame['ITC'] = itc['Close Price']
close_prices_dataFrame['Reliance'] = reliance['Close Price']
close_prices_dataFrame['Voltas'] = voltas['Close Price']
close_prices_dataFrame.dropna()


# In[35]:


pct_change_dataFrame = close_prices_dataFrame.pct_change().fillna(0)
pct_change_dataFrame.dropna()


# In[36]:


import seaborn as sns

sns.set(color_codes=True)
sns.pairplot(pct_change_dataFrame)


# # Problem Statement 2.7
# 
# Volatility is the change in variance in the returns of a stock over a specific period of time.Do give the following documentation on volatility a read.
# You have already calculated the percentage changes in several stock prices. Calculate the 7 day rolling average of the percentage change of any of the stock prices, then compute the standard deviation (which is the square root of the variance) and plot the values.
# Note: pandas provides a rolling() function for dataframes and a std() function also which you can use.

# In[37]:


import matplotlib.pyplot as plt
rolling_avg_mindtree = pct_change_dataFrame['Mindtree'].rolling(7).mean()
rolling_avg_mindtree


# In[38]:


sd_mindtree = rolling_avg_mindtree.fillna(0).std()
sd_mindtree


# In[39]:


import pandas as pd
crrDate = pd.to_datetime(mindtree['Date'])
crrLis = crrDate.tolist()
plt.figure(figsize=(20,10))
plt.plot(crrLis,rolling_avg_mindtree.fillna(0).tolist())
plt.show()


# # Problem Statement 2.8
# 
# Calculate the volatility for the Nifty index and compare the 2. This leads us to a useful indicator known as 'Beta' ( We'll be covering this in length in Module 3)

# In[40]:


nifty_load = pd.read_csv('NIFTY50.csv')
nifty_load


# In[42]:


nifty_close_price = nifty_load['Close']
nifty_change = nifty_close_price.pct_change().fillna(0).rolling(7).mean().fillna(0)
niftyDate = pd.to_datetime(nifty_load['Date'])
niftyDate = niftyDate.tolist()
plt.figure(figsize=(20,10))

tcs_Date = pd.to_datetime(tcs['Date'])
tcsLis = tcs_Date.tolist()
tcs_close_price = tcs['Close Price']
tcs_change = tcs_close_price.pct_change().fillna(0).rolling(7).mean().fillna(0)
plt.figure(figsize=(20,10))
plt.plot(tcsLis,rolling_avg_mindtree.fillna(0).tolist())

plt.title("Volatility of NIFTY with respect to TCS and Mindtree")
plt.plot(niftyDate,nifty_change.tolist(),label = 'nifty')
plt.plot(crrLis,rolling_avg_mindtree.fillna(0).tolist(),label = 'Mindtree')
plt.plot(tcsLis,tcs_change,label = 'TCS')
plt.legend(loc='upper left')
plt.show()


# # Problem Statement 2.9
# 
# Trade Calls - Using Simple Moving Averages. Study about moving averages here.Plot the 21 day and 34 day Moving average with the average price and decide a Call ! Call should be buy whenever the smaller moving average (21) crosses over longer moving average (34) AND the call should be sell whenever smaller moving average crosses under longer moving average. One of the most widely used technical indicators.

# In[43]:


# we will use tcs stocks for applying buy/sell signals
plt.figure(figsize=(20,10))
plt.plot(tcsLis,tcs_change,label = 'tcs')
plt.legend(loc='upper left')
plt.show()


# In[46]:


import numpy as np
#making short and long signals
short_window = 21
long_window = 34

signals = pd.DataFrame(index=tcs.index)
signals['signal'] = 0.0

#SMA of Short Window
signals['short_mavg'] = tcs['Close Price'].rolling(window=short_window, min_periods=1,center=False).mean()

#SMA of Long Window
signals['long_mavg'] = tcs['Close Price'].rolling(window=long_window,min_periods=1, center=False).mean()

#Create signals
signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:] > signals['long_mavg'][short_window:], 1.0,0.0)

#Generate trading orders
signals['positions'] = signals['signal'].diff()
print(signals)

# tcs['Date'] = pd.to_datetime(tcs['Date'])
# tcs.set_index('Date', inplace=True)
# tcs


# In[47]:


# Initialize the plot figure
fig = plt.figure(figsize=(20,15))

#Add a subplot and label for y-axis
ax1 = fig.add_subplot(111, ylabel='Price')

#Plot the closing price
tcs['Close Price'].plot(ax=ax1, color='black', lw=2.)

#plot the short and long moving averages
signals[['short_mavg', 'long_mavg']].plot(ax=ax1, lw=2.)

#Plot the buy signals
ax1.plot(signals.loc[signals.positions == 1.0].index, signals.short_mavg[signals.positions == 1.0], '^' , markersize=20,color='g')

#Plot the sell signals
ax1.plot(signals.loc[signals.positions == -1.0].index, signals.short_mavg[signals.positions == -1.0], 'v' , markersize=20,color='r')

plt.show()


# # Problem Statement 2.10 
# 
# Trade Calls - Using Bollinger Bands
# Plot the bollinger bands for this stock - the duration of 14 days and 2 standard deviations away from the average The bollinger bands comprise the following data points- The 14 day rolling mean of the closing price (we call it the average) Upper band which is the rolling mean + 2 standard deviations away from the average. Lower band which is the rolling mean - 2 standard deviations away from the average. Average Daily stock price. Bollinger bands are extremely reliable , with a 95% accuracy at 2 standard deviations , and especially useful in sideways moving market. Observe the bands yourself , and analyse the accuracy of all the trade signals provided by the bollinger bands. Save to a new csv file.

# In[52]:


import pandas as pd
import matplotlib.pyplot as plt

symbol = 'TCS'
# read csv file, use date as index and read close as a column
df = pd.read_csv('tcs.csv'.format(symbol), index_col='Date',
                 parse_dates=True, usecols=['Date', 'Close Price'],
                 na_values='nan')

# rename the column header with symbol name
df = df.rename(columns={'Close Price': symbol})
df.dropna(inplace=True)

# calculate Simple Moving Average with 14 days window
sma = df.rolling(window=14).mean()

# calculate the standar deviation
rstd = df.rolling(window=14).std()

upper_band = sma + 2 * rstd
upper_band = upper_band.rename(columns={symbol: 'upper'})
lower_band = sma - 2 * rstd
lower_band = lower_band.rename(columns={symbol: 'lower'})
df = df.join(upper_band).join(lower_band)
ax = df.plot(title='{} Price and BB'.format(symbol))
ax.fill_between(df.index, lower_band['lower'], upper_band['upper'], color='#ADCCFF', alpha='0.4')
ax.set_xlabel('Date')
ax.set_ylabel('SMA and BB')
ax.grid()
plt.show()


# In[ ]:




