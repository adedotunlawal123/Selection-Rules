#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 20:05:34 2021

@author: amlawal
"""

Nmax = 20
no_trnstn_pth = 0
#range over all the allowed principal quantum number n so that n2 is always 
#greater than n1
for n2 in range(2, Nmax+1):
    En2 = -13.6/(n2**2) #E2
    for n1 in range(1, n2):
        En1 = -13.6/(n1**2)
        #range over all allowed angular momentum numbers (l) for n1 and n2
        for l2 in range(0, n2):
            for l1 in range(0, n1):
                #range over all the allowed angular momentum projection (m)
                for m2 in range(-l2, l2+1):
                    for m1 in range(-l1, l1+1):
                        #check if the selection rule is satisfied
                        if (l2 - l1 == 1 or l2 - l1 == -1) and \
                        (m2 - m1 == 0 or m2 - m1 == 1 or m2 - m1 == -1):
                            #for satisfied selection rule increment the \ 
                            #number transition path by 1
                            no_trnstn_pth += 1
        dlt_E = En2 - En1
        wvlngth = 1240/dlt_E
        if 380 < wvlngth < 750:
            n1 = str(n1)+'v' #append string for visible light spectrum
        print('{}->{} {:10} {:10.3f} {:10.3f}'.format(n2,n1,no_trnstn_pth,\
                                                    dlt_E, wvlngth))
        no_trnstn_pth = 0 #reassign the number of transition path to 0 for n1
