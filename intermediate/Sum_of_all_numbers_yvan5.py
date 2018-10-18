#!/usr/bin/env python
# -*- coding: utf-8 -*-

def sum_all(tab):
    #si ordre inverse
    if tab[0] > tab[1]:
        #switch
        tmp = tab[0]
        tab[0] = tab[1]
        tab[1] = tmp
    print(tab)

    #parcourir le tableau
    i = tab[0]
    res = 0
    while(i <= tab[1]):
        res = res + i
        i += 1
    return res

if __name__ == "__main__":
    print(sum_all([1, 4]))
    print(sum_all([4, 1]))
