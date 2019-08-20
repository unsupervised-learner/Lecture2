import pandas as pd
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


if __name__ == '__main__':
	main()
