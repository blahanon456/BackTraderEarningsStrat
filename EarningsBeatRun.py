from EarningsBeatStrategy import EarningsBeatStrategy
from strategies import *

# extending generic data class to include eps estimate, actual, and suprise percent
class PutEarningsData(bt.feeds.GenericCSVData):
    lines = ('epsestimate', 'epsactual', 'epssurprisepct')
    params = (
        ('dtformat', '%Y-%m-%d'),
        ('Date', 0),
        ('Open', 1),
        ('High', 2),
        ('Low', 3),
        ('Close', 4),
        ('Adj Close', 5),
        ('Volume', 6),
        ('epsestimate', 7),
        ('epsactual', 8),
       ('epssurprisepct', 9)
    )

# creating and instantiating the new data
aapl_test_file = "C:\\Users\\jmkre\\PycharmProjects\\financialPythonPractice\\HistoricalData1D\\AAPL.csv"
aapl_eps_feed = PutEarningsData(dataname = aapl_test_file)

cerebro = bt.Cerebro()
cerebro.broker.set_cash(25000)
cerebro.adddata(aapl_eps_feed)
cerebro.addstrategy(EarningsBeatStrategy)
print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())
cerebro.run()
print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
cerebro.plot()