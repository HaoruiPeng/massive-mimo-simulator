import os
import numpy as np
from multiprocessing import Pool
import json
import time

PROCESSES = 4


simulations = []


SEED = round(time.time() / 10)

s2 = "FCFS"
s1 = "FCFS"
#
# period_vars = np.linspace(0.01, 0.15, 15)
# deadline_vars = np.linspace(0.01, 0.15, 15)
# ratios = np.linspace(0.3, 1.7, 15)
# variance_vars = np.linspace(0.05, 0.5, 15)

# no_urllc_list = [60, 90, 150]

# for deadline_vars in deadline_vars:
#     for ratio in ratios:
#         for no_urllc in no_urllc_list:
#             for period_var in period_vars:
#                 for variance_var in variance_vars:
#                     SEED += np.random.randint(100)
#                     simulations.append("python3 main.py \
#                                         --ratio {} --deadline_var {} \
#                                         --period_var {} --variance_var {} \
#                                         --urllc_node {} \
#                                         --mu {} --seed {}".format(ratio, deadline_var, period_var, variance_var, no_urllc, mu, SEED))
mu_list = [0, 3.12, 6.9 ,9.3]
ratios = [1.0]
no_urllc = 180
period_var = 0.04
deadline_var = 0.02
variance_var = 0.08
SEED = 1025

for ratio in ratios:
    for mu in mu_list:
        simulations.append("python3 main.py \
                            --ratio {} --deadline_var {} \
                            --period_var {} --variance_var {} \
                            --urllc_node {} \
                            --mu {} --seed {}".format(ratio, deadline_var, period_var, variance_var, no_urllc, mu, SEED))

pool = Pool(processes=PROCESSES)
for k, simulation in enumerate(simulations):
    pool.apply_async(os.system, (simulation,))

pool.close()
pool.join()
print("All simulations completed!")