from datamodel import OrderDepth, UserId, TradingState, Order
from typing import List


class Trader:
    POSITION_LIMIT = 15# The maximum absolute value of the position

    def run(self, state: TradingState):
        print("traderData: " + state.traderData)
        print("Observations: " + str(state.observations))
        result = {}
        threshold_price = 10000  # Price threshold for buying or selling

        # Process AMETHYSTS according to the existing logic
        if 'AMETHYSTS' in state.order_depths:
            order_depth: OrderDepth = state.order_depths['AMETHYSTS']
            orders: List[Order] = []

            # Process sell orders if any bid price is higher than the threshold
            if len(order_depth.buy_orders) != 0:
                best_bid, best_bid_amount = list(order_depth.buy_orders.items())[0]
                if int(best_bid) > threshold_price:
                    print("SELL", str(best_bid_amount) + "x", best_bid)
                    orders.append(Order('AMETHYSTS', best_bid, best_bid_amount))  # Selling all available volume

            # Process buy orders if any ask price is lower than the threshold
            if len(order_depth.sell_orders) != 0:
                best_ask, best_ask_amount = list(order_depth.sell_orders.items())[0]
                if int(best_ask) < threshold_price:
                    print("BUY", str(-best_ask_amount) + "x", best_ask)
                    orders.append(Order('AMETHYSTS', best_ask, -best_ask_amount))  # Buying all available volume

            result['AMETHYSTS'] = orders

        # Process STARFRUIT according to the new logic
        if 'STARFRUIT' in state.order_depths:
            order_depth: OrderDepth = state.order_depths['STARFRUIT']
            starfruit_orders: List[Order] = []

            # Extract the best bid and best ask
            best_bid = max(order_depth.buy_orders, key=lambda price: int(price), default=None)
            best_ask = min(order_depth.sell_orders, key=lambda price: int(price), default=None)

            position = state.positions.get('STARFRUIT', 0)

            # Decide whether to buy or sell based on the threshold_price and position limit
            if position <= self.POSITION_LIMIT:
                if best_ask and int(best_ask) < threshold_price:
                    best_ask_amount = order_depth.sell_orders[best_ask]
                    buy_amount = min(best_ask_amount, self.POSITION_LIMIT - position)
                    starfruit_orders.append(Order('STARFRUIT', best_ask, buy_amount))

            if position >= -self.POSITION_LIMIT:
                if best_bid and int(best_bid) > threshold_price:
                    best_bid_amount = order_depth.buy_orders[best_bid]
                    sell_amount = min(best_bid_amount, self.POSITION_LIMIT + position)
                    starfruit_orders.append(Order('STARFRUIT', best_bid, -sell_amount))

            result['STARFRUIT'] = starfruit_orders

        # Update the trader state data if needed
        traderData = "SAMPLE"
        conversions = None  # Placeholder for conversions value
        return result, conversions, traderData