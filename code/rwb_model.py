#!/bin/python
#-----------------------------------------------------------------------------
# File Name : rwb_model.py
# Author: Emre Neftci
#
# Creation Date : Mon 01 Apr 2019 11:03:48 AM PDT
# Last Modified : 
#
# Copyright : (c) UC Regents, Emre Neftci
# Licence : GPLv2

#----------------------------------------------------------------------------- 
import numpy as np
from pylab import *
def rwb(std, drift, crit, n_reps = 500, T = 1000):
    latencies = np.empty([n_reps], dtype='int')
    responses = np.empty([n_reps], dtype='int')
    evidences = np.empty([T, n_reps])

    for n in range(n_reps):
        evidences[:,n] = np.cumsum(np.random.normal(drift, std, size=T))
        latencies[n] = np.where(np.abs(evidences[:,n])>crit)[0][0]
        responses[n] = np.sign(evidences[latencies[n],n])
        evidences[latencies[n]:,n] = np.sign(evidences[latencies[n],n])*crit

    return latencies, responses, evidences 

if __name__ == "__main__":
    #Experimental
    n_reps = 1000
    T = 1000

    #Parameters
    std = .3
    drift = .03
    crit = 3

    latencies, responses, evidences = rwb(std, drift, crit, n_reps, T)

    meanlRT = latencies[responses == 1].mean()
    meanrRT = latencies[responses == -1].mean()
    accuracy = (responses==1).mean()

    figure()
    subplot(211)
    plot(evidences, color='k', alpha=.5)
    ylabel("$Z_T$")
    xlim([0,T])
    subplot(212)
    hist(latencies)
    xlabel('RT')
    ylabel('Count')
    xlim([0,T])
    tight_layout()
    savefig('../slides/img/rwb_model_all_latencies_drift{0}.png'.format(str(drift).replace('.','_')))

    figure()
    subplot(311)
    plot(evidences, color='k', alpha=.5)
    ylabel("$Z_T$")
    xlim([0,T])
    subplot(312)
    hist(latencies[responses == -1], label='mean RT = {0:.2}, probability = {1:.2}'.format(meanrRT,1-accuracy),bins = range(0,T,50))
    xlabel('RT')
    ylabel('Count (right)')
    xlim([0,T])
    legend()
    subplot(313)
    hist(latencies[responses == 1], label='mean RT = {0:.2}, probility = {1:.2}'.format(meanlRT,accuracy),bins = range(0,T,50))
    xlabel('RT')
    ylabel('Count (left)')
    xlim([0,T])
    legend()
    tight_layout()
    savefig('../slides/img/rwb_model_lr_latencies_drift{0}.png'.format(str(drift).replace('.','_')))
    show()

