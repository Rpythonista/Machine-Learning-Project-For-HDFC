
# MODULE 1

# Problem statement 1.1

Import the csv file of the stock you have been allotted using 'pd.read_csv()' function into a dataframe.
Shares of a company can be offered in more than one category. The category of a stock is indicated in the ‘Series’ column. If the csv file has data on more than one category, the ‘Date’ column will have repeating values. To avoid repetitions in the date, remove all the rows where 'Series' column is NOT 'EQ'.
Analyze and understand each column properly.
You'd find the head(), tail() and describe() functions to be immensely useful for exploration. You're free to carry out any other exploration of your own.


```python
#Importing libraries
import pandas as pd
import numpy as np
import datetime
```


```python
#Reading data
raw_data=pd.read_csv("HDFC.csv")
raw_data.head() #use to display initial few rows of dataset
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>15-May-2017</td>
      <td>1549.80</td>
      <td>1554.50</td>
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
    </tr>
    <tr>
      <th>1</th>
      <td>HDFC</td>
      <td>W2</td>
      <td>15-May-2017</td>
      <td>204.45</td>
      <td>217.95</td>
      <td>217.95</td>
      <td>205.00</td>
      <td>205.0</td>
      <td>205.00</td>
      <td>209.50</td>
      <td>29200</td>
      <td>6.117400e+06</td>
      <td>4</td>
      <td>29200</td>
      <td>100.00</td>
    </tr>
    <tr>
      <th>2</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>16-May-2017</td>
      <td>1559.50</td>
      <td>1558.00</td>
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
    </tr>
    <tr>
      <th>3</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>17-May-2017</td>
      <td>1566.55</td>
      <td>1565.50</td>
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
    </tr>
    <tr>
      <th>4</th>
      <td>HDFC</td>
      <td>W2</td>
      <td>17-May-2017</td>
      <td>205.00</td>
      <td>204.95</td>
      <td>207.00</td>
      <td>204.95</td>
      <td>207.0</td>
      <td>207.00</td>
      <td>205.75</td>
      <td>73000</td>
      <td>1.501938e+07</td>
      <td>10</td>
      <td>73000</td>
      <td>100.00</td>
    </tr>
  </tbody>
</table>
</div>




```python
raw_data.tail() #use to display last few rows of dataset
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>824</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>07-May-2019</td>
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
    </tr>
    <tr>
      <th>825</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>08-May-2019</td>
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
    </tr>
    <tr>
      <th>826</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>09-May-2019</td>
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
    </tr>
    <tr>
      <th>827</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>10-May-2019</td>
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
    </tr>
    <tr>
      <th>828</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>13-May-2019</td>
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
    </tr>
  </tbody>
</table>
</div>




