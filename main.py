import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from black_scholes_pricing import *
from get_data import *
from volatility import *
from plots import *



ticker = str(input(f"Please input a stock ticker:"))
r = get_risk_free_rate()
S, T, Market_calls, Market_puts = get_option_data(ticker)

# Estimate the volatility using one of three methods: mle, ewma, garch(1,1)
end = datetime.today()
start = end - timedelta(days = 365)
Vol = Volatility(ticker, start, end)
sigma = Vol.mle_estimator()

print(f'Current price of {ticker} is: ', S)
print("Select a strike price for the option expiring in ", round(T,2), "years: ")
print(Market_calls['strike'].values)
strike_selection = int(input(f'\nInput a number from 0 to {len(Market_calls)-1} to select the strike price: '))

K = Market_calls['strike'][strike_selection]

# instance of BlackScholes:
bm = BlackScholes(S, K, T, r, sigma)

print("Model parameters: \n")
print(bm.parameters())

print("\nBlack Scholes option price =  ", round(bm._call(), 2))
print("Market option price = ", Market_calls['lastPrice'][strike_selection])

plot_vs_S(K, T, r, sigma)
plot_vs_T(S, K, r, sigma)
plot_vs_sig(S, K, T, r)
plot_ST_contour(K, r, sigma)
