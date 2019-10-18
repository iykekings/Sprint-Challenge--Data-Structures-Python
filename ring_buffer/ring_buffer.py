class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    #  Overwrites the oldest element in the storage
    self.storage[self.current % self.capacity] = item
    # Increment current
    self.current += 1

  def get(self):
    return self.storage
