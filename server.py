import stopwatch
import departure as dep
import heapq

class Server:

    def __init__(self, resource_list):
        #taskQueue[0] is the ongoing job (also in departures)
        self.taskQueue = []
        self.resource_list = resource_list
        self.idle_swatch = stopwatch.Stopwatch()
        self.idle_swatch.start(0)
        self.is_idle = True

    def add_job(self, job, departures, arr_time):
        # if server is idle, push the current job onto departures queue
        if len(self.taskQueue) == 0:
            # print(len(job.req_list))
            # print(len(self.resource_list))
            departure_time = arr_time + max([req/res for req, res in zip(job.req_list, self.resource_list)])
            heapq.heappush(departures, dep.Departure(job, departure_time))
            self.idle_swatch.pause(arr_time)

        job.assign_server(self)
        self.taskQueue.append(job)


    def next_job(self, departures, start_time):
        self.taskQueue.pop(0)
        if(len(self.taskQueue) == 0):
            self.idle_swatch.start(start_time)
        else:
            new_dep = dep.Departure(self.taskQueue[0], start_time +
                                    max([req/res for req, res in zip(self.taskQueue[0].req_list, self.resource_list)]))
            heapq.heappush(departures, new_dep)

    def start_idle_timer(self,time_curr):
        self.is_idle = True
        self.idle_swatch.start(time_curr)


