from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import MetaTrader5 as mt5

def DataRequest(ticker, rates, plot):

    print("establish connection to MetaTrader 5 terminal...")
    if not mt5.initialize():
        print("initialize() failed, error code =",mt5.last_error())
        quit()

    # request rates from ticker
    tickerRates = mt5.copy_rates_from(ticker, mt5.TIMEFRAME_M1, datetime.now(), rates)

    #print those values
    print("Number of rates returned: " + str(len(tickerRates)))

    #create dataframe from rates and handle datetime as string for interpolation on pyplot
    tickerFrame = pd.DataFrame(tickerRates)
    tickerFrame['time']=pd.to_datetime(tickerFrame['time'], unit='s')
    tickerFrame['time'] = tickerFrame['time'].astype(str)

    if(plot):
        plt.plot(tickerFrame['time'], tickerFrame['close'], 'b-', label='close')
        plt.show()
    
    return tickerFrame

DataRequest("WIN$N", 1000, True)



