# IoT Simulator for Smart Grids

## Project Objectives

This project aims to develop a robust simulation tool for modeling and analyzing IoT-enabled smart grid systems. The primary objectives are:

- **Simulate Energy Dynamics**: Create a realistic simulation of grid load, renewable generation, battery storage, and electric vehicle (EV) charging in a smart grid environment.
- **Enhance Modularity**: Design a flexible, modular structure for easy updates and scalability.
- **Provide Visualization**: Generate comprehensive plots to analyze energy system performance over time.
- **Support Research and Development**: Offer a tool for testing and optimizing IoT-based energy management strategies.

## Project Overview

The IoT Simulator for Smart Grids is a Python-based tool that simulates the interaction of solar panels, battery storage, EV chargers, and smart meters in a 24-hour smart grid environment. It leverages a modular architecture to model energy generation, storage, and consumption, providing insights into grid stability and renewable integration. The simulator includes dynamic load profiles, realistic battery management, and visualization of key metrics, making it suitable for research and practical applications in smart grid design.

## Technical Implementation

### Core Components

1. **Configuration (`simulation_config.yaml`)**:

   - Defines simulation parameters, such as `duration_hours` (set to 24).

2. **Device Classes (`devices.py`)**:

   - Implements `SolarPanel`, `BatteryStorage`, `EVCharger`, and `SmartMeter` with realistic constraints (e.g., 6 kW solar capacity, 50 kWh battery, 95% efficiency).

3. **Simulation Logic (`simulation.py`)**:

   - Manages the 24-hour simulation, incorporating dynamic load profiles (base load with evening peaks), renewable generation, and battery recharge logic for late-day scenarios.

4. **Visualization (`plotting.py`)**:

   - Generates four plots using Matplotlib: Grid Load vs Renewable Generation, Renewable Generation vs Battery SOC, Battery SOC Over Time, and EV Energy Delivered.

5. **Entry Point (`main.py`)**:
   - Orchestrates the simulation by loading configuration, running the simulation, logging results, and generating visualizations.

### Energy System Features

| Component        | Description                  | Key Parameters                                    |
| ---------------- | ---------------------------- | ------------------------------------------------- |
| `SolarPanel`     | Simulates solar power output | Capacity: 6 kW, Variability: 80-120%              |
| `BatteryStorage` | Manages energy storage       | Capacity: 50 kWh, Efficiency: 95%, Max Rate: 6 kW |
| `EVCharger`      | Models EV charging           | Max Charge: 7.4 kW, Active: 12-14 hours           |
| `SmartMeter`     | Tracks energy consumption    | Non-negative consumption                          |

**Dynamic Load Model**: Base load follows a sinusoidal pattern with an evening peak (18-21 hours) scaled by a factor of 3.0 with 20% random variation.

## Installation and Usage

### Setup Instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/iot-simulator-smart-grids.git
   cd iot-simulator-smart-grids
   ```

2. Install dependencies:

   ```bash
   pip install numpy matplotlib pyyaml
   ```

3. Run the simulation:

   ```bash
   python main.py
   ```

## Performance Insights

### Key Metrics

- **Battery SOC**: Starts at 25 kWh, peaks up to 20 kWh (partial utilization of 50 kWh), and declines to 0 kWh by end-day.
- **Renewable Generation**: Ranges from 0 to 6 kWh, peaking mid-day.
- **Grid Load**: Varies from 0 to 6 kWh, with peaks during EV charging (12-14 hours) and evening demand (18-21 hours).
- **EV Energy Delivered**: Reaches 14.8 kWh with 2 hours of charging at 7.4 kWh.

### Realism Assessment

- The simulation is highly realistic with non-negative values, dynamic loads, and correct EV charging.
- Limitations include partial battery utilization (20 kWh vs. 50 kWh) and limited late-day recharge, suggesting potential for higher solar capacity or grid support.

## Visualizations

The simulator generates visualizations to provide insights into energy system performance.

### Screenshots

- **Grid Load vs Renewable Generation (`generated_plot.png`)**: Bar chart comparing grid load (blue) and renewable generation (orange) over 24 hours, highlighting demand and supply dynamics.
- **Renewable Generation vs Battery SOC (`generated_plot.png`)**: Scatter plot showing correlation between generation and battery state of charge (red dots).
- **Battery SOC Over Time (`generated_plot.png`)**: Line plot of battery SOC (green) from 25 kWh to 0 kWh.
- **EV Energy Delivered (`generated_plot.png`)**: Bar chart of EV energy delivery (purple), peaking at 14.8 kWh.

_Note_: Plots are generated dynamically; filenames are illustrative.

## Key Insights and Learnings

### Successful Outcomes

- **Realistic Energy Dynamics**: Captures mid-day solar peaks and evening load surges effectively.
- **Modular Design**: Allows easy modification of devices and simulation logic.
- **EV Integration**: Successfully models 7.4 kWh charging during designated hours.

### Areas for Improvement

- **Battery Utilization**: SOC reaches only 20 kWh; increasing solar capacity or efficiency could maximize the 50 kWh capacity.
- **Late-Day Recharge**: Limited recharge after 18:00 suggests need for extended solar availability or grid input.
- **Load Balancing**: Occasional high grid loads could be mitigated with enhanced battery discharge strategies.

### Key Learnings

- **Dynamic Loads**: Evening peak variations improve realism but require robust battery support.
- **Renewable Reliance**: Higher solar capacity is key to full battery utilization.
- **Modularity**: Separate files enhance maintainability and scalability.

## Project Structure

```
iot-simulator-smart-grids/
│
├── devices.py            # Device classes (SolarPanel, BatteryStorage, EVCharger, SmartMeter)
├── simulation.py         # Simulation logic
├── plotting.py           # Visualization functions
├── main.py               # Entry point and orchestration
├── simulation_config.yaml # Configuration file
└── README.md
```

## References

1. [Matplotlib Documentation](https://matplotlib.org/stable/)
2. [NumPy Documentation](https://numpy.org/doc/stable/)
3. [PyYAML Documentation](https://pyyaml.org/wiki/PyYAMLDocumentation)

## License

This project is licensed under the MIT License.
