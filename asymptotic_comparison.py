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


# arr_rate_exp = 0.9
dep_rate_exp = 1
total_jobs = 2**20

throwaway = 2**13
num_server = 50
# jsq_n = 2

x = list(range(700,940,5))
y = list(range(940,1000,1))
z = x + y
arr_rates = []
arr_rates[:] = [i/1000 for i in z]
print(arr_rates)
art_jsq = []
art_jsq2 = []
# art_jsq3 = []
for arr_rate in arr_rates:
    print(arr_rate)
    res_jsq = simulate.simulate(arr_rate,dep_rate_exp,total_jobs,n_identical,num_server)
    res_jsq2 = simulate.simulate(arr_rate,dep_rate_exp,total_jobs,n_identical,num_server,2)
    # res_jsq3 = simulate.simulate(arr_rate,dep_rate_exp,total_jobs,n_identical,num_server,3)
    art_jsq.append(np.mean(res_jsq[throwaway:]))
    art_jsq2.append(np.mean(res_jsq2[throwaway:]))
    # art_jsq3.append(np.mean(res_jsq3[throwaway:]))

jsq2_div2 = []
# jsq3_div2 = []
jsq2_div2[:] = [i / 2 for i in art_jsq2]
# jsq3_div2[:] = [i / 2 for i in art_jsq3]

plt.gcf().set_size_inches(30,20)
plt.plot(arr_rates,art_jsq,label="jsq")
plt.plot(arr_rates,art_jsq2,label="jsq_2")
plt.plot(arr_rates, jsq2_div2, label='jsq_2/2')
plt.xlabel('$\lambda$, arrival rate')
plt.ylabel('ART (average response time)')
plt.title("ART v. Arrival Rate \n $n=2^20$, $s=50$, step = 0.001")
plt.legend(loc="best")

plt.savefig("JSQs2_2^20_.999_HD",format='png',dpi=300)
plt.show()

# plt.clf()
#
# plt.plot(arr_rates,art_jsq,label="jsq")
# plt.plot(arr_rates,art_jsq2,label="jsq_2")
# plt.plot(arr_rates,art_jsq3,label="jsq_3")
# plt.plot(arr_rates, jsq2_div2, label='jsq_2/2')
# plt.plot(arr_rates, jsq3_div2, label='jsq_3/2')
#
# plt.xlabel('$\lambda$, arrival rate')
# plt.ylabel('ART (average response time)')
# plt.title("ART v. Arrival Rate \n $n=2^20$, $s=50$")
# plt.gcf().set_size_inches(30,20)
# plt.legend(loc="best")
#
# plt.savefig("JSQs23_2^20_.999_HD",format='png',dpi=300)
# plt.show()