import server


class ServerCluster:

    def __init__(self,num_servers):
        self.serverList=[]

    def add_server(self,new_server):
        self.serverList.append(new_server)

    ######UPDATE########
    def find_next_server(self,task):
        return self.serverList[0]

    def add_job(self, timer, job):
        self.find_next_server(job).add_job()
        return



