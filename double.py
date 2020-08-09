 class ArrayQueue:
        DEFAULT_CAPACITY = 10
    # moderate capacity for all new queues
    def _init_ (self):
        '''Create an empty queue.'''
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY 
        self._size = 0
        self._front = 0
        self._last = 0

    def len (self):        
        '''Return the number of elements in the queue.'''
        return self. size
        
    def is_empty(self):
        '''Return True if the queue is empty.'''
        return self._size == 0
        
    def first(self):
        '''Return (but do not remove) the element at the front of the queue. Raise Empty exception if the queue is empty'''
        if self.is_empty():
            raise Exception( "Queue is empty" ) 
            return self._data[self._front]

    def dequeue(self):
        '''Remove and return the first element of the queue (i.e., FIFO).Raise Empty exception if the queue is empty. '''
        if self.is_empty():
            raise Exception( "Queue is empty" )
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data) 
        self._size -= 1
        return answer
        # help garbage collection
        
        '''
        
        [1,None,3,4] => front 2, size : 3
        dequeue()
        
        answer = 3
         [1,None,None,4]
         front = 3%4 = 3 =====10 % 7 = 3,4,5,6,0,1, =======
         size = 2 
         return answer 
         
         4%4 =0
         '''
    def enqueue(self, e):
        
        '''Add an element to the back of queue.'''
        if self._size == len(self._data):
            self._resize(2  * len(self._data)) # double the array size 
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1
        
        
        
    def   _resize(self, cap): 
        # we assume cap >= len(self) 
        '''Resize to a new list of capacity >= len(self).'''
        old = self._data
        self._data = [None] * cap 
        walk = self._front
        for k in range(self. size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old) 
        self._front = 0
        # keep track of existing list
        # allocate list with new capacity
        # only consider existing elements # intentionally shift indices

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
   
