
class Job:
    ID = 0
    def __init__(self,resource_req,arr_time,server=None, dep_time = None):
        self.arr_time = arr_time
        self.server = server
        self.req_list = resource_req
        self.ID = Job.ID


    def __str__(self):
        return "Job[" + "ID:" + self.ID.__str__() + ", size:" + self.size.__str__() + ", arr:" + self.arr_time.__str__() + ", server:" + self.server.__str__() + "]"

    def assign_server(self,server):
        self.server=server

    def assign_departure_time(self,dep_time):
        self.dep_time = dep_time




# print(Job(5,2,4))