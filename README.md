# IoT Simulator for Smart Grids

## Overview

This project provides a Python-based simulator for modeling IoT-enabled smart grid systems over a 24-hour period. It models interactions between solar panels, battery storage, electric vehicle (EV) chargers, and smart meters. Designed for flexibility and extensibility, the simulator supports energy system design, testing, and research in renewable energy and smart grid optimization.

## Objectives

- Simulate energy generation, consumption, and storage within a smart grid.
- Provide a modular codebase for easy updates and scalability.
- Generate visualizations to interpret system performance.
- Serve as a platform for testing IoT-based energy management strategies.

## System Architecture

### Modules

1. **Configuration (`simulation_config.yaml`)**  
   Defines simulation parameters, including the duration (default: 24 hours).

2. **Device Classes (`devices.py`)**  
   Models components such as:

   - `SolarPanel` (6 kW capacity)
   - `BatteryStorage` (50 kWh, 95% efficiency)
   - `EVCharger` (7.4 kW, active 12:00–14:00)
   - `SmartMeter`

3. **Simulation Logic (`simulation.py`)**  
   Controls hourly simulation of loads, generation, EV charging, and battery logic.

4. **Visualization (`plotting.py`)**  
   Generates four Matplotlib plots:

   - Grid Load vs. Renewable Generation
   - Renewable Generation vs. Battery SOC
   - Battery SOC Over Time
   - EV Energy Delivered

5. **Entry Point (`main.py`)**  
   Orchestrates configuration loading, simulation execution, and plot generation.

### Energy Model

| Component      | Description            | Parameters                            |
| -------------- | ---------------------- | ------------------------------------- |
| SolarPanel     | Simulates solar output | 6 kW, output varies 80–120%           |
| BatteryStorage | Stores/reserves energy | 50 kWh, 95% efficiency, max rate 6 kW |
| EVCharger      | Models EV energy use   | 7.4 kW max rate, active 2 hours daily |
| SmartMeter     | Tracks consumption     | Non-negative load profile             |

- **Load Profile**: Sinusoidal base with an evening peak (18–21h), scaled x3 with ±20% randomness.

## Installation

### Requirements

- Python 3.8+
- `numpy`, `matplotlib`, `pyyaml`

### Setup

```bash
pip install numpy matplotlib pyyaml
```

### Run Simulation

```bash
python main.py
```

## Output and Insights

### Key Metrics

- **Battery SOC**: Starts at 25 kWh, drops to 0 kWh by end of simulation.
- **Solar Generation**: Peaks at 6 kW mid-day.
- **Grid Load**: Increases during EV charging and evening peak.
- **EV Charging**: Delivers 14.8 kWh over a 2-hour charging period.

### Observations

- Mid-day solar peaks align with highest generation.
- Battery under-utilized (20/50 kWh); higher solar input or grid backup needed.
- Evening loads exceed stored energy, stressing grid.

## Visual Output

_The following plots are generated upon simulation completion:_

- Grid Load vs. Renewable Generation
- Renewable Generation vs. Battery SOC
- Battery SOC Over Time
- EV Energy Delivered

> Plots are saved automatically to the working directory.

## Learnings and Recommendations

- Load variability enhances realism, but demands flexible storage strategies.
- Improving solar efficiency can reduce reliance on the grid.
- Modular architecture simplifies integration of new devices or profiles.

## Project Structure

```
iot-simulator-smart-grids/
├── devices.py
├── simulation.py
├── plotting.py
├── main.py
├── simulation_config.yaml
└── README.md
```

## References

- [Matplotlib Documentation](https://matplotlib.org/stable/)
- [NumPy Documentation](https://numpy.org/doc/stable/)
- [PyYAML Documentation](https://pyyaml.org/wiki/PyYAMLDocumentation)
