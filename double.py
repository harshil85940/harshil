 class Queue:
        DEFAULT_CAPACITY = 10
    def _init_ (self):
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY 
        self._size = 0
        self._front = 0
        self._last = 0

    def len (self):        
        return self. size
        
    def is_empty(self):
        return self._size == 0
        
    def first(self):
        if self.is_empty():
            raise Exception( "Queue is empty" ) 
            return self._data[self._front]

    def dequeue(self):
        if self.is_empty():
            raise Exception( "Queue is empty" )
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data) 
        self._size -= 1
        return answer
       
    def enqueue(self, e):
        if self._size == len(self._data):
            self._resize(2  * len(self._data)) # double the array size 
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1
       
    def   _resize(self, cap): 
        old = self._data
        self._data = [None] * cap 
        walk = self._front
        for k in range(self. size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old) 
        self._front = 0
       
    def dequeuelast(self):
      if self.is_empty():
       raiseException("queue is empty")
      answer = self._data[self._last]
      self._last = [self._last] = None
      self._last = [self._last+1]%len[self._data]
      self._size-=1
      retrun answer
   
   def lastenqueue(self,e):
     if self._size == len(self._data):
      self.resizel(2*len(self._data))
      availl = (self._last + self._size)%len(self._data)
      self._data[availl] = e
      self._size += 1
    
   def resizel(self,capp):
     old = self._data
     self._data = [None]*capp
     New = self._last
    for i in range(self._size):
      self._data[i] = old[New]
      New = [1 + New] % len(old)
      self._last = 0
   
