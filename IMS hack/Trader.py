from datamodel import OrderDepth, UserId, TradingState, Order
from typing import List

class Trader:
    def __init__(self):
        self.price_history = {'AMETHYSTS': [], 'STARFRUIT': []}

    def update_price_history(self, product: str, new_price: float):
        """Adds the latest price to the product's price history."""
        self.price_history[product].append(new_price)
        # Optional: Trim the history to the last N prices to save memory
        max_history_size = 500  # For example, keep the last 100 prices
        self.price_history[product] = self.price_history[product][-max_history_size:]
    def calculate_ema(self, prices, span=100):
        """
        Calculate the Exponential Moving Average (EMA) for a list of prices.
        :param prices: List of prices (floats or integers).
        :param span: The time span for the EMA.
        :return: The EMA of the provided prices.
        """
        if not prices:
            return None
        ema = [prices[0]]  # Start EMA with the first price
        alpha = 2 / (span + 1)  # The smoothing factor
        for price in prices[1:]:
            ema.append((price - ema[-1]) * alpha + ema[-1])
        return ema[-1]

    def calculate_volatile_product_price(self, product: str) -> int:
        """
        Calculate the acceptable price for a volatile product using Exponential Moving Average (EMA).
        """
        prices = self.price_history[product]
        if len(prices) < 10:  # Ensuring there's enough data to calculate EMA
            return 4000  # Default price if not enough data
        else:
            ema_price = self.calculate_ema(prices)
            return int(ema_price) if ema_price else 5000


    def run(self, state: TradingState) -> tuple[dict[Symbol, list[Order]], int, str]:
        orders = {}
        conversions = 0
        trader_data = ""

        for product, order_depth in state.order_depths.items():
            orders[product] = []
            if order_depth.buy_orders:  # Ensure there are buy orders
                latest_price = max(order_depth.buy_orders.keys())
                self.update_price_history(product, latest_price)
                print("latest price: ", latest_price)
            else:
                latest_price = None

            if product == 'AMETHYSTS':
                acceptable_price = 10000
            else:
                acceptable_price = self.calculate_volatile_product_price(product)

            logger.print("Acceptable  price : " + str(acceptable_price))

            if len(order_depth.sell_orders) != 0:
                best_ask, best_ask_amount = list(order_depth.sell_orders.items())[0]
                if int(best_ask) < acceptable_price:
                    logger.print("BUY", str(-best_ask_amount) + "x", best_ask)
                    orders[product].append(Order(product, best_ask, -best_ask_amount))

            if len(order_depth.buy_orders) != 0:
                best_bid, best_bid_amount = list(order_depth.buy_orders.items())[0]
                if int(best_bid) > acceptable_price:
                    logger.print("SELL", str(best_bid_amount) + "x", best_bid)
                    orders[product].append(Order(product, best_bid, -best_bid_amount))

        logger.flush(state, orders, conversions, trader_data)
        return orders, conversions, trader_data