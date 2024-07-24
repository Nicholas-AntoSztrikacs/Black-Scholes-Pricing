import requests
from bs4 import BeautifulSoup
import yfinance as yf
from datetime import datetime

def get_risk_free_rate():
    url = 'https://fred.stlouisfed.org/series/DGS10'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Locate the span class="series-meta-observation-value" to extract the
    span = soup.find('span', class_="series-meta-observation-value")

    # Extract the text from the span and convert to float
    risk_free_rate = float(span.text) / 100
    return risk_free_rate

def get_option_data(ticker):
    tick = yf.Ticker(f'{ticker}')

    # Get current stock price
    underlying_price = tick.info['previousClose']

    # Get time to expiry
    expirations = tick.options
    print("Select an expiration date for the option:")
    print(expirations)
    selection = int(
        input(f'\nInput a number from 0 to {len(expirations)-1} to select the expiration date: '))

    current_date = datetime.today()
    expiration = datetime.strptime(tick.options[selection], '%Y-%m-%d')
    time_to_maturity = (expiration - current_date).days / 255

    # get the market option and the strike price
    option = tick.option_chain(tick.options[selection])
    return underlying_price, time_to_maturity, option.calls, option.puts