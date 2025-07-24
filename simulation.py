import numpy as np
import random
from devices import SolarPanel, BatteryStorage, EVCharger, SmartMeter


def run_simulation(duration, base_load_amplitude=2.0, peak_load_factor=3.0):
    try:
        solar = SolarPanel()
        battery = BatteryStorage()
        ev_charger = EVCharger()
        smart_meter = SmartMeter()

        grid_load = []
        renewable_generation = []
        battery_soc = []
        ev_energy_delivered = []

        for hour in range(duration):
            solar_gen = solar.get_power(hour)
            base_load = base_load_amplitude + 0.5 * \
                np.sin((hour / 24) * 2 * np.pi)
            evening_peak = peak_load_factor * \
                (1 + 0.2 * random.random()) if 18 <= hour <= 21 else 1.0
            ev_load = 7.4 if 12 <= hour <= 14 and random.random() < 0.5 else 0
            total_load = max(0, (base_load * evening_peak) + ev_load)
            excess_solar = max(0, solar_gen - battery.max_rate)
            battery.charge(min(excess_solar, battery.max_rate))

            if total_load > solar_gen and battery.soc > 0:
                discharge = min(battery.max_rate, total_load -
                                solar_gen, battery.soc)
                battery.discharge(discharge)
                total_load -= discharge * battery.efficiency
                grid_load.append(max(0, total_load))
            else:
                if hour >= 18 and solar_gen > total_load and battery.soc < battery.capacity:
                    charge_amount = min(
                        battery.max_rate, solar_gen - total_load)
                    battery.charge(charge_amount)
                grid_load.append(max(0, total_load - solar_gen))

            renewable_generation.append(solar_gen)
            battery_soc.append(battery.soc)
            if 12 <= hour <= 14 and random.random() < 0.5:
                ev_charger.charge(1)
            ev_energy_delivered.append(ev_charger.energy_delivered)

        return grid_load, renewable_generation, battery_soc, ev_energy_delivered
    except Exception as e:
        raise Exception(f"Simulation failed: {e}")
