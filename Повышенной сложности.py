#!/usr/bin/env python3
# -*- кодировка: utf-8 -*-
import math
import sys

print('Введите предложение')
s = input()
s1 = s.split(' ')
for i in range(len(s1)-1):
    for j in range(len(s1)-i-1):
        if len(s1[j]) < len(s1[j+1]): # Вариант по убыванию. По возрастанию - заменить < на >
            s1[j], s1[j+1] = s1[j+1], s1[j]
 
s = ''
for i in range(0, len(s1)):
    s += s1[i] + ' '
 
print(s)
