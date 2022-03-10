# Password Generator 

from re import T

import random
upper_letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_letters="abcdefghijklmnopqrstuvwxyz"
numbers="0123456789"
symbols="[]{}()!@#$%^&*_-=+><?/.,';:"

all=""
upper,lower,number,symbol= True,True,True,True

if upper:
    all+=upper_letters 
if lower:
    all+=lower_letters 
if number:
    all+=numbers
if symbol:
    all+=symbols 

length=1 
for i in range(length):
    password="".join(random.sample(all,10))
    print(password)