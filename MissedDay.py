import os, datetime, time
from pandas_datareader import data
import yfinance as yf
import pandas as pd

#Read .csv containing list of stocks
stocks_mentioned = pd.read_csv(r'C:\\Users\\Ashley\\Downloads\\Scripts\\Stonks\\StocksMentioned.csv')

#Produce excel file with columns: symbol, closing price, % day change
	#List of tickers
tickers = stocks_mentioned['Symbol'].to_list()

	#Today's date in proper format for datareader and 
	#yesterday's date to read .csv file containing yesterday's data
today = datetime.date.today()
date = datetime.date.isoformat(today)
yesterday = today - datetime.timedelta(days=1)

	#Adj Close today and previous day- if monday do friday as start and monday as end
adjClose = data.DataReader(tickers,
						start='2021-04-27',
						end='2021-04-28',
						data_source='yahoo')['Adj Close']
adjClose = adjClose.transpose()
adjClose.columns = ['Adj Close Yesterday', 'Adj Close']

	#Calculate % Day Change and add to data
adjClose['Percent Change'] = ((adjClose['Adj Close'] - adjClose['Adj Close Yesterday'])/adjClose['Adj Close Yesterday']) * 100

	#Change color of Excel cell based on value in Percent Change
#data.style.\
#	applymap(lambda val: 'background-color: red' if val < 0 else 'background-color: green')

	#Removing Adj Close yesterday
adjClose = adjClose.drop(columns=['Adj Close Yesterday'])

	#Sorting by Percent change
adjClose = adjClose.sort_values(by=['Percent Change'], ascending=False)
print(adjClose)

#Save out to new .csv, new filename containing the days' date
adjClose.to_csv(r'C:\\Users\\Ashley\\Downloads\\Scripts\\Stonks\\Output\\2021-04-28.csv')

#run at market close
#time.strftime