```python
raw_data.describe() #use to display description and features of dataset
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>829.000000</td>
      <td>829.000000</td>
      <td>829.000000</td>
      <td>829.000000</td>
      <td>829.000000</td>
      <td>829.000000</td>
      <td>829.000000</td>
      <td>8.290000e+02</td>
      <td>8.290000e+02</td>
      <td>829.000000</td>
      <td>8.290000e+02</td>
      <td>829.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>1235.068637</td>
      <td>1237.372376</td>
      <td>1249.368938</td>
      <td>1223.320869</td>
      <td>1236.191858</td>
      <td>1236.496562</td>
      <td>1236.178492</td>
      <td>1.763380e+06</td>
      <td>3.107192e+09</td>
      <td>67614.677925</td>
      <td>1.241798e+06</td>
      <td>72.594077</td>
    </tr>
    <tr>
      <th>std</th>
      <td>728.839077</td>
      <td>730.235891</td>
      <td>734.456171</td>
      <td>724.421341</td>
      <td>729.350445</td>
      <td>729.566264</td>
      <td>729.328719</td>
      <td>1.650588e+06</td>
      <td>3.092474e+09</td>
      <td>63518.256040</td>
      <td>1.183951e+06</td>
      <td>15.632166</td>
    </tr>
    <tr>
      <th>min</th>
      <td>193.000000</td>
      <td>193.000000</td>
      <td>194.400000</td>
      <td>190.250000</td>
      <td>193.000000</td>
      <td>193.000000</td>
      <td>193.290000</td>
      <td>7.300000e+03</td>
      <td>1.445400e+06</td>
      <td>1.000000</td>
      <td>0.000000e+00</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>365.000000</td>
      <td>367.450000</td>
      <td>373.000000</td>
      <td>357.000000</td>
      <td>365.000000</td>
      <td>365.000000</td>
      <td>364.590000</td>
      <td>1.460000e+05</td>
      <td>5.301187e+07</td>
      <td>18.000000</td>
      <td>1.022000e+05</td>
      <td>65.840000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>1700.800000</td>
      <td>1705.000000</td>
      <td>1715.000000</td>
      <td>1685.050000</td>
      <td>1701.000000</td>
      <td>1702.100000</td>
      <td>1703.630000</td>
      <td>1.685595e+06</td>
      <td>3.091969e+09</td>
      <td>75553.000000</td>
      <td>1.141221e+06</td>
      <td>72.720000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>1858.900000</td>
      <td>1864.000000</td>
      <td>1881.500000</td>
      <td>1847.050000</td>
      <td>1860.050000</td>
      <td>1859.550000</td>
      <td>1865.270000</td>
      <td>2.778618e+06</td>
      <td>5.053920e+09</td>
      <td>116325.000000</td>
      <td>1.983472e+06</td>
      <td>80.950000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>2069.150000</td>
      <td>2068.000000</td>
      <td>2073.000000</td>
      <td>2039.150000</td>
      <td>2067.000000</td>
      <td>2069.150000</td>
      <td>2057.720000</td>
      <td>9.486397e+06</td>
      <td>1.749929e+10</td>
      <td>312842.000000</td>
      <td>6.951300e+06</td>
      <td>100.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
data = raw_data[raw_data.Series == 'EQ'] #drops the W2 entries from the dataset
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>15-May-2017</td>
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
    </tr>
    <tr>
      <th>2</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>16-May-2017</td>
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
    </tr>
    <tr>
      <th>3</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>17-May-2017</td>
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
    </tr>
    <tr>
      <th>5</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>18-May-2017</td>
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
    </tr>
    <tr>
      <th>7</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>19-May-2017</td>
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
    </tr>
    <tr>
      <th>9</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>22-May-2017</td>
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
    </tr>
    <tr>
      <th>11</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>23-May-2017</td>
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
    </tr>
    <tr>
      <th>13</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>24-May-2017</td>
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
    </tr>
    <tr>
      <th>15</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>25-May-2017</td>
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
    </tr>
    <tr>
      <th>17</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>26-May-2017</td>
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
    </tr>
    <tr>
      <th>19</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>29-May-2017</td>
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
    </tr>
    <tr>
      <th>21</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>30-May-2017</td>
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
    </tr>
    <tr>
      <th>23</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>31-May-2017</td>
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
    </tr>
    <tr>
      <th>25</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>01-Jun-2017</td>
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
    </tr>
    <tr>
      <th>27</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>02-Jun-2017</td>
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
    </tr>
    <tr>
      <th>29</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>05-Jun-2017</td>
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
    </tr>
    <tr>
      <th>31</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>06-Jun-2017</td>
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
    </tr>
    <tr>
      <th>33</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>07-Jun-2017</td>
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
    </tr>
    <tr>
      <th>35</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>08-Jun-2017</td>
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
    </tr>
    <tr>
      <th>37</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>09-Jun-2017</td>
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
    </tr>
    <tr>
      <th>39</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>12-Jun-2017</td>
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
    </tr>
    <tr>
      <th>41</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>13-Jun-2017</td>
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
    </tr>
    <tr>
      <th>43</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>14-Jun-2017</td>
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
    </tr>
    <tr>
      <th>45</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>15-Jun-2017</td>
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
    </tr>
    <tr>
      <th>47</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>16-Jun-2017</td>
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
    </tr>
    <tr>
      <th>49</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>19-Jun-2017</td>
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
    </tr>
    <tr>
      <th>51</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>20-Jun-2017</td>
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
    </tr>
    <tr>
      <th>53</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>21-Jun-2017</td>
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
    </tr>
    <tr>
      <th>55</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>22-Jun-2017</td>
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
    </tr>
    <tr>
      <th>57</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>23-Jun-2017</td>
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
    </tr>
    <tr>
      <th>799</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>27-Mar-2019</td>
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
    </tr>
    <tr>
      <th>800</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>28-Mar-2019</td>
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
    </tr>
    <tr>
      <th>801</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>29-Mar-2019</td>
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
    </tr>
    <tr>
      <th>802</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>01-Apr-2019</td>
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
    </tr>
    <tr>
      <th>803</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>02-Apr-2019</td>
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
    </tr>
    <tr>
      <th>804</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>03-Apr-2019</td>
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
    </tr>
    <tr>
      <th>805</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>04-Apr-2019</td>
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
    </tr>
    <tr>
      <th>806</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>05-Apr-2019</td>
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
    </tr>
    <tr>
      <th>807</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>08-Apr-2019</td>
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
    </tr>
    <tr>
      <th>808</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>09-Apr-2019</td>
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
    </tr>
    <tr>
      <th>809</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>10-Apr-2019</td>
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
    </tr>
    <tr>
      <th>810</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>11-Apr-2019</td>
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
    </tr>
    <tr>
      <th>811</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>12-Apr-2019</td>
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
    </tr>
    <tr>
      <th>812</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>15-Apr-2019</td>
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
    </tr>
    <tr>
      <th>813</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>16-Apr-2019</td>
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
    </tr>
    <tr>
      <th>814</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>18-Apr-2019</td>
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
    </tr>
    <tr>
      <th>815</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>22-Apr-2019</td>
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
    </tr>
    <tr>
      <th>816</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>23-Apr-2019</td>
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
    </tr>
    <tr>
      <th>817</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>24-Apr-2019</td>
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
    </tr>
    <tr>
      <th>818</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>25-Apr-2019</td>
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
    </tr>
    <tr>
      <th>819</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>26-Apr-2019</td>
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
    </tr>
    <tr>
      <th>820</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>30-Apr-2019</td>
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
    </tr>
    <tr>
      <th>821</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>02-May-2019</td>
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
    </tr>
    <tr>
      <th>822</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>03-May-2019</td>
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
    </tr>
    <tr>
      <th>823</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>06-May-2019</td>
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
    </tr>
    <tr>
      <th>824</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>07-May-2019</td>
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
    </tr>
    <tr>
      <th>825</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>08-May-2019</td>
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
    </tr>
    <tr>
      <th>826</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>09-May-2019</td>
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
    </tr>
    <tr>
      <th>827</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>10-May-2019</td>
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
    </tr>
    <tr>
      <th>828</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>13-May-2019</td>
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
    </tr>
  </tbody>
</table>
<p>494 rows × 15 columns</p>
</div>



# Problem statement 1.2

Calculate the maximum, minimum and mean price for the last 90 days. (price=Closing Price unless stated otherwise)


```python
data.tail(90)['Close Price'].max() #Calculates maximum price for last 30 days.
```




    2069.15




```python
data.tail(90)['Close Price'].min() #Calculates minimum price for last 30 days.
```




    1841.0




```python
data.tail(90)['Close Price'].mean() #Calculates mean price for last 30 days.
```




    1955.255555555555



# Problem statement 1.3

Analyse the data types for each column of the dataframe. Pandas knows how to deal with dates in an intelligent manner. But to make use of Pandas functionality for dates, you need to ensure that the column is of type 'datetime64(ns)'. Change the date column from 'object' type to 'datetime64(ns)' for future convenience. See what happens if you subtract the minimum value of the date column from the maximum value.


```python
data.dtypes
```




    Symbol                     object
    Series                     object
    Date                       object
    Prev Close                float64
    Open Price                float64
    High Price                float64
    Low Price                 float64
    Last Price                float64
    Close Price               float64
    Average Price             float64
    Total Traded Quantity       int64
    Turnover                  float64
    No. of Trades               int64
    Deliverable Qty             int64
    % Dly Qt to Traded Qty    float64
    dtype: object




```python
data['Date'] = data['Date'].astype('datetime64[ns]')
```


```python
data.dtypes
```




    Symbol                            object
    Series                            object
    Date                      datetime64[ns]
    Prev Close                       float64
    Open Price                       float64
    High Price                       float64
    Low Price                        float64
    Last Price                       float64
    Close Price                      float64
    Average Price                    float64
    Total Traded Quantity              int64
    Turnover                         float64
    No. of Trades                      int64
    Deliverable Qty                    int64
    % Dly Qt to Traded Qty           float64
    dtype: object




```python
max_date = max(data["Date"]) #Calculate max date
min_date = min(data["Date"]) #calculate min date
sub_date= max_date-min_date #Subtraction of min date from max date
sub_date
```




    Timedelta('728 days 00:00:00')



# Problem Statement 1.4

In a separate array , calculate the monthwise VWAP (Volume Weighted Average Price ) of the stock.
( VWAP = sum(price*volume)/sum(volume) )
{Hint : Create a new dataframe column ‘Month’. The values for this column can be derived from the ‘Date” column by using appropriate pandas functions. Similarly, create a column ‘Year’ and initialize it. Then use the 'groupby()' function by month and year. Finally, calculate the vwap value for each month (i.e. for each group created).


```python
data['Month'] = pd.DatetimeIndex(data['Date']).month #A new dataframe column ‘Month’.
data['Year'] = pd.DatetimeIndex(data['Date']).year #A new dataframe column ‘Year’.
#Calculation of VWAP value
data['VWAP'] = (np.cumsum(data['Close Price'] * data['Total Traded Quantity'])/(np.cumsum(data['Total Traded Quantity'])))
data_vwap = data[['Month','Year','VWAP']]
#Data grouping
group = data_vwap.groupby(['Month','Year'])
group.first()
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
      <th></th>
      <th>VWAP</th>
    </tr>
    <tr>
      <th>Month</th>
      <th>Year</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">1</th>
      <th>2018</th>
      <td>1694.491061</td>
    </tr>
    <tr>
      <th>2019</th>
      <td>1794.152939</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">2</th>
      <th>2018</th>
      <td>1720.484381</td>
    </tr>
    <tr>
      <th>2019</th>
      <td>1802.884744</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">3</th>
      <th>2018</th>
      <td>1730.985450</td>
    </tr>
    <tr>
      <th>2019</th>
      <td>1806.769172</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">4</th>
      <th>2018</th>
      <td>1738.592304</td>
    </tr>
    <tr>
      <th>2019</th>
      <td>1813.411405</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">5</th>
      <th>2017</th>
      <td>1559.500000</td>
    </tr>
    <tr>
      <th>2018</th>
      <td>1747.132021</td>
    </tr>
    <tr>
      <th>2019</th>
      <td>1821.038455</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">6</th>
      <th>2017</th>
      <td>1554.616636</td>
    </tr>
    <tr>
      <th>2018</th>
      <td>1755.426983</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">7</th>
      <th>2017</th>
      <td>1606.443668</td>
    </tr>
    <tr>
      <th>2018</th>
      <td>1763.034286</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">8</th>
      <th>2017</th>
      <td>1639.711234</td>
    </tr>
    <tr>
      <th>2018</th>
      <td>1776.142270</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">9</th>
      <th>2017</th>
      <td>1667.030031</td>
    </tr>
    <tr>
      <th>2018</th>
      <td>1784.464312</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">10</th>
      <th>2017</th>
      <td>1686.617325</td>
    </tr>
    <tr>
      <th>2018</th>
      <td>1787.719313</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">11</th>
      <th>2017</th>
      <td>1692.873801</td>
    </tr>
    <tr>
      <th>2018</th>
      <td>1782.283901</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">12</th>
      <th>2017</th>
      <td>1694.459291</td>
    </tr>
    <tr>
      <th>2018</th>
      <td>1786.975805</td>
    </tr>
  </tbody>
