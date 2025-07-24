import random
import numpy as np


class SolarPanel:
    def __init__(self, capacity=6):
        self.capacity = capacity

    def get_power(self, hour):
        base = self.capacity * np.sin((hour / 24) * 2 * np.pi)
        return max(0, base * (0.8 + 0.4 * random.random()))


class BatteryStorage:
    def __init__(self, capacity=50, efficiency=0.95):
        self.capacity = capacity
        self.soc = capacity / 2
        self.efficiency = efficiency
        self.max_rate = 6

    def charge(self, amount):
        effective_amount = amount * self.efficiency
        self.soc = min(self.capacity, self.soc +
                       min(effective_amount, self.max_rate))

    def discharge(self, amount):
        effective_amount = amount / self.efficiency
        self.soc = max(0, self.soc - min(effective_amount, self.max_rate))


class EVCharger:
    def __init__(self, max_charge=7.4):
        self.max_charge = max_charge
        self.energy_delivered = 0

    def charge(self, hours):
        if hours > 0:
            self.energy_delivered += self.max_charge * hours


class SmartMeter:
    def __init__(self):
        self.energy_consumed = 0

    def consume(self, amount):
        self.energy_consumed += max(0, amount)
