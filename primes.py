"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""
from decimal import ROUND_UP
import math

def primes(number_of_primes):
    list = []#list of prime numbers that have been found
    if (number_of_primes <= 0):#if 0 or less entered give an error
        return "ValueError"
    i=2 #the first prime number
    while len(list)!= number_of_primes: #if we have not got the correct number of items in the list
        counter = 0 #detects if, for any of the numbers we divide i by, there is a remainder of 0. if there is a remainder of 0, the number can't be prime.
        for x in range(2, (1+ int(math.sqrt(i)))):
            if i%x == 0:
                counter+=1
        if counter == 0: #if the number is prime (no non primes detected) add it to the list
            list.append(i)       
        i+=1
        print("loop")
    return list



