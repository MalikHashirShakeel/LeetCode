class StockSpanner:

    def __init__(self):
        self._arr = list()

    def next(self, price: int) -> int:
        self._arr.append(price)
        span = 0

        for item_price in self._arr[::-1]:
            if item_price > price:
                break
            else:
                span += 1

        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)