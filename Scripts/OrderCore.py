import json
import alpaca
from alpaca.trading.client import TradingClient
from alpaca.data.timeframe import TimeFrame, TimeFrameUnit
from alpaca.data.historical.stock import StockHistoricalDataClient
from alpaca.trading.stream import TradingStream
from alpaca.data.live.stock import StockDataStream

def lambda_handler(event, context):
    # TODO implemen
    api_key = "PK87X9Q8XDXTHNOO16FP"
    secret_key = "mvnUTdejlnMy3tkTpiD1fzUWB6UXfK3gckya0qBL"
    paper = True
    trade_api_url = None
    trade_api_wss = None
    data_api_url = None
    stream_data_wss = None

    # setup clients
    trade_client = TradingClient(api_key=api_key, secret_key=secret_key, paper=paper, url_override=trade_api_url)
    acct = trade_client.get_account()
    print(acct)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

def tomarOrden(symbol):
    symbol = "SPY"
    req = MarketOrderRequest(
    symbol = symbol,
    notional = 1.11,  # notional is specified in USD, here we specify $1.11
    side = OrderSide.BUY,
    type = OrderType.MARKET,
    time_in_force = TimeInForce.DAY,
    )

    res = trade_client.submit_order(req)

    print(res)
