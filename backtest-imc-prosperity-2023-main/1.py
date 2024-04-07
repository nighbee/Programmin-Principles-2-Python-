from datamodel import OrderDepth, UserId, TradingState, Order
from typing import List


class Trader:
    POSITION_LIMIT = 15  # The maximum absolute value of the position
    AMETHYSTS_BUY_THRESHOLD = 9950  # Price threshold for buying AMETHYSTS
    AMETHYSTS_SELL_THRESHOLD = 10500  # Price threshold for selling AMETHYSTS
    STARFRUIT_BUY_THRESHOLD = 4800  # Price threshold for buying STARFRUIT
    STARFRUIT_SELL_THRESHOLD = 4950  # Price threshold for selling STARFRUIT

    def run(self, state: TradingState):
        print("traderData: " + state.traderData)
        print("Observations: " + str(state.observations))
        result = {}

        # Process AMETHYSTS according to the new logic
        if 'AMETHYSTS' in state.order_depths:
            amethysts_orders: List[Order] = []
            self.process_coin('AMETHYSTS', state, amethysts_orders, self.AMETHYSTS_BUY_THRESHOLD,
                              self.AMETHYSTS_SELL_THRESHOLD)
            result['AMETHYSTS'] = amethysts_orders

        # Process STARFRUIT according to the new logic
        if 'STARFRUIT' in state.order_depths:
            starfruit_orders: List[Order] = []
            self.process_coin('STARFRUIT', state, starfruit_orders, self.STARFRUIT_BUY_THRESHOLD,
                              self.STARFRUIT_SELL_THRESHOLD)
            result['STARFRUIT'] = starfruit_orders

        # Update the trader state data if needed
        traderData = "SAMPLE"
        conversions = None  # Placeholder for conversions value
        return result, conversions, traderData

    def process_coin(self, coin: str, state: TradingState, orders: List[Order], buy_threshold: int,
                     sell_threshold: int):
        order_depth: OrderDepth = state.order_depths[coin]
        best_bid = max(order_depth.buy_orders, key=lambda price: int(price), default=None)
        best_ask = min(order_depth.sell_orders, key=lambda price: int(price), default=None)
        position = state.positions.get(coin, 0)

        if position > self.POSITION_LIMIT:
            if best_bid and int(best_bid) > sell_threshold:
                best_bid_amount = order_depth.buy_orders[best_bid]
                sell_amount = min(best_bid_amount, position - self.POSITION_LIMIT)
                orders.append(Order(coin, best_bid, -sell_amount))

        if position < -self.POSITION_LIMIT:
            if best_ask and int(best_ask) < buy_threshold:
                best_ask_amount = order_depth.sell_orders[best_ask]
                buy_amount = min(best_ask_amount, -position - self.POSITION_LIMIT)
                orders.append(Order(coin, best_ask, buy_amount))