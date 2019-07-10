 # import server_cluster as sc
import server
import timer as tm
import numpy as np
import job as j
import departure as dep
import heapq
import math
import statistics
import random
import matplotlib.pyplot as plt

##############################
# Variable Parameters
# #   1. Interarrival Time
# #   2. Task Size
##############################

def next_inter_arrival_time(distribution, arr_rate_exp, std = 0.01):
    if distribution == DISTRIBUTION_GAU:
        return max(1/np.random.normal(arr_rate_exp,std),np.nextafter(0,1))
    if distribution == DISTRIBUTION_EXP:
        return np.random.exponential(1 / arr_rate_exp)


def next_job_req(distribution, dep_rate_exp, std = 0.01):
    # if distribution == DISTRIBUTION_GAU:
    #     return max(1/np.random.normal(dep_rate_exp,std),np.nextafter(0,1))
    # if distribution == DISTRIBUTION_EXP:
    return [np.random.exponential(1 / dep_rate_exp)] * 2


#UPDATE
# def find_next_server():
#     return server_list[0]
def find_next_server_rand(server_list):
    return server_list[np.random.randint(len(server_list))]


def find_next_server_jsq_n(server_list,n = 2):
    if len(server_list) <= n:
        return find_next_server_jsq(server_list)
    server_ids = list(range(len(server_list)))
    rand_ids = []
    for i in range(n):
        rand_id = server_ids[np.random.randint(len(server_ids))]
        server_ids.remove(rand_id)
        rand_ids.append(rand_id)
    min_length = float('inf')
    min_id = -1
    for i in range(n):
        if len(server_list[rand_ids[i]].taskQueue) < min_length:
            min_id = rand_ids[i]
            min_length = len(server_list[rand_ids[i]].taskQueue)
    # tracker_jsqn[min_id] += 1
    return server_list[min_id]



def find_next_server_jsq(server_list):
    running_min = float("inf")
    min_ID = -1
    for i in range(len(server_list)):
        if len(server_list[i].taskQueue) < running_min:
            running_min = len(server_list[i].taskQueue)
            min_ID = i
    return server_list[min_ID]



#UPDATE
def n_identical(n = 2):
    server_list = []
    for i in range(n):
        server_list.append(server.Server([1,1]))
    return server_list

DISTRIBUTION_EXP = "exponential"
DISTRIBUTION_GAU = "gaussian"
##############################
#
# Simulation Starts
#
##############################

# @Param:
#   Required:
#       arr_rate: average rate of job arrivals per server (simulate() will scale it by num_server to get aggregated arrival rate


def simulate(arr_rate, dep_rate_exp, total_jobs, server_farm_init_func, num_server = 2, num_sample = None):
    if num_sample == None:
        num_sample = num_server
    departures = []
    server_list = server_farm_init_func(num_server)
    arr_rate_exp_aggr = arr_rate * num_server
    response_times = []
    timer = tm.Timer()
    for i in range(total_jobs):
        next_arrival_inter = next_inter_arrival_time(DISTRIBUTION_EXP, arr_rate_exp_aggr)
        next_arrival_abs = timer.current_time + next_arrival_inter

        while (len(departures) > 0) and (departures[0].dep_time <= next_arrival_abs):
            response_times.append(departures[0].dep_time - departures[0].job.arr_time)
            timer.sync(departures[0].dep_time)
            departures[0].job.server.next_job(departures, timer.current_time)
            heapq.heappop(departures)

        job_arr = j.Job(next_job_req(DISTRIBUTION_EXP, dep_rate_exp), next_arrival_abs)
        timer.sync(next_arrival_abs)
        find_next_server_jsq_n(server_list,num_sample).add_job(job_arr, departures, timer.current_time)
    return response_times


# def simulate_jsqn(arr_rate_exp, dep_rate_exp, total_jobs, throwaway, server_farm_init_func, num_server = 2, jsq_n = None):
#     departures = []
#     server_list = server_farm_init_func(num_server)
#     arr_rate_aggr = arr_rate_exp * num_server
#     response_times = []
#     timer = tm.Timer()
#     for i in range(total_jobs):
#         # print("i: " + i.__str__())
#         next_arrival_inter = next_inter_arrival_time(DISTRIBUTION_EXP, arr_rate_aggr)
#         next_arrival_abs = timer.current_time + next_arrival_inter
#
#         while (len(departures) > 0) and (departures[0].dep_time <= next_arrival_abs):
#             response_times.append(departures[0].dep_time - departures[0].job.arr_time)
#             timer.sync(departures[0].dep_time)
#             departures[0].job.server.next_job(departures, timer.current_time)
#             heapq.heappop(departures)
#
#         job_arr = j.Job(next_job_size(DISTRIBUTION_EXP, dep_rate_exp), next_arrival_inter, next_arrival_abs)
#         timer.sync(next_arrival_abs)
#         find_next_server_jsq_n(server_list,10).add_job(job_arr, departures, timer.current_time)
#     return response_times

# Parameters
arr_rate_exp = 0.9
dep_rate_exp = 1
total_jobs = 100000

throwaway_ratio = 0.05
throwaway = 2000
num_server = 50
jsq_n = 2
#
responses = simulate(arr_rate_exp, dep_rate_exp, total_jobs, n_identical, num_server)
responses_jsq2 = simulate(arr_rate_exp, dep_rate_exp, total_jobs, n_identical, num_server, jsq_n)
print(len(responses))
print(len(responses_jsq2))
print(np.mean(responses[throwaway:]))
print(np.mean(responses_jsq2[throwaway:]))

# x_log2 = list(range(6,22))
# total_jobs = 2**21
# y_art_jsq = []
# y_art_jsq2 = []
#
# y_art_jsq_master = simulate(arr_rate_exp, dep_rate_exp, total_jobs, n_identical, num_server)[throwaway:]
# y_art_jsq2_master = simulate(arr_rate_exp, dep_rate_exp, total_jobs, n_identical, num_server, jsq_n)[throwaway:]
#
# print(len(y_art_jsq_master))
# print(len(y_art_jsq2_master))
#
# for power in x_log2:
#     start_index = math.floor((2 ** power)* throwaway_ratio)
#     end_index = min(2 ** power,len(y_art_jsq2_master),len(y_art_jsq_master))
#     print("#" + power.__str__()+": start"+start_index.__str__())
#     print("#" + power.__str__()+": end  "+end_index.__str__())
#     y_art_jsq.append(np.mean(y_art_jsq_master[start_index:end_index]))
#     y_art_jsq2.append(np.mean(y_art_jsq2_master[start_index:end_index]))
#
#
# plt.plot(x_log2,y_art_jsq)
# plt.plot(x_log2,y_art_jsq2)
# plt.xlabel('log$_2$ $x$ , $x$ = num_jobs')
# plt.ylabel('ART (average response time)')
# plt.title("Sentivity testing: \n ART v. num_jobs")
# plt.show()
# plt.savefig("sensitivity.png",dpi=300)
# print(server_list[0].idle_swatch.read())

