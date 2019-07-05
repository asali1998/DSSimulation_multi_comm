import simulate
import numpy as np
import server
import matplotlib.pyplot as plt
import math

def n_identical(n = 2):
    server_list = []
    for i in range(n):
        server_list.append(server.Server())
    return server_list


arr_rate_exp = 0.98
dep_rate_exp = 1
total_jobs = 2**20

throwaway = 2**12
# num_server = 50
jsq_n = 2

t = list(range(0,46))
list_num_server = []
list_num_server[:]=[round(1.2**i) for i in t]
art = []
art_jsq2 = []

for num_server in list_num_server:
    print(num_server)
    res = simulate.simulate(arr_rate_exp,dep_rate_exp,total_jobs,n_identical,num_server)
    art.append(np.mean(res[throwaway:]))
    res_jsq2 = simulate.simulate(arr_rate_exp,dep_rate_exp,total_jobs,n_identical,num_server,jsq_n)
    art_jsq2.append(np.mean(res_jsq2[throwaway:]))


plt.plot(t,art,label='JSQ')
plt.plot(t,art_jsq2,label='JSQ-2')
print(art)
print(art_jsq2)
plt.xlabel('$log_{1.2} s$, s = number of servers')
plt.ylabel('ART (average response time)')
plt.title("Number of servers v. ART \n $\lambda=0.98$, $n=2^{20}$")
plt.legend(loc="best")
plt.savefig("servers_2^20_0_45_0.98_jsqs2_exp1.2.png",dpi=300)
plt.show()
