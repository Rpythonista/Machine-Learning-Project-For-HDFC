
# Module 2 (Data visualization and Technical Analysis)

# Problem Statement 2.1
Load the week2.csv file into a dataframe. What is the type of the Date column? Make sure it is of type datetime64. Convert the Date column to the index of the dataframe.
Plot the closing price of each of the days for the entire time frame to get an idea of what the general outlook of the stock is.
1. Look out for drastic changes in this stock, you have the exact date when these took place, try to fetch the news for this day of this stock
2. This would be helpful if we are to train our model to take NLP inputs.


```python
#import libraries
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from functools import partial
import matplotlib.pyplot as plt
```


```python
data = pd.read_csv("week2.csv")#loading week2.csv file
del data['Unnamed: 0']
raw_data = data 
data.head()#loading first few lines of week2.csv file
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Symbol</th>
      <th>Series</th>
      <th>Date</th>
      <th>Prev Close</th>
      <th>Open Price</th>
      <th>High Price</th>
      <th>Low Price</th>
      <th>Last Price</th>
      <th>Close Price</th>
      <th>Average Price</th>
      <th>Total Traded Quantity</th>
      <th>Turnover</th>
      <th>No. of Trades</th>
      <th>Deliverable Qty</th>
      <th>% Dly Qt to Traded Qty</th>
      <th>Month</th>
      <th>Year</th>
      <th>VWAP</th>
      <th>Day_Perc_Change</th>
      <th>Trend</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2017-05-15</td>
      <td>1549.80</td>
      <td>1554.5</td>
      <td>1572.60</td>
      <td>1554.10</td>
      <td>1561.0</td>
      <td>1559.50</td>
      <td>1562.62</td>
      <td>1270297</td>
      <td>1.984990e+09</td>
      <td>59917</td>
      <td>955875</td>
      <td>75.25</td>
      <td>5</td>
      <td>2017</td>
      <td>1559.500000</td>
      <td>0.000000</td>
      <td>Slight or No change</td>
    </tr>
    <tr>
      <th>1</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2017-05-16</td>
      <td>1559.50</td>
      <td>1558.0</td>
      <td>1569.00</td>
      <td>1554.00</td>
      <td>1568.0</td>
      <td>1566.55</td>
      <td>1564.05</td>
      <td>2114918</td>
      <td>3.307844e+09</td>
      <td>79354</td>
      <td>1652379</td>
      <td>78.13</td>
      <td>5</td>
      <td>2017</td>
      <td>1563.904498</td>
      <td>0.004521</td>
      <td>Slight or No change</td>
    </tr>
    <tr>
      <th>2</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2017-05-17</td>
      <td>1566.55</td>
      <td>1565.5</td>
      <td>1570.95</td>
      <td>1549.75</td>
      <td>1550.1</td>
      <td>1552.50</td>
      <td>1557.08</td>
      <td>2161434</td>
      <td>3.365526e+09</td>
      <td>80317</td>
      <td>1794472</td>
      <td>83.02</td>
      <td>5</td>
      <td>2017</td>
      <td>1559.460361</td>
      <td>-0.008969</td>
      <td>Slight or No change</td>
    </tr>
    <tr>
      <th>3</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2017-05-18</td>
      <td>1552.50</td>
      <td>1547.0</td>
      <td>1558.60</td>
      <td>1526.50</td>
      <td>1545.0</td>
      <td>1537.05</td>
      <td>1539.03</td>
      <td>2404372</td>
      <td>3.700407e+09</td>
      <td>85842</td>
      <td>1837821</td>
      <td>76.44</td>
      <td>5</td>
      <td>2017</td>
      <td>1552.683515</td>
      <td>-0.009952</td>
      <td>Slight or No change</td>
    </tr>
    <tr>
      <th>4</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2017-05-19</td>
      <td>1537.05</td>
      <td>1545.0</td>
      <td>1548.00</td>
      <td>1515.35</td>
      <td>1526.5</td>
      <td>1520.60</td>
      <td>1526.14</td>
      <td>2142433</td>
      <td>3.269652e+09</td>
      <td>113875</td>
      <td>1601236</td>
      <td>74.74</td>
      <td>5</td>
      <td>2017</td>
      <td>1545.873479</td>
      <td>-0.010702</td>
      <td>Slight or No change</td>
    </tr>
  </tbody>
</table>
</div>




```python
data['Date'] = data['Date'].astype('datetime64[ns]')
data.Date.dtype
```




    dtype('<M8[ns]')




```python
data.set_index('Date', inplace = True)
data
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Symbol</th>
      <th>Series</th>
      <th>Prev Close</th>
      <th>Open Price</th>
      <th>High Price</th>
      <th>Low Price</th>
      <th>Last Price</th>
      <th>Close Price</th>
      <th>Average Price</th>
      <th>Total Traded Quantity</th>
      <th>Turnover</th>
      <th>No. of Trades</th>
      <th>Deliverable Qty</th>
      <th>% Dly Qt to Traded Qty</th>
      <th>Month</th>
      <th>Year</th>
      <th>VWAP</th>
      <th>Day_Perc_Change</th>
      <th>Trend</th>
    </tr>
    <tr>
      <th>Date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-05-15</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>1549.80</td>
      <td>1554.50</td>
      <td>1572.60</td>
      <td>1554.10</td>
      <td>1561.00</td>
      <td>1559.50</td>
      <td>1562.62</td>
      <td>1270297</td>
      <td>1.984990e+09</td>
      <td>59917</td>
      <td>955875</td>
      <td>75.25</td>
      <td>5</td>
      <td>2017</td>
      <td>1559.500000</td>
      <td>0.000000</td>
      <td>Slight or No change</td>
    </tr>
    <tr>
      <th>2017-05-16</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>1559.50</td>
      <td>1558.00</td>
      <td>1569.00</td>
      <td>1554.00</td>
      <td>1568.00</td>
      <td>1566.55</td>
      <td>1564.05</td>
      <td>2114918</td>
      <td>3.307844e+09</td>
      <td>79354</td>
      <td>1652379</td>
      <td>78.13</td>
      <td>5</td>
      <td>2017</td>
      <td>1563.904498</td>
      <td>0.004521</td>
      <td>Slight or No change</td>
    </tr>
    <tr>
      <th>2017-05-17</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>1566.55</td>
      <td>1565.50</td>
      <td>1570.95</td>
      <td>1549.75</td>
      <td>1550.10</td>
      <td>1552.50</td>
      <td>1557.08</td>
      <td>2161434</td>
      <td>3.365526e+09</td>
      <td>80317</td>
      <td>1794472</td>
      <td>83.02</td>
      <td>5</td>
      <td>2017</td>
      <td>1559.460361</td>
      <td>-0.008969</td>
      <td>Slight or No change</td>
    </tr>
    <tr>
      <th>2017-05-18</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>1552.50</td>
      <td>1547.00</td>
      <td>1558.60</td>
      <td>1526.50</td>
      <td>1545.00</td>
      <td>1537.05</td>
      <td>1539.03</td>
      <td>2404372</td>
      <td>3.700407e+09</td>
      <td>85842</td>
      <td>1837821</td>
      <td>76.44</td>
      <td>5</td>
      <td>2017</td>
      <td>1552.683515</td>
      <td>-0.009952</td>
      <td>Slight or No change</td>
    </tr>
    <tr>
      <th>2017-05-19</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>1537.05</td>
      <td>1545.00</td>
      <td>1548.00</td>
      <td>1515.35</td>
      <td>1526.50</td>
      <td>1520.60</td>
      <td>1526.14</td>
      <td>2142433</td>
      <td>3.269652e+09</td>
      <td>113875</td>
      <td>1601236</td>
      <td>74.74</td>
      <td>5</td>
      <td>2017</td>
      <td>1545.873479</td>
      <td>-0.010702</td>
      <td>Slight or No change</td>
    </tr>
    <tr>
      <th>2017-05-22</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>1520.60</td>
      <td>1530.00</td>
      <td>1530.00</td>
      <td>1510.25</td>
      <td>1519.95</td>
      <td>1519.85</td>
      <td>1518.84</td>
      <td>1920867</td>
      <td>2.917481e+09</td>
      <td>70390</td>
      <td>1541085</td>
      <td>80.23</td>
      <td>5</td>
      <td>2017</td>
      <td>1541.712808</td>
      <td>-0.000493</td>
      <td>Slight or No change</td>
    </tr>
    <tr>
      <th>2017-05-23</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>1519.85</td>
      <td>1521.70</td>
      <td>1537.20</td>
      <td>1503.45</td>
      <td>1510.00</td>
      <td>1511.50</td>
      <td>1521.20</td>
      <td>1408855</td>
      <td>2.143149e+09</td>
      <td>56848</td>
      <td>969791</td>
      <td>68.84</td>
      <td>5</td>
      <td>2017</td>
      <td>1538.541765</td>
      <td>-0.005494</td>
      <td>Slight or No change</td>
    </tr>
    <tr>
      <th>2017-05-24</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>1511.50</td>
      <td>1519.00</td>
      <td>1541.75</td>
      <td>1512.40</td>
      <td>1525.00</td>
      <td>1524.85</td>
      <td>1527.90</td>
      <td>2209471</td>
      <td>3.375851e+09</td>
      <td>75808</td>
      <td>1361319</td>
      <td>61.61</td>
      <td>5</td>
      <td>2017</td>
      <td>1536.606612</td>
      <td>0.008832</td>
      <td>Slight or No change</td>
    </tr>
    <tr>
      <th>2017-05-25</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>1524.85</td>
      <td>1533.90</td>
      <td>1546.00</td>
      <td>1530.50</td>
      <td>1539.00</td>
      <td>1539.75</td>
      <td>1539.88</td>
      <td>4099792</td>
      <td>6.313184e+09</td>
      <td>91104</td>
      <td>3327557</td>
      <td>81.16</td>
      <td>5</td>
      <td>2017</td>
      <td>1537.259711</td>
      <td>0.009771</td>
      <td>Slight or No change</td>
    </tr>
    <tr>
      <th>2017-05-26</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>1539.75</td>
      <td>1538.10</td>
      <td>1563.00</td>
      <td>1530.25</td>
      <td>1544.50</td>
      <td>1547.90</td>
      <td>1548.63</td>
      <td>1871008</td>
      <td>2.897491e+09</td>
      <td>59347</td>
      <td>1270174</td>
      <td>67.89</td>
      <td>5</td>
      <td>2017</td>
      <td>1538.181234</td>
      <td>0.005293</td>
      <td>Slight or No change</td>
    </tr>
    <tr>
      <th>2017-05-29</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>1547.90</td>
      <td>1546.00</td>
      <td>1601.25</td>
      <td>1546.00</td>
      <td>1596.75</td>
      <td>1598.85</td>
      <td>1586.02</td>
      <td>3464406</td>
      <td>5.494627e+09</td>
      <td>75137</td>
      <td>1961992</td>
      <td>56.63</td>
      <td>5</td>
      <td>2017</td>
      <td>1546.565727</td>
      <td>0.032916</td>
      <td>Slight or No change</td>
    </tr>
    <tr>
      <th>2017-05-30</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>1598.85</td>
      <td>1595.70</td>
      <td>1604.00</td>
      <td>1575.05</td>
      <td>1582.60</td>
      <td>1579.50</td>
      <td>1588.05</td>
      <td>1605211</td>
      <td>2.549149e+09</td>
      <td>77293</td>
      <td>1019565</td>
      <td>63.52</td>
      <td>5</td>
      <td>2017</td>
      <td>1548.547744</td>
      <td>-0.012102</td>
      <td>Slight or No change</td>
    </tr>
    <tr>
      <th>2017-05-31</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>1579.50</td>
      <td>1581.00</td>
      <td>1596.15</td>
      <td>1565.40</td>
      <td>1576.80</td>
      <td>1569.85</td>
      <td>1571.89</td>
      <td>4907685</td>
      <td>7.714320e+09</td>
      <td>160031</td>
      <td>3833239</td>
      <td>78.11</td>
      <td>5</td>
      <td>2017</td>
      <td>1551.858139</td>
      <td>-0.006110</td>
      <td>Slight or No change</td>
    </tr>
    <tr>
      <th>2017-06-01</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>1569.85</td>
      <td>1551.80</td>
      <td>1587.40</td>
      <td>1551.80</td>
      <td>1577.25</td>
      <td>1583.75</td>
      <td>1575.11</td>
      <td>2990228</td>
      <td>4.709942e+09</td>
      <td>155736</td>
      <td>1983472</td>
      <td>66.33</td>
      <td>6</td>
      <td>2017</td>
      <td>1554.616636</td>
      <td>0.008854</td>
      <td>Slight or No change</td>
    </tr>
    <tr>
      <th>2017-06-02</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>1583.75</td>
      <td>1582.00</td>
      <td>1612.80</td>
      <td>1582.00</td>
      <td>1595.35</td>
      <td>1604.65</td>
      <td>1602.17</td>
      <td>3427957</td>
      <td>5.492167e+09</td>
      <td>99348</td>
      <td>2572628</td>
      <td>75.05</td>
      <td>6</td>
      <td>2017</td>
      <td>1559.130242</td>
      <td>0.013197</td>
      <td>Slight or No change</td>
    </tr>
    <tr>
      <th>2017-06-05</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>1604.65</td>
      <td>1606.40</td>
      <td>1612.00</td>
      <td>1591.15</td>
      <td>1605.00</td>
      <td>1606.15</td>
      <td>1603.91</td>
      <td>2988075</td>
      <td>4.792594e+09</td>
      <td>81217</td>
      <td>2167100</td>
      <td>72.52</td>
      <td>6</td>
      <td>2017</td>
      <td>1562.558122</td>
      <td>0.000935</td>
      <td>Slight or No change</td>
    </tr>
    <tr>
      <th>2017-06-06</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>1606.15</td>
      <td>1610.00</td>
      <td>1624.85</td>
      <td>1602.50</td>
      <td>1603.70</td>
      <td>1605.75</td>
      <td>1611.85</td>
      <td>2170920</td>
      <td>3.499205e+09</td>
      <td>48603</td>
      <td>1537563</td>
      <td>70.83</td>
      <td>6</td>
      <td>2017</td>
      <td>1564.730750</td>
      <td>-0.000249</td>
      <td>Slight or No change</td>
    </tr>
    <tr>
      <th>2017-06-07</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>1605.75</td>
      <td>1609.70</td>
      <td>1611.50</td>
      <td>1590.60</td>
      <td>1600.00</td>
      <td>1599.35</td>
      <td>1598.75</td>
      <td>1726464</td>
      <td>2.760191e+09</td>
      <td>69120</td>
      <td>1256284</td>
      <td>72.77</td>
      <td>6</td>
      <td>2017</td>
      <td>1566.062369</td>
      <td>-0.003986</td>
      <td>Slight or No change</td>
    </tr>
    <tr>
      <th>2017-06-08</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>1599.35</td>
      <td>1608.90</td>
      <td>1635.00</td>
      <td>1605.00</td>
      <td>1631.00</td>
      <td>1633.55</td>
      <td>1628.23</td>
      <td>2289492</td>
      <td>3.727828e+09</td>
      <td>104016</td>
      <td>1459772</td>
      <td>63.76</td>
      <td>6</td>
      <td>2017</td>
      <td>1569.337748</td>
      <td>0.021384</td>
      <td>Slight or No change</td>
    </tr>
    <tr>
      <th>2017-06-09</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>1633.55</td>
      <td>1628.00</td>
      <td>1649.00</td>
      <td>1620.10</td>
      <td>1646.10</td>
      <td>1647.20</td>
      <td>1636.33</td>
      <td>2633241</td>
      <td>4.308860e+09</td>
      <td>73460</td>
      <td>1898414</td>
      <td>72.09</td>
      <td>6</td>
      <td>2017</td>
      <td>1573.454229</td>
      <td>0.008356</td>
      <td>Slight or No change</td>
    </tr>
    <tr>
      <th>2017-06-12</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>1647.20</td>
      <td>1644.00</td>
      <td>1651.80</td>
      <td>1633.85</td>
      <td>1647.00</td>
      <td>1647.50</td>
      <td>1643.89</td>
      <td>2000556</td>
      <td>3.288695e+09</td>
      <td>71819</td>
      <td>1467513</td>
      <td>73.36</td>
      <td>6</td>
      <td>2017</td>
      <td>1576.313510</td>
      <td>0.000182</td>
      <td>Slight or No change</td>
    </tr>
    <tr>
      <th>2017-06-13</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>1647.50</td>
      <td>1642.05</td>
      <td>1682.20</td>
      <td>1642.05</td>
      <td>1665.00</td>
      <td>1667.65</td>
      <td>1667.32</td>
      <td>2737084</td>
      <td>4.563601e+09</td>
      <td>143134</td>
      <td>1840910</td>
      <td>67.26</td>
      <td>6</td>
      <td>2017</td>
      <td>1580.896821</td>
      <td>0.012231</td>
      <td>Slight or No change</td>
    </tr>
    <tr>
      <th>2017-06-14</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>1667.65</td>
      <td>1661.55</td>
      <td>1668.00</td>
      <td>1644.00</td>
      <td>1647.10</td>
      <td>1651.10</td>
      <td>1651.72</td>
      <td>6519614</td>
      <td>1.076859e+10</td>
      <td>139220</td>
      <td>6014688</td>
      <td>92.26</td>
      <td>6</td>
      <td>2017</td>
      <td>1588.392150</td>
      <td>-0.009924</td>
      <td>Slight or No change</td>
    </tr>
    <tr>
      <th>2017-06-15</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>1651.10</td>
      <td>1648.70</td>
      <td>1653.70</td>
      <td>1629.55</td>
      <td>1635.00</td>
      <td>1636.85</td>
      <td>1642.13</td>
      <td>5678766</td>
      <td>9.325296e+09</td>
      <td>73070</td>
      <td>5097448</td>
      <td>89.76</td>
      <td>6</td>
      <td>2017</td>
      <td>1592.515132</td>
      <td>-0.008631</td>
      <td>Slight or No change</td>
    </tr>
    <tr>
      <th>2017-06-16</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>1636.85</td>
      <td>1634.30</td>
      <td>1651.00</td>
      <td>1629.15</td>
      <td>1635.20</td>
      <td>1640.85</td>
      <td>1641.87</td>
      <td>2692532</td>
      <td>4.420795e+09</td>
      <td>73989</td>
      <td>1737533</td>
      <td>64.53</td>
      <td>6</td>
      <td>2017</td>
      <td>1594.389431</td>
      <td>0.002444</td>
      <td>Slight or No change</td>
    </tr>
    <tr>
      <th>2017-06-19</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>1640.85</td>
      <td>1659.00</td>
      <td>1660.00</td>
      <td>1645.20</td>
      <td>1659.60</td>
      <td>1654.20</td>
      <td>1652.88</td>
      <td>2907637</td>
      <td>4.805977e+09</td>
      <td>62546</td>
      <td>2321542</td>
      <td>79.84</td>
      <td>6</td>
      <td>2017</td>
      <td>1596.793349</td>
      <td>0.008136</td>
      <td>Slight or No change</td>
    </tr>
    <tr>
      <th>2017-06-20</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>1654.20</td>
      <td>1651.15</td>
      <td>1660.00</td>
      <td>1627.90</td>
      <td>1632.15</td>
      <td>1631.50</td>
      <td>1636.96</td>
      <td>2304515</td>
      <td>3.772390e+09</td>
      <td>67469</td>
      <td>1652828</td>
      <td>71.72</td>
      <td>6</td>
      <td>2017</td>
      <td>1597.864807</td>
      <td>-0.013723</td>
      <td>Slight or No change</td>
    </tr>
    <tr>
      <th>2017-06-21</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>1631.50</td>
      <td>1632.15</td>
      <td>1638.00</td>
      <td>1615.50</td>
      <td>1626.00</td>
      <td>1628.25</td>
      <td>1622.59</td>
      <td>2359678</td>
      <td>3.828801e+09</td>
      <td>85584</td>
      <td>1833784</td>
      <td>77.71</td>
      <td>6</td>
      <td>2017</td>
      <td>1598.795876</td>
      <td>-0.001992</td>
      <td>Slight or No change</td>
    </tr>
    <tr>
      <th>2017-06-22</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>1628.25</td>
      <td>1626.10</td>
      <td>1660.00</td>
      <td>1626.10</td>
      <td>1650.10</td>
      <td>1653.80</td>
      <td>1651.94</td>
      <td>3438975</td>
      <td>5.680997e+09</td>
      <td>129910</td>
      <td>2724127</td>
      <td>79.21</td>
      <td>6</td>
      <td>2017</td>
      <td>1601.147225</td>
      <td>0.015692</td>
      <td>Slight or No change</td>
    </tr>
    <tr>
      <th>2017-06-23</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>1653.80</td>
      <td>1660.00</td>
      <td>1661.00</td>
      <td>1642.10</td>
      <td>1650.20</td>
      <td>1651.35</td>
      <td>1651.51</td>
      <td>2590704</td>
      <td>4.278584e+09</td>
      <td>119288</td>
      <td>1946085</td>
      <td>75.12</td>
      <td>6</td>
      <td>2017</td>
      <td>1602.713518</td>
      <td>-0.001481</td>
      <td>Slight or No change</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2019-03-27</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>1946.30</td>
      <td>1955.55</td>
      <td>1959.00</td>
      <td>1906.00</td>
      <td>1914.10</td>
      <td>1919.90</td>
      <td>1937.71</td>
      <td>3076446</td>
      <td>5.961253e+09</td>
      <td>161822</td>
      <td>2146231</td>
      <td>69.76</td>
      <td>3</td>
      <td>2019</td>
      <td>1811.895440</td>
      <td>-0.013564</td>
      <td>Slight or No change</td>
    </tr>
    <tr>
      <th>2019-03-28</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>1919.90</td>
      <td>1917.00</td>
      <td>1950.00</td>
      <td>1912.05</td>
      <td>1942.10</td>
      <td>1944.45</td>
      <td>1942.93</td>
      <td>6370987</td>
      <td>1.237836e+10</td>
      <td>151893</td>
      <td>5177109</td>
      <td>81.26</td>
      <td>3</td>
      <td>2019</td>
      <td>1812.535496</td>
      <td>0.012787</td>
      <td>Slight or No change</td>
    </tr>
    <tr>
      <th>2019-03-29</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>1944.45</td>
      <td>1950.05</td>
      <td>1972.25</td>
      <td>1936.05</td>
      <td>1964.00</td>
      <td>1968.25</td>
      <td>1956.38</td>
      <td>4320179</td>
      <td>8.451925e+09</td>
      <td>148642</td>
      <td>3200934</td>
      <td>74.09</td>
      <td>3</td>
      <td>2019</td>
      <td>1813.043688</td>
      <td>0.012240</td>
      <td>Slight or No change</td>
    </tr>
    <tr>
      <th>2019-04-01</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>1968.25</td>
      <td>1968.10</td>
      <td>1975.00</td>
      <td>1945.05</td>
      <td>1951.00</td>
      <td>1959.65</td>
      <td>1960.06</td>
      <td>3328552</td>
      <td>6.524154e+09</td>
      <td>168073</td>
      <td>2370360</td>
      <td>71.21</td>
      <td>4</td>
      <td>2019</td>
      <td>1813.411405</td>
      <td>-0.004369</td>
      <td>Slight or No change</td>
    </tr>
    <tr>
      <th>2019-04-02</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>1959.65</td>
      <td>1966.10</td>
      <td>2001.00</td>
      <td>1955.00</td>
      <td>1998.95</td>
      <td>1995.95</td>
      <td>1979.73</td>
      <td>3655232</td>
      <td>7.236387e+09</td>
      <td>159005</td>
      <td>2561511</td>
      <td>70.08</td>
      <td>4</td>
      <td>2019</td>
      <td>1813.912801</td>
      <td>0.018524</td>
      <td>Slight or No change</td>
    </tr>
    <tr>
      <th>2019-04-03</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>1995.95</td>
      <td>2004.00</td>
      <td>2032.45</td>
      <td>1997.15</td>
      <td>2008.75</td>
      <td>2013.10</td>
      <td>2019.73</td>
      <td>4345772</td>
      <td>8.777270e+09</td>
      <td>109651</td>
      <td>2926819</td>
      <td>67.35</td>
      <td>4</td>
      <td>2019</td>
      <td>1814.561173</td>
      <td>0.008592</td>
      <td>Slight or No change</td>
    </tr>
    <tr>
      <th>2019-04-04</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2013.10</td>
      <td>2008.00</td>
      <td>2058.80</td>
      <td>2006.30</td>
      <td>2041.90</td>
      <td>2042.05</td>
      <td>2037.46</td>
      <td>4463212</td>
      <td>9.093604e+09</td>
      <td>154293</td>
      <td>3106308</td>
      <td>69.60</td>
      <td>4</td>
      <td>2019</td>
      <td>1815.319146</td>
      <td>0.014381</td>
      <td>Slight or No change</td>
    </tr>
    <tr>
      <th>2019-04-05</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2042.05</td>
      <td>2045.00</td>
      <td>2065.00</td>
      <td>2035.00</td>
      <td>2064.50</td>
      <td>2059.20</td>
      <td>2055.28</td>
      <td>2576789</td>
      <td>5.296023e+09</td>
      <td>125822</td>
      <td>1692384</td>
      <td>65.68</td>
      <td>4</td>
      <td>2019</td>
      <td>1815.787385</td>
      <td>0.008398</td>
      <td>Slight or No change</td>
    </tr>
    <tr>
      <th>2019-04-08</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2059.20</td>
      <td>2068.00</td>
      <td>2072.50</td>
      <td>2029.25</td>
      <td>2052.00</td>
      <td>2054.90</td>
      <td>2048.64</td>
      <td>2057768</td>
      <td>4.215626e+09</td>
      <td>114354</td>
      <td>1387042</td>
      <td>67.41</td>
      <td>4</td>
      <td>2019</td>
      <td>1816.153439</td>
      <td>-0.002088</td>
      <td>Slight or No change</td>
    </tr>
    <tr>
      <th>2019-04-09</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2054.90</td>
      <td>2062.50</td>
      <td>2073.00</td>
      <td>2039.15</td>
      <td>2067.00</td>
      <td>2069.15</td>
      <td>2057.72</td>
      <td>2381281</td>
      <td>4.900013e+09</td>
      <td>162102</td>
      <td>1662887</td>
      <td>69.83</td>
      <td>4</td>
      <td>2019</td>
      <td>1816.600846</td>
      <td>0.006935</td>
      <td>Slight or No change</td>
    </tr>
    <tr>
      <th>2019-04-10</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2069.15</td>
      <td>2067.50</td>
      <td>2068.00</td>
      <td>2025.10</td>
      <td>2029.95</td>
      <td>2029.25</td>
      <td>2038.39</td>
      <td>3036356</td>
      <td>6.189267e+09</td>
      <td>151203</td>
      <td>2155517</td>
      <td>70.99</td>
      <td>4</td>
      <td>2019</td>
      <td>1817.079273</td>
      <td>-0.019283</td>
      <td>Slight or No change</td>
    </tr>
    <tr>
      <th>2019-04-11</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2029.25</td>
      <td>2028.00</td>
      <td>2048.00</td>
      <td>2017.50</td>
      <td>2018.10</td>
      <td>2022.80</td>
      <td>2029.46</td>
      <td>2521729</td>
      <td>5.117742e+09</td>
      <td>160208</td>
      <td>1690856</td>
      <td>67.05</td>
      <td>4</td>
      <td>2019</td>
      <td>1817.462949</td>
      <td>-0.003179</td>
      <td>Slight or No change</td>
    </tr>
    <tr>
      <th>2019-04-12</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2022.80</td>
      <td>2024.00</td>
      <td>2029.90</td>
      <td>2008.10</td>
      <td>2023.00</td>
      <td>2024.95</td>
      <td>2020.07</td>
      <td>2121821</td>
      <td>4.286233e+09</td>
      <td>102234</td>
      <td>1519702</td>
      <td>71.62</td>
      <td>4</td>
      <td>2019</td>
      <td>1817.788042</td>
      <td>0.001063</td>
      <td>Slight or No change</td>
    </tr>
    <tr>
      <th>2019-04-15</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2024.95</td>
      <td>2034.90</td>
      <td>2034.90</td>
      <td>2010.00</td>
      <td>2012.00</td>
      <td>2014.25</td>
      <td>2019.10</td>
      <td>1333222</td>
      <td>2.691910e+09</td>
      <td>76176</td>
      <td>811985</td>
      <td>60.90</td>
      <td>4</td>
      <td>2019</td>
      <td>1817.981266</td>
      <td>-0.005284</td>
      <td>Slight or No change</td>
    </tr>
    <tr>
      <th>2019-04-16</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2014.25</td>
      <td>2019.70</td>
      <td>2034.30</td>
      <td>2016.10</td>
      <td>2027.20</td>
      <td>2026.70</td>
      <td>2025.80</td>
      <td>2000314</td>
      <td>4.052236e+09</td>
      <td>166866</td>
      <td>1489678</td>
      <td>74.47</td>
      <td>4</td>
      <td>2019</td>
      <td>1818.288804</td>
      <td>0.006181</td>
      <td>Slight or No change</td>
    </tr>
    <tr>
      <th>2019-04-18</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2026.70</td>
      <td>2040.00</td>
      <td>2047.90</td>
      <td>1998.15</td>
      <td>2005.00</td>
      <td>2003.75</td>
      <td>2013.04</td>
      <td>3888701</td>
      <td>7.828095e+09</td>
      <td>175404</td>
      <td>2147684</td>
      <td>55.23</td>
      <td>4</td>
      <td>2019</td>
      <td>1818.818535</td>
      <td>-0.011324</td>
      <td>Slight or No change</td>
    </tr>
    <tr>
      <th>2019-04-22</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2003.75</td>
      <td>2005.00</td>
      <td>2010.00</td>
      <td>1948.00</td>
      <td>1958.50</td>
      <td>1953.90</td>
      <td>1970.41</td>
      <td>2002662</td>
      <td>3.946056e+09</td>
      <td>80677</td>
      <td>1361456</td>
      <td>67.98</td>
      <td>4</td>
      <td>2019</td>
      <td>1819.016944</td>
      <td>-0.024878</td>
      <td>Slight or No change</td>
    </tr>
    <tr>
      <th>2019-04-23</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>1953.90</td>
      <td>1958.00</td>
      <td>1966.25</td>
      <td>1929.60</td>
      <td>1930.00</td>
      <td>1934.70</td>
      <td>1944.34</td>
      <td>2848980</td>
      <td>5.539373e+09</td>
      <td>109800</td>
      <td>1999347</td>
      <td>70.18</td>
      <td>4</td>
      <td>2019</td>
      <td>1819.258163</td>
      <td>-0.009827</td>
      <td>Slight or No change</td>
    </tr>
    <tr>
      <th>2019-04-24</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>1934.70</td>
      <td>1943.90</td>
      <td>1985.00</td>
      <td>1933.25</td>
      <td>1984.70</td>
      <td>1980.40</td>
      <td>1958.44</td>
      <td>2758373</td>
      <td>5.402103e+09</td>
      <td>115391</td>
      <td>1799052</td>
      <td>65.22</td>
      <td>4</td>
      <td>2019</td>
      <td>1819.582830</td>
      <td>0.023621</td>
      <td>Slight or No change</td>
    </tr>
    <tr>
      <th>2019-04-25</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>1980.40</td>
      <td>1987.55</td>
      <td>1998.80</td>
      <td>1946.55</td>
      <td>1951.45</td>
      <td>1955.15</td>
      <td>1970.35</td>
      <td>4162465</td>
      <td>8.201508e+09</td>
      <td>136733</td>
      <td>2807343</td>
      <td>67.44</td>
      <td>4</td>
      <td>2019</td>
      <td>1819.993756</td>
      <td>-0.012750</td>
      <td>Slight or No change</td>
    </tr>
    <tr>
      <th>2019-04-26</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>1955.15</td>
      <td>1959.30</td>
      <td>1982.15</td>
      <td>1941.60</td>
      <td>1976.95</td>
      <td>1977.40</td>
      <td>1963.96</td>
      <td>2094836</td>
      <td>4.114177e+09</td>
      <td>102041</td>
      <td>1440081</td>
      <td>68.74</td>
      <td>4</td>
      <td>2019</td>
      <td>1820.233511</td>
      <td>0.011380</td>
      <td>Slight or No change</td>
    </tr>
    <tr>
      <th>2019-04-30</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>1977.40</td>
      <td>1977.40</td>
      <td>1999.85</td>
      <td>1954.20</td>
      <td>1995.55</td>
      <td>1995.05</td>
      <td>1976.43</td>
      <td>3675345</td>
      <td>7.264045e+09</td>
      <td>122095</td>
      <td>2606623</td>
      <td>70.92</td>
      <td>4</td>
      <td>2019</td>
      <td>1820.699438</td>
      <td>0.008926</td>
      <td>Slight or No change</td>
    </tr>
    <tr>
      <th>2019-05-02</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>1995.05</td>
      <td>1995.00</td>
      <td>2027.90</td>
      <td>1989.25</td>
      <td>2018.00</td>
      <td>2017.40</td>
      <td>2012.44</td>
      <td>2380823</td>
      <td>4.791258e+09</td>
      <td>124835</td>
      <td>1428794</td>
      <td>60.01</td>
      <td>5</td>
      <td>2019</td>
      <td>1821.038455</td>
      <td>0.011203</td>
      <td>Slight or No change</td>
    </tr>
    <tr>
      <th>2019-05-03</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2017.40</td>
      <td>2017.50</td>
      <td>2037.60</td>
      <td>2000.00</td>
      <td>2002.80</td>
      <td>2006.40</td>
      <td>2020.47</td>
      <td>1451357</td>
      <td>2.932422e+09</td>
      <td>80223</td>
      <td>850504</td>
      <td>58.60</td>
      <td>5</td>
      <td>2019</td>
      <td>1821.233002</td>
      <td>-0.005453</td>
      <td>Slight or No change</td>
    </tr>
    <tr>
      <th>2019-05-06</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2006.40</td>
      <td>1987.25</td>
      <td>1993.95</td>
      <td>1957.00</td>
      <td>1965.90</td>
      <td>1965.45</td>
      <td>1967.93</td>
      <td>2216418</td>
      <td>4.361748e+09</td>
      <td>89509</td>
      <td>1394023</td>
      <td>62.90</td>
      <td>5</td>
      <td>2019</td>
      <td>1821.463786</td>
      <td>-0.020410</td>
      <td>Slight or No change</td>
    </tr>
    <tr>
      <th>2019-05-07</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>1965.45</td>
      <td>1974.80</td>
      <td>2009.15</td>
      <td>1959.20</td>
      <td>1964.50</td>
      <td>1966.30</td>
      <td>1983.01</td>
      <td>2683956</td>
      <td>5.322315e+09</td>
      <td>114029</td>
      <td>1522276</td>
      <td>56.72</td>
      <td>5</td>
      <td>2019</td>
      <td>1821.743908</td>
      <td>0.000432</td>
      <td>Slight or No change</td>
    </tr>
    <tr>
      <th>2019-05-08</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>1966.30</td>
      <td>1964.50</td>
      <td>1964.50</td>
      <td>1925.05</td>
      <td>1930.10</td>
      <td>1930.75</td>
      <td>1941.55</td>
      <td>3626183</td>
      <td>7.040422e+09</td>
      <td>151779</td>
      <td>2378973</td>
      <td>65.61</td>
      <td>5</td>
      <td>2019</td>
      <td>1822.028003</td>
      <td>-0.018080</td>
      <td>Slight or No change</td>
    </tr>
    <tr>
      <th>2019-05-09</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>1930.75</td>
      <td>1926.00</td>
      <td>1931.60</td>
      <td>1901.30</td>
      <td>1914.15</td>
      <td>1914.60</td>
      <td>1918.15</td>
      <td>1932792</td>
      <td>3.707382e+09</td>
      <td>130444</td>
      <td>1132999</td>
      <td>58.62</td>
      <td>5</td>
      <td>2019</td>
      <td>1822.156420</td>
      <td>-0.008365</td>
      <td>Slight or No change</td>
    </tr>
    <tr>
      <th>2019-05-10</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>1914.60</td>
      <td>1915.25</td>
      <td>1956.00</td>
      <td>1910.75</td>
      <td>1926.80</td>
      <td>1931.70</td>
      <td>1936.05</td>
      <td>1628923</td>
      <td>3.153682e+09</td>
      <td>97684</td>
      <td>811832</td>
      <td>49.84</td>
      <td>5</td>
      <td>2019</td>
      <td>1822.284341</td>
      <td>0.008931</td>
      <td>Slight or No change</td>
    </tr>
    <tr>
      <th>2019-05-13</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>1931.70</td>
      <td>1926.10</td>
      <td>1984.40</td>
      <td>1917.85</td>
      <td>1957.00</td>
      <td>1952.90</td>
      <td>1958.85</td>
      <td>4509527</td>
      <td>8.833504e+09</td>
      <td>139299</td>
      <td>1332224</td>
      <td>29.54</td>
      <td>5</td>
      <td>2019</td>
      <td>1822.705238</td>
      <td>0.010975</td>
      <td>Slight or No change</td>
    </tr>
  </tbody>
