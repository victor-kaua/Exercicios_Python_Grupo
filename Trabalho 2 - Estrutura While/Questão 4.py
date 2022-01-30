# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 00:32:33 2021

@author: Victor Kauã
"""
n = int(input('Entre com NUM: '))

b=1
if n<0:
    print(f'Não existe fatorial de {n}')

if n==0:
    print('*'*b)


else:
    fat = 1
    i=1
    while i<=n:
         fat *= i
         i += 1
    print('*'*fat)
    vasco = fat//2
    vascao = vasco//2
    print('*'*vascao)
        