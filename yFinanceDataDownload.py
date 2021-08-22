import yahoo_fin.stock_info as si
import time
import datetime
import pandas as pd

SYMBOL_LIST = ['GILD', 'MU', 'ISRG', 'AMAT', 'INTU', 'AMD', 'ZM', 'ABNB', 'SBUX', 'CHTR', 'AMGN', 'TXN', 'COST', 'TMUS', 'QCOM',
           'AVGO', 'CSCO', 'PEP', 'ADBE', 'INTC', 'CMCSA', 'NFLX', 'PYPL', 'NVDA', 'FB', 'TSLA', 'GOOG', 'AMZN', 'MSFT',
           'AAPL', 'GE']


def dataMerge():
    for i in SYMBOL_LIST:
        period1 = int(time.mktime(datetime.datetime(2018, 1, 1, 23, 59).timetuple()))
        period2 = int(time.mktime(datetime.datetime(2021, 7, 31, 23, 59).timetuple()))
        interval = '1d'  # 1d, 1m
        query_string = f'https://query1.finance.yahoo.com/v7/finance/download/{i}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'
        df = pd.read_csv(query_string)
        earnDF = getEarnings(i)
        dfmerge = pd.merge(df, earnDF, on = ['Date'], how = 'outer')
        dfmerge.fillna('0.0', inplace=True)
        dfmerge.to_csv("C:\\Users\\jmkre\\PycharmProjects\\financialPythonPractice\\HistoricalData1D\\" + i + '.csv', index=False)


def getEarnings(symbol):
    earnHistory = si.get_earnings_history(symbol)
    eHDF = pd.DataFrame.from_dict(earnHistory)
    mask = (eHDF['startdatetime'] > '2018-1-1') & (eHDF['startdatetime'] < '2021-7-30')
    eHDF = eHDF.loc[mask].rename(columns = {'startdatetime':'Date'})\
        .drop(columns=['ticker','companyshortname','startdatetimetype','timeZoneShortName','gmtOffsetMilliSeconds','quoteType'])\
        .dropna()
    eHDF['Date'] = eHDF['Date'].str.split('T').str[0]
    return eHDF.dropna()


def main():
    dataMerge()

main()