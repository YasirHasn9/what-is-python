# Queue
'''
queue is a way of ordering the execution of function in global stack
and what ever the first object/function is will be firs who gets executed 
'''


class Queue:
    def __init__(self, size, storage):
        self.size = size
        self.storage = storage