</table>
</div>



# Problem Statement 1.5

Write a function to calculate the average price over the last N days of the stock price data where N is a user defined parameter. Write a second function to calculate the profit/loss percentage over the last N days.
Calculate the average price AND the profit/loss percentages over the course of last -
1 week, 2 weeks, 1 month, 3 months, 6 months and 1 year.
{Note : Profit/Loss percentage between N days is the percentage change between the closing prices of the 2 days }


```python
def avgerage_price(N): #N refers to number of days.
    return (data['Average Price'].tail(N).sum())/N
print("Average prices for last N days are as follows:")
print("Last 1 week",avgerage_price(5))
print("Last 2 weeks",avgerage_price(10))
print("Last 1 month",avgerage_price(20))
print("Last 3 months",avgerage_price(60))
print("Last 6 months",avgerage_price(120))
print("Last 1 year",avgerage_price(240))
```

    Average prices for last N days are as follows:
    Last 1 week 1947.5220000000002
    Last 2 weeks 1967.8839999999996
    Last 1 month 1983.4120000000003
    Last 3 months 1948.4721666666667
    Last 6 months 1947.6675833333331
    Last 1 year 1904.6807916666664
    


```python
data['Close Price'].tail(4)
data['Close Price'].tail(4).iloc[3]
```




    1952.9




