import yfinance as yf
import pandas as pd
import numpy as np
from arch import arch_model


# class to compute the volatilities using historical data
# these return yearly volatilities

class Volatility:
    def __init__(self, ticker, start, end):
        self.ticker = ticker
        self.start = start
        self.end = end

        tick = yf.Ticker(f'{self.ticker}')
        dataDF = tick.history(tick, start=start, end=end)
        self.close_data = pd.DataFrame(dataDF['Close'], columns=["Close"])
        self.close_data['log_return'] = np.log(
            self.close_data) - np.log(self.close_data.shift(1))

        self.close_data = self.close_data.dropna()

    def mle_estimator(self):
        return np.sqrt(
            255) * np.sqrt(((self.close_data['log_return'] - self.close_data['log_return'].mean())**2).mean())

    def ewma(self):
        moving_average = self.close_data['log_return'].ewm(span=252).std()
        return moving_average.iloc[-1] * np.sqrt(255)

    def garch(self):
        garch_model = arch_model(
            self.close_data['log_return'],
            mean='Zero',
            vol='Garch',
            p=1,
            q=1)
        garch_fit = garch_model.fit(disp='off')

        forecasts = garch_fit.forecast(horizon=1)
        var = forecasts.variance.iloc[-1]

        return float(np.sqrt(var) * np.sqrt(255))