</table>
<p>494 rows × 19 columns</p>
</div>




```python
%matplotlib inline
data['Close Price'].plot(label='HDFC',figsize=(20,10),title="Closeing Price with respect to Date")
plt.legend()
```




    <matplotlib.legend.Legend at 0x2c214903550>




![png](output_6_1.png)



```python
data['Close Price'].diff().abs().sort_values(ascending= False)
```




    Date
    2018-09-24    120.70
    2018-01-15    110.25
    2018-10-31     97.35
    2017-07-27     94.75
    2018-02-05     80.50
    2018-10-19     77.55
    2018-10-05     69.80
    2018-02-02     63.70
    2018-11-02     62.40
    2018-01-29     59.30
    2017-07-28     57.15
    2018-12-17     56.25
    2018-10-24     54.70
    2018-09-25     54.65
    2018-10-11     52.40
    2018-10-01     51.85
    2017-05-29     50.95
    2018-08-16     50.30
    2019-04-22     49.85
    2018-06-22     47.85
    2018-09-14     47.65
    2018-10-25     47.00
    2017-11-01     46.90
    2018-09-17     46.60
    2018-12-24     46.45
    2018-10-12     45.75
    2019-04-24     45.70
    2018-08-03     45.55
    2018-10-09     45.05
    2018-12-10     44.85
                   ...  
    2017-10-31      1.60
    2017-06-05      1.50
    2018-06-15      1.50
    2018-06-14      1.45
    2018-02-19      1.45
    2017-07-26      1.40
    2018-12-11      1.25
    2018-08-29      1.10
    2018-05-15      1.05
    2018-06-11      1.00
    2018-04-26      0.95
    2017-12-05      0.90
    2019-05-07      0.85
    2017-12-12      0.85
    2017-05-22      0.75
    2018-08-07      0.70
    2017-07-18      0.65
    2019-03-26      0.65
    2019-03-05      0.55
    2017-06-06      0.40
    2019-01-07      0.30
    2017-06-27      0.30
    2017-06-12      0.30
    2018-11-09      0.25
    2019-02-28      0.20
    2017-07-25      0.20
    2017-10-24      0.10
    2019-02-18      0.05
    2017-11-27      0.05
    2017-05-15       NaN
    Name: Close Price, Length: 494, dtype: float64




