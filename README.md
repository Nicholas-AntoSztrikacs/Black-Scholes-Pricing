# Black-Scholes-Pricing
This repository contains a Python program for option pricing via the Black-Scholes-Merton model. This repository uses real market data to price the options, however, it is not meant as a serious option pricer, but rather was created as a tool to learn the theory of option pricing models, and as a testbed to write better software. 

The Black-Scholes-Pricing repository is used to price vanilla European, as well as binary derivatives and is written within a flexible OOP framework such that adding new functionalities to the model is straightforward. The repository also contains files to get market data to provide more realistic predictions

## Getting Started 
If you would like to use or add to this repository you can either clone or download it

```
git clone https://github.com/Nicholas-AntoSztrikacs/Black-Scholes-Pricing
```

The main file in this repository is `main.py` which when run, prompts the user to input a ticker to obtain data corresponding to this security, such as the stock price `S0`, the strike price `K`, and the time to expiration `T` of an option. Beyond this, the risk free interest rate '`r` is scraped to represent the daily rate using `get_data`. Furthermore, the `volatility` class is used to estimate the volatilty parameter `sigma` from historical data, with a 3 possible estimation methods. The program returns the model price of the option, and then compares it to the actual market data. Moreover, the program also shows output plots displaying how the option price will change as a function of parameters in the model.   

## Prerequisites
This repository makes use of external packages: `numpy`, `scipy`, and `matplotlib`, `datetime`, `requests`, `bs4`, `yfinance`. You can install them using `pip` with the following code:
```
pip install numpy scipy matplotlib requests beautifulsoup4 yfinance
```

## To-Do
1) Implement other derivative products
    * Asian derivatives 

2) Add additional functionality to the volatility class
    * Implement impplied volatility calculator

3) Add in the analysis of the Greeks
