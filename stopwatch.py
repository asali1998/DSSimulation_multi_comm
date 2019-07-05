class Stopwatch:
    def __init__(self):
        self.cumulative = 0
        self.is_running = False
        self.last_checkpoint = 0

    def start(self,curr):
        if self.is_running == True:
            return
        self.is_running = True
        self.last_checkpoint = curr

    def pause(self,curr):
        if self.is_running == False:
            return
        self.is_running = False
        self.cumulative += curr - self.last_checkpoint
        self.last_checkpoint = curr

    def read(self):
        return self.cumulative