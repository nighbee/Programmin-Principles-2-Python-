from datamodel import OrderDepth, UserId, TradingState, Order
from typing import List


class Trader:
    POSITION_LIMIT = 20  # The maximum absolute value of the position

    def __init__(self):
        self.threshold_prices = {
            'AMETHYSTS': {
                'buy': 9000,
                'sell': 9996
            },
            'STARFRUIT': {
                'buy': 4980,
                'sell': 5000
            }
        }

    def run(self, state: TradingState):
        print("traderData: " + state.traderData)
        print("Observations: " + str(state.observations))
        result = {}

        # Process AMETHYSTS
        if 'AMETHYSTS' in state.order_depths:
            order_depth: OrderDepth = state.order_depths['AMETHYSTS']
            orders: List[Order] = []
            buy_threshold = self.threshold_prices['AMETHYSTS']['buy']
            sell_threshold = self.threshold_prices['AMETHYSTS']['sell']

            # Process sell orders if any bid price is higher than the sell threshold
            if len(order_depth.buy_orders) != 0:
                best_bid, best_bid_amount = list(order_depth.buy_orders.items())[0]
                if int(best_bid) > sell_threshold:
                    print("SELL", str(best_bid_amount) + "x", best_bid)
                    orders.append(Order('AMETHYSTS', best_bid, best_bid_amount))  # Selling all available volume

            # Process buy orders if any ask price is lower than the buy threshold
            if len(order_depth.sell_orders) != 0:
                best_ask, best_ask_amount = list(order_depth.sell_orders.items())[0]
                if int(best_ask) < buy_threshold:
                    print("BUY", str(-best_ask_amount) + "x", best_ask)
                    orders.append(Order('AMETHYSTS', best_ask, -best_ask_amount))  # Buying all available volume

            result['AMETHYSTS'] = orders

        # Process STARFRUIT
        if 'STARFRUIT' in state.order_depths:
            order_depth: OrderDepth = state.order_depths['STARFRUIT']
            starfruit_orders: List[Order] = []
            current_position = state.position.get('STARFRUIT', 0)  # Get the current position for STARFRUIT
            buy_threshold = self.threshold_prices['STARFRUIT']['buy']
            sell_threshold = self.threshold_prices['STARFRUIT']['sell']

            # Extract the best bid and best ask
            best_bid = max(order_depth.buy_orders, key=lambda price: int(price), default=None)
            best_ask = min(order_depth.sell_orders, key=lambda price: int(price), default=None)

            # Decide whether to buy or sell based on the threshold prices and position limit
            if best_ask and int(best_ask) < buy_threshold:
                best_ask_amount = order_depth.sell_orders[best_ask]
                buy_amount = min(best_ask_amount,
                                 self.POSITION_LIMIT - current_position)  # Do not exceed position limit
                if buy_amount > 0:
                    starfruit_orders.append(Order('STARFRUIT', best_ask, buy_amount))

            elif best_bid and int(best_bid) > sell_threshold:
                best_bid_amount = order_depth.buy_orders[best_bid]
                sell_amount = min(best_bid_amount,
                                  self.POSITION_LIMIT + current_position)  # Do not exceed position limit
                if sell_amount > 0:
                    starfruit_orders.append(Order('STARFRUIT', best_bid, -sell_amount))

            result['STARFRUIT'] = starfruit_orders

        # Update the trader state data if needed
        traderData = "SAMPLE"
        conversions = None  # Placeholder for conversions value
        return result, conversions, traderData