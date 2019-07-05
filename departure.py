class Departure:
    def __init__(self,job,dep_time):
        self.job = job
        # print(job.arr_time)
        self.dep_time = dep_time

    def __lt__(self, other):
        if self.dep_time < other.dep_time:
            return True
        return False

    def __lq__(self, other):
        if self.dep_time <= other.dep_time:
            return True
        return False

    def __eq__(self, other):
        if self.dep_time == other.dep_time:
            return True
        return False

    def __gt__(self, other):
        if self.dep_time > other.dep_time:
            return True
        return False

    def __ge__(self, other):
        if self.dep_time >= other.dep_time:
            return True
        return False

    def __str__(self):
        return "Depature {" + self.job.__str__() + ", time:" + self.dep_time.__str__() + "}"


# event = Event(job.Job(1,2,3),2,1)
# print(event)