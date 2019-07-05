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


arr_rate_exp = 0.9
dep_rate_exp = 1
# total_jobs = 100000

throwaway_ratio = 0.01
# throwaway = 2000
num_server = 50
jsq_n = 2

x_log2 = list(range(10,25))
total_jobs = 2**24
y_art_jsq = []
y_art_jsq2 = []

y_art_jsq_master = simulate.simulate(arr_rate_exp, dep_rate_exp, total_jobs, n_identical, num_server)
y_art_jsq2_master = simulate.simulate(arr_rate_exp, dep_rate_exp, total_jobs, n_identical, num_server, jsq_n)

print(len(y_art_jsq_master))
print(len(y_art_jsq2_master))

for power in x_log2:
    start_index = math.floor((2 ** power)* throwaway_ratio)
    end_index = min(2 ** power,len(y_art_jsq2_master),len(y_art_jsq_master))
    y_art_jsq.append(np.mean(y_art_jsq_master[start_index:end_index]))
    y_art_jsq2.append(np.mean(y_art_jsq2_master[start_index:end_index]))

plt.gcf().set_size_inches(9,6)
plt.plot(x_log2,y_art_jsq,label="jsq")
plt.plot(x_log2,y_art_jsq2,label="jsq_2")
plt.xlabel('log$_2$ $x$ , $x$ = num_jobs')
plt.ylabel('ART (average response time)')
plt.title("Sentivity: ART v. num_jobs \n s=50,$\lambda=0.9$")
plt.legend(loc="best")
plt.savefig("sensitivity_2^24_50_0.9.png",dpi=300)
plt.show()