```python
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
```

    News for Jan 15, 2018
    
    
    Title:
    Buy HDFC Bank, says Mitessh Thakkar
    
    
    Subject:
    Mitessh Thakkar of mitesshthakkar.com advises buying HDFC Bank.
    
    
    Report:
    Mitessh Thakkar of mitesshthakkar.com told CNBC-TV18, "HDFC Bank is a buy with a stoploss of Rs 1,884 for target of Rs 1,930."
    
    
    ///////////////////////////////////////////////////////////////////////////////////////////////////////////////
    
    
    News for Jul 27, 2018
    
    
    Title:
    IHH open offer for Fortis to commence on Sept 7
    
    
    Subject:
    A draft letter of the offer to Fortis shareholders was submitted to the bourses by the managers to open offer -- HSBC Securities and Capital Markets (India) Pvt Ltd, HDFC Bank Ltd, Citigroup Global Markets India Pvt Ltd and Deutsche Equities India Pvt Ltd.
    
    
    Report:
    The open offer by Malaysian firm IHH Healthcare Berhad to acquire additional 26 percent stake in Fortis Healthcare will commence on September 7 and close on September 24, 2018, as per a regulatory filing by managers of the offer.
    
    
    ///////////////////////////////////////////////////////////////////////////////////////////////////////////////
    
    
    News for Oct 19, 2018
    
    
    Title:
    HDFC Bank Q2 earnings preview: Watch out for these 5 key factors
    
    
    Subject:
    Asset quality is also expected to remain stable for the quarter on sequential basis.
    
    
    Report:
    HDFC Bank is expected to report a double-digit profit, net interest income and loan growth year-on-year (YoY) in the second quarter of FY19 with sequentially stable asset quality. The country's second largest private sector lender will release its second quarter (July-September) earnings on October 20.
    
    
    
