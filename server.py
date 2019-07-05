import stopwatch
import departure as dep
import heapq

class Server:

    def __init__(self):
        #taskQueue[0] is the ongoing job (also in departures)
        self.taskQueue = []
        self.idle_swatch = stopwatch.Stopwatch()
        self.idle_swatch.start(0)
        self.is_idle = True

    def add_job(self, job, departures, arr_time):
        # if server is idle, push the current job onto departures queue
        if len(self.taskQueue) == 0:
            heapq.heappush(departures, dep.Departure(job, job.size + arr_time))
            self.idle_swatch.pause(arr_time)

        job.assign_server(self)
        self.taskQueue.append(job)


    def next_job(self, departures, start_time):
        self.taskQueue.pop(0)
        if(len(self.taskQueue) == 0):
            self.idle_swatch.start(start_time)
        else:
            new_dep = dep.Departure(self.taskQueue[0], start_time + self.taskQueue[0].size)
            heapq.heappush(departures, new_dep)

    def start_idle_timer(self,time_curr):
        self.is_idle = True
        self.idle_swatch.start(time_curr)


