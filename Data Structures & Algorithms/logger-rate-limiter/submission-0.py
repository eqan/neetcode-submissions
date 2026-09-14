class Logger:

    def __init__(self):
        self.logger = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        # Case 1: add message to print
        if message not in self.logger:
            self.logger[message] = timestamp
            return True

        # Case 2: Update timestamp of the message 
        if timestamp - self.logger[message] >= 10:
            self.logger[message] = timestamp
            return True
        else:
            return False



# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
