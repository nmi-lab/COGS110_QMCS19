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
import sys
from pylab import *
def rwb(std, drift, crit, sp=0, n_reps = 500, T = 1000):
    if not hasattr(drift, '__len__'):
        drift = np.ones(n_reps)*drift

    if not hasattr(sp, '__len__'):
        sp = np.ones(n_reps)*sp

    latencies = np.empty([n_reps], dtype='int')
    responses = np.empty([n_reps], dtype='int')
    evidences = np.empty([T, n_reps])

    for n in range(n_reps):
        evidences[:,n] = np.cumsum(np.random.normal(drift[n], std, size=T))+sp[n]
        try:
            latencies[n] = np.where(np.abs(evidences[:,n])>crit)[0][0]
        except IndexError:
            latencies[n] = T-1
        responses[n] = np.sign(evidences[latencies[n],n])
        evidences[latencies[n]:,n] = np.sign(evidences[latencies[n],n])*crit

    return latencies, responses, evidences 

if __name__ == "__main__":
    #Experimental
    n_reps = 3000
    T = 500

    #Parameters
    std = .3
    mudrift = float(sys.argv[1])
    std_drift = float(sys.argv[2])
    drift = np.random.normal(mudrift, std_drift, size=[n_reps])
    std_sp = float(sys.argv[3])
    sp = np.random.normal(0, std_sp, size=[n_reps])
    crit = 3

    latencies, responses, evidences = rwb(std, drift, crit, sp, n_reps, T)

    meanRT = latencies.mean()
    meanlRT = latencies[responses == 1].mean()
    meanrRT = latencies[responses == -1].mean()
    accuracy = (responses==1).mean()

    evidences2p = evidences[:,:50]
    responses2p = responses[:50]

    figure()
    subplot(311)
    plot(evidences2p[:,responses2p==1], color='b', alpha=.5)
    plot(evidences2p[:,responses2p==-1], color='r', alpha=.5)
    ylabel("$Z_T$")
    xlim([0,T])
    subplot(312)
    hist(latencies[responses == -1], label='mean RT = {0:.2}, probability = {1:.2}'.format(meanrRT,1-accuracy),bins = range(0,T,25), color='r')
    xlabel('RT')
    ylabel('Count (right)')
    xlim([0,T])
    legend()
    subplot(313)
    hist(latencies[responses == 1], label='mean RT = {0:.2}, probability = {1:.2}'.format(meanlRT,accuracy),bins = range(0,T,25), color='b')
    xlabel('RT')
    ylabel('Count (left)')
    xlim([0,T])
    legend()
    tight_layout()
    savefig('../slides/img/rwbt2t_model_lr_latencies_dirft{0}_stddrift{1}_sp{2}.png'.format(
        str(mudrift).replace('.','_'),
        str(std_drift).replace('.','_'),
        str(std_sp).replace('.','_')))

    figure()
    subplot(211)
    plot(evidences2p[:,responses2p==1], color='b', alpha=.5)
    plot(evidences2p[:,responses2p==-1], color='r', alpha=.5)
    ylabel("$Z_T$")
    xlim([0,T])
    subplot(212)
    hist(latencies, label='mean RT = {0:.2}, probability = {1:.2}'.format(meanRT,accuracy),bins = range(0,T,25))
    xlabel('RT')
    ylabel('Count (left)')
    xlim([0,T])
    legend()
    tight_layout()
    savefig('../slides/img/rwbt2t_model_all_latencies_dirft{0}_stddrift{1}_sp{2}.png'.format(
        str(mudrift).replace('.','_'),
        str(std_drift).replace('.','_'),
        str(std_sp).replace('.','_')))
    #show()

