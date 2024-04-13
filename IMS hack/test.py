import pandas as pd
from prophet import Prophet
import configparser
from typing import Dict, List
from collections import deque
import logging

from datamodel import OrderDepth, Order, TradingState

# Read configuration from file
config = configparser.ConfigParser()
config.read('config.ini')
MAX_HISTORY_SIZE = int(config.get('trader', 'max_history_size', fallback=500))
DEFAULT_VOLATILE_PRICE = int(config.get('trader', 'default_volatile_price', fallback=4000))

# Set up logging
logging.basicConfig(filename='trader.log', level=logging.INFO)

class Trader:
    def __init__(self):
        self.price_history: Dict[str, deque] = {'AMETHYSTS': deque(maxlen=MAX_HISTORY_SIZE),
                                                'STARFRUIT': deque(maxlen=MAX_HISTORY_SIZE)}
        self.models: Dict[str, Prophet] = {'AMETHYSTS': Prophet(),
                                           'STARFRUIT': Prophet()}

    def update_price_history(self, product: str, new_price: float):
        """Adds the latest price to the product's price history."""
        self.price_history[product].append(new_price)

    def train_model(self, product: str):
        """Train the time series forecasting model for the given product."""
        history = list(self.price_history[product])
        if len(history) < 10:
            return

        df = pd.DataFrame({'ds': [i for i in range(len(history))], 'y': history})
        self.models[product].fit(df)

    def predict_price(self, product: str) -> float:
        """Predict the next price for the given product using the trained model."""
        history = list(self.price_history[product])
        if not history:
            return DEFAULT_VOLATILE_PRICE

        self.train_model(product)

        # Predict the next price
        future = self.models[product].make_future_dataframe(periods=1)
        forecast = self.models[product].predict(future)
        predicted_price = forecast['yhat'].values[-1]

        return predicted_price

    def run(self, state: TradingState) -> Dict[str, List[Order]]:
        orders = {}
        for product, order_depth in state.order_depths.items():
            orders[product] = self.place_orders(order_depth, product)
        return orders

    def place_orders(self, order_depth: OrderDepth, product: str) -> List[Order]:
        """
        Place buy and sell orders based on the order depth and predicted price for the product.
        """
        orders = []
        if not order_depth.buy_orders and not order_depth.sell_orders:
            logging.warning(f"No buy or sell orders available for {product}")
            return orders

        if order_depth.buy_orders:  # Ensure there are buy orders
            latest_price = max(order_depth.buy_orders.keys())
            self.update_price_history(product, latest_price)

        predicted_price = self.predict_price(product)
        logging.info(f"Predicted price for {product}: {predicted_price:.2f}")

        if order_depth.sell_orders:
            best_ask, best_ask_amount = next(iter(order_depth.sell_orders.items()))
            if best_ask < predicted_price:
                logging.info(f"BUY {-best_ask_amount}x {product} @ {best_ask}")
                orders.append(Order(product, best_ask, -best_ask_amount))

        if order_depth.buy_orders:
            best_bid, best_bid_amount = next(iter(order_depth.buy_orders.items()))
            if best_bid > predicted_price:
                logging.info(f"SELL {best_bid_amount}x {product} @ {best_bid}")
                orders.append(Order(product, best_bid, best_bid_amount))

        return orders