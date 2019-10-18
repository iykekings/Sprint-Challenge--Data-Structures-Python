class RingBuffer:
  def __init__(self, capacity: int):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    #  Overwrites the oldest element in the storage
    self.storage[self.current % self.capacity] = item
    # Increment current
    self.current += 1

  def get(self):
    return list(filter(None ,self.storage))


buffer = RingBuffer(3)

buffer.append('a')
print(buffer.get())
buffer.append('b')
print(buffer.get())
buffer.append('c')
print(buffer.get())
