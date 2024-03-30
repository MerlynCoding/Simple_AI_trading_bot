from module import *

API_KEY = "API_KEY"
API_SECRET = "API_SECRET"
BASE_URL = "https://api.alpaca.markets"

ALPACA_CREDS = {
    "API_KEY":API_KEY,
    "API_SECRET": API_SECRET,
    # "PAPER": True
}


start_date = datetime(2020,1,1)
end_date = datetime(2024,3,30)
broker = Alpaca(ALPACA_CREDS)
strategy = MLTrader(name='mlstrat', broker=broker,
                    parameters={"symbol":"SPY",
                                "cash_at_risk":.5})
strategy.backtest(
    YahooDataBacktesting,
    start_date,
    end_date,
    parameters={"symbol":"SPY", "cash_at_risk":.5}
)
# trader = Trader()
# trader.add_strategy(strategy)
# trader.run_all()
