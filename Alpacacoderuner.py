import subprocess
import time
import alpaca_trade_api as tradeapi
import schedule

# set up Alpaca API credentials
api_key = 'PKF6FQFL86F53UDQ59XU'
api_secret = 'sCIrdCRuPCqTUaFaZQACmqG9lzfiVcwREArNCo6j'
base_url = 'https://paper-api.alpaca.markets'

# create Alpaca API client
api = tradeapi.REST(api_key, api_secret, base_url)

# retrieve account information
account = api.get_account()

# retrieve all positions
positions = api.list_positions()
# run the doctorOalpaca.py file using the subprocess module
subprocess.run(["python", "doctorOalpaca.py"])
time.sleep(10)
# loop through positions and submit sell orders for each
for position in positions:
    symbol = position.symbol
    qty = position.qty
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='sell',
        type='market',
        time_in_force='gtc'
    )
    print(f'Sold {qty} shares of {symbol}.')

print('All positions have been sold.')
