
class Job:
    ID = 0
    def __init__(self,size,iat,arr_time,server=None, dep_time = None):
        self.size = size
        self.iat = iat
        self.arr_time = arr_time
        # print(arr_time)
        self.server = server
        self.ID = Job.ID


    def __str__(self):
        return "Job[" + "ID:" + self.ID.__str__() + ", size:" + self.size.__str__() + ", iat:" + self.iat.__str__() + ", arr:" + self.arr_time.__str__() + ", server:" + self.server.__str__() + "]"

    def assign_server(self,server):
        self.server=server

    def assign_departure_time(self,dep_time):
        self.dep_time = dep_time




# print(Job(5,2,4))