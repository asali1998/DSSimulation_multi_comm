class Timer:
    def __init__(self):
        self.current_time=0

    def increment(self,increment):
        self.current_time += increment
        return self.current_time

    def sync(self, new_time):
        if new_time >= self.current_time:
            self.current_time = new_time
            # print("time synced: " + self.current_time.__str__())
        else:
            print("current time: " + self.current_time.__str__() )
            print("new_time: " + new_time.__str__())
            raise ValueError("Decrement not allowed:")


    def get_current_time(self):
        return self.current_time

    def put_stamp(self,code):
        return

    def reset(self):
        self.current_time = 0


