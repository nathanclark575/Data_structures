from collections import deque

# append for stack, appendleft for queue

stock_price_queue = deque()

stock_price_queue.appendleft({"one" : 1})
stock_price_queue.appendleft(10)
stock_price_queue.appendleft(11)

print(stock_price_queue)

print(stock_price_queue.pop())
print(stock_price_queue.pop())
print(stock_price_queue.pop())

print(stock_price_queue)