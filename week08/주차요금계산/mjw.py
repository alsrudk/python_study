# https://school.programmers.co.kr/learn/courses/30/lessons/92341

from math import ceil
from collections import defaultdict

def time2min(t):
    hh, mm = t.split(':')
    return int(hh)*60 + int(mm)

class Parking:
    def __init__(self, fees):
        self.fees = fees

        self.parked = False
        self.in_time = 0
        self.parking_time = 0
    
    def update(self, t, history):
        t = time2min(t)
        if history == 'IN':
            self.parked = True
            self.in_time = t
        else:
            self.parked = False
            self.parking_time += (t - self.in_time)
    
    def calc(self):
        if self.parked:
            self.update('23:59', 'OUT')

        fare = self.fees[1]
        if self.parking_time > self.fees[0]:
            fare += ceil((self.parking_time-self.fees[0])/self.fees[2])*self.fees[3]
        return fare


def solution(fees, records):
    cars = defaultdict(lambda:Parking(fees))
    
    for record in records:
        time_, id_, history = record.split()
        cars[id_].update(time_, history)
        
    return [cars[id_].calc() for id_ in sorted(cars)]
