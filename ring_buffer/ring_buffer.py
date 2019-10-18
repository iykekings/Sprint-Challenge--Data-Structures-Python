class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    # #  if capacity has been reached
    # if(self.current + 1 == self.capacity):
    #   # replace the item after current index in the storage
    #   self.storage.insert(0, item)
    #   #  reset self.current to 1
    #   self.current = 1
    # else:
    #   self.storage.insert(self.current, item)
    # # Increment self.current
    # self.current += 1
    self.storage[self.current % self.capacity] = item
    self.current += 1

  def get(self):
    return self.storage


ike = RingBuffer(3)
ike.append(2)
ike.append(1)
ike.append(4)
ike.append(5)
ike.append(7)
ike.append(5)
ike.append(6)