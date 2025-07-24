import matplotlib.pyplot as plt
import numpy as np


def plot_results(grid_load, renewable_generation, battery_soc, ev_energy_delivered):
    fig, axs = plt.subplots(2, 2, figsize=(12, 8))
    fig.suptitle('Robust Energy System Simulation Over 24 Hours')

    axs[0, 0].bar(np.arange(len(grid_load)) - 0.2, grid_load,
                  0.4, label='Grid Load (kWh)', color='blue')
    axs[0, 0].bar(np.arange(len(renewable_generation)) + 0.2, renewable_generation,
                  0.4, label='Renewable Generation (kWh)', color='orange')
    axs[0, 0].set_title('Grid Load vs Renewable Generation')
    axs[0, 0].set_xlabel('Hour')
    axs[0, 0].set_ylabel('kWh')
    axs[0, 0].legend()

    axs[0, 1].scatter(renewable_generation, battery_soc,
                      color='red', alpha=0.5)
    axs[0, 1].set_title('Renewable Generation vs Battery SOC')
    axs[0, 1].set_xlabel('Renewable Generation (kWh)')
    axs[0, 1].set_ylabel('Battery SOC (kWh)')

    axs[1, 0].plot(battery_soc, label='Battery SOC (kWh)', color='green')
    axs[1, 0].set_title('Battery SOC Over Time')
    axs[1, 0].set_xlabel('Hour')
    axs[1, 0].set_ylabel('kWh')
    axs[1, 0].legend()

    axs[1, 1].bar(range(len(ev_energy_delivered)),
                  ev_energy_delivered, color='purple')
    axs[1, 1].set_title('EV Energy Delivered')
    axs[1, 1].set_xlabel('Hour')
    axs[1, 1].set_ylabel('kWh')

    plt.tight_layout()
    plt.show()
