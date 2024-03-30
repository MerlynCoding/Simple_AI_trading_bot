# Simple_AI_trading_bot
This project implements a trading strategy that incorporates sentiment analysis of financial news using the Alpaca API.

## Installation

To install and run this project, follow these steps:

1. **Clone the Repository**: Clone this repository to your local machine using the following command:

    ```bash
    git clone https://github.com/your-username/trading-strategy.git
    ```

2. **Install Dependencies**: Navigate to the project directory and install the required dependencies using pip:

    ```bash
    cd trading-strategy
    pip install -r requirements.txt
    ```

3. **Set Up Alpaca API Credentials**: Sign up for an account on [Alpaca](https://alpaca.markets/) and obtain your API key and secret key. Replace `"API_KEY"` and `"API_SECRET"` in the `config.py` file with your actual API key and secret key.

4. **Run the Strategy**: Execute the `main.py` file to run the trading strategy:

    ```bash
    python main.py
    ```

## Usage

### MLTrader Class

The `MLTrader` class implements the trading strategy. Here's a breakdown of its key components:

- **initialize**: This method initializes the strategy with parameters such as the symbol to trade and the risk percentage.
- **position_sizing**: This method calculates the position size based on available cash and risk percentage.
- **get_dates**: This method retrieves the current date and the date three days prior.
- **get_sentiment**: This method fetches financial news for the specified symbol and estimates sentiment using a pre-trained model.
- **on_trading_iteration**: This method executes the trading logic based on sentiment analysis and risk management.

### Backtesting

The `backtest` method in the `strategy` object is used to backtest the trading strategy using historical data. Specify the start and end dates for the backtest, along with any additional parameters.

## inspiration by
Nicholas Renotte

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.