```python
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
```

    Profit/Loss % for N days are as follows:
    Loss/Profit percentage for last N days are as follows:
    Last 1 week 0.6861590455220371
    Last 2 weeks 1.2545445235291104
    Last 1 month 3.9095703825080603
    Last 3 months 0.2406677249219133
    Last 6 months 5.084745762711874
    Last 1 year 7.31732295560449
    

# Problem Statement 1.6

Add a column 'Day_Perc_Change' where the values are the daily change in percentages i.e. the percentage change between 2 consecutive day's closing prices. Instead of using the basic mathematical formula for computing the same, use 'pct_change()' function provided by Pandas for dataframes. You will note that the first entry of the column will have a ‘Nan’ value. Why does this happen? Either remove the first row, or set the entry to 0 before proceeding.


```python
data['Day_Perc_Change'] = data['Close Price'].pct_change().fillna(0) #Adds a column Day_Perc_Change.
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2017-05-15</td>
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
    </tr>
    <tr>
      <th>2</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2017-05-16</td>
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
    </tr>
    <tr>
      <th>3</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2017-05-17</td>
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
    </tr>
    <tr>
      <th>5</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2017-05-18</td>
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
    </tr>
    <tr>
      <th>7</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2017-05-19</td>
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
    </tr>
    <tr>
      <th>9</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2017-05-22</td>
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
    </tr>
    <tr>
      <th>11</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2017-05-23</td>
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
    </tr>
    <tr>
      <th>13</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2017-05-24</td>
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
    </tr>
    <tr>
      <th>15</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2017-05-25</td>
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
    </tr>
    <tr>
      <th>17</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2017-05-26</td>
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
    </tr>
    <tr>
      <th>19</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2017-05-29</td>
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
    </tr>
    <tr>
      <th>21</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2017-05-30</td>
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
    </tr>
    <tr>
      <th>23</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2017-05-31</td>
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
    </tr>
    <tr>
      <th>25</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2017-06-01</td>
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
    </tr>
    <tr>
      <th>27</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2017-06-02</td>
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
    </tr>
    <tr>
      <th>29</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2017-06-05</td>
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
    </tr>
    <tr>
      <th>31</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2017-06-06</td>
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
    </tr>
    <tr>
      <th>33</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2017-06-07</td>
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
    </tr>
    <tr>
      <th>35</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2017-06-08</td>
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
    </tr>
    <tr>
      <th>37</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2017-06-09</td>
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
    </tr>
    <tr>
      <th>39</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2017-06-12</td>
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
    </tr>
    <tr>
      <th>41</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2017-06-13</td>
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
    </tr>
    <tr>
      <th>43</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2017-06-14</td>
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
    </tr>
    <tr>
      <th>45</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2017-06-15</td>
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
    </tr>
    <tr>
      <th>47</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2017-06-16</td>
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
    </tr>
    <tr>
      <th>49</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2017-06-19</td>
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
    </tr>
    <tr>
      <th>51</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2017-06-20</td>
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
    </tr>
    <tr>
      <th>53</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2017-06-21</td>
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
    </tr>
    <tr>
      <th>55</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2017-06-22</td>
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
    </tr>
    <tr>
      <th>57</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2017-06-23</td>
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
      <th>799</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2019-03-27</td>
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
    </tr>
    <tr>
      <th>800</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2019-03-28</td>
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
    </tr>
    <tr>
      <th>801</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2019-03-29</td>
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
    </tr>
    <tr>
      <th>802</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2019-04-01</td>
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
    </tr>
    <tr>
      <th>803</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2019-04-02</td>
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
    </tr>
    <tr>
      <th>804</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2019-04-03</td>
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
    </tr>
    <tr>
      <th>805</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2019-04-04</td>
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
    </tr>
    <tr>
      <th>806</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2019-04-05</td>
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
    </tr>
    <tr>
      <th>807</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2019-04-08</td>
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
    </tr>
    <tr>
      <th>808</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2019-04-09</td>
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
    </tr>
    <tr>
      <th>809</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2019-04-10</td>
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
    </tr>
    <tr>
      <th>810</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2019-04-11</td>
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
    </tr>
    <tr>
      <th>811</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2019-04-12</td>
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
    </tr>
    <tr>
      <th>812</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2019-04-15</td>
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
    </tr>
    <tr>
      <th>813</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2019-04-16</td>
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
    </tr>
    <tr>
      <th>814</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2019-04-18</td>
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
    </tr>
    <tr>
      <th>815</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2019-04-22</td>
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
    </tr>
    <tr>
      <th>816</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2019-04-23</td>
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
    </tr>
    <tr>
      <th>817</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2019-04-24</td>
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
    </tr>
    <tr>
      <th>818</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2019-04-25</td>
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
    </tr>
    <tr>
      <th>819</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2019-04-26</td>
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
    </tr>
    <tr>
      <th>820</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2019-04-30</td>
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
    </tr>
    <tr>
      <th>821</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2019-05-02</td>
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
    </tr>
    <tr>
      <th>822</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2019-05-03</td>
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
    </tr>
    <tr>
      <th>823</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2019-05-06</td>
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
    </tr>
    <tr>
      <th>824</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2019-05-07</td>
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
    </tr>
    <tr>
      <th>825</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2019-05-08</td>
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
    </tr>
    <tr>
      <th>826</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2019-05-09</td>
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
    </tr>
    <tr>
      <th>827</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2019-05-10</td>
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
    </tr>
    <tr>
      <th>828</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2019-05-13</td>
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
    </tr>
  </tbody>
</table>
<p>494 rows × 19 columns</p>
</div>



# Problem Statement 1.7

Add another column 'Trend' whose values are:
1. 'Slight or No change' for 'Day_Perc_Change' in between -0.5 and 0.5
2. 'Slight positive' for 'Day_Perc_Change' in between 0.5 and 1
3. 'Slight negative' for 'Day_Perc_Change' in between -0.5 and -1
4. 'Positive' for 'Day_Perc_Change' in between 1 and 3
5. 'Negative' for 'Day_Perc_Change' in between -1 and -3
6. 'Among top gainers' for 'Day_Perc_Change' in between 3 and 7
7. 'Among top losers' for 'Day_Perc_Change' in between -3 and -7
8. 'Bull run' for 'Day_Perc_Change' >7
9. 'Bear drop' for 'Day_Perc_Change' <-7


```python
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
      <th>2</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2017-05-16</td>
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
      <th>3</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2017-05-17</td>
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
      <th>5</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2017-05-18</td>
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
      <th>7</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2017-05-19</td>
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
      <th>9</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2017-05-22</td>
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
      <th>11</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2017-05-23</td>
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
      <th>13</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2017-05-24</td>
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
      <th>15</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2017-05-25</td>
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
      <th>17</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2017-05-26</td>
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
      <th>19</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2017-05-29</td>
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
      <th>21</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2017-05-30</td>
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
      <th>23</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2017-05-31</td>
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
      <th>25</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2017-06-01</td>
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
      <th>27</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2017-06-02</td>
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
      <th>29</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2017-06-05</td>
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
      <th>31</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2017-06-06</td>
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
      <th>33</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2017-06-07</td>
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
      <th>35</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2017-06-08</td>
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
      <th>37</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2017-06-09</td>
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
      <th>39</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2017-06-12</td>
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
      <th>41</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2017-06-13</td>
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
      <th>43</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2017-06-14</td>
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
      <th>45</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2017-06-15</td>
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
      <th>47</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2017-06-16</td>
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
      <th>49</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2017-06-19</td>
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
      <th>51</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2017-06-20</td>
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
      <th>53</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2017-06-21</td>
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
      <th>55</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2017-06-22</td>
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
      <th>57</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2017-06-23</td>
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
      <td>...</td>
    </tr>
    <tr>
      <th>799</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2019-03-27</td>
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
      <th>800</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2019-03-28</td>
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
      <th>801</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2019-03-29</td>
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
      <th>802</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2019-04-01</td>
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
      <th>803</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2019-04-02</td>
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
      <th>804</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2019-04-03</td>
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
      <th>805</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2019-04-04</td>
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
      <th>806</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2019-04-05</td>
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
      <th>807</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2019-04-08</td>
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
      <th>808</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2019-04-09</td>
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
      <th>809</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2019-04-10</td>
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
      <th>810</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2019-04-11</td>
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
      <th>811</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2019-04-12</td>
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
      <th>812</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2019-04-15</td>
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
      <th>813</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2019-04-16</td>
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
      <th>814</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2019-04-18</td>
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
      <th>815</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2019-04-22</td>
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
      <th>816</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2019-04-23</td>
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
      <th>817</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2019-04-24</td>
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
      <th>818</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2019-04-25</td>
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
      <th>819</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2019-04-26</td>
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
      <th>820</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2019-04-30</td>
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
      <th>821</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2019-05-02</td>
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
      <th>822</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2019-05-03</td>
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
      <th>823</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2019-05-06</td>
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
      <th>824</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2019-05-07</td>
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
      <th>825</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2019-05-08</td>
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
      <th>826</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2019-05-09</td>
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
      <th>827</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2019-05-10</td>
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
      <th>828</th>
      <td>HDFC</td>
      <td>EQ</td>
      <td>2019-05-13</td>
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
<p>494 rows × 20 columns</p>
</div>



# Problem Statement 1.8

Find the average and median values of the column 'Total Traded Quantity' for each of the types of 'Trend'.
{Hint : use 'groupby()' on the 'Trend' column and then calculate the average and median values of the column 'Total Traded Quantity'}


```python
data.groupby(data.Trend).mean()['Total Traded Quantity'] #Calculation of mean value for Total Traded Quantity
data.groupby(data.Trend).median()['Total Traded Quantity'] #Calculation of median value for Total Traded Quantity
```




    Trend
    Slight or No change    2557129.0
    Name: Total Traded Quantity, dtype: float64



# Problem Statement 1.9

SAVE the dataframe with the additional columns computed as a csv file week2.csv. In Module 2, you are going to get familiar with matplotlib, the python module which is used to visualize data.


```python
data.to_csv('week2.csv') #Save the dataset.
```
