import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as pdr
import datetime as dt

def main():
	start_date = dt.datetime(2010, 1, 1)
	end_date = dt.datetime(2019, 6, 24)
	print('start date : {}'.format(start_date))
	print('end date : {}'.format(end_date))

	#download data
	stocks = pdr.DataReader('MMM', 'yahoo', start_date, end_date)
	print(stocks)

	#create figure
	fig1 = plt.subplot2grid((7,1) , (0,0), rowspan=5, colspan=1)
	fig2 = plt.subplot2grid((7,1), (1,0) , rowspan=2, colspan=1)

	plt.plot(stocks.index, stocks['Adj Close'])
	plt.show()


if __name__ == '__main__':
	main()
