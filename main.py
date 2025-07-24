import logging
import yaml
from simulation import run_simulation
from plotting import plot_results


def setup_logger(log_file="simulation.log"):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler(log_file)
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

# Configuration Loader with Validation


def load_config(config_file="simulation_config.yaml"):
    try:
        with open(config_file, 'r') as file:
            config = yaml.safe_load(file)
        if not config or 'simulation' not in config or 'duration_hours' not in config['simulation']:
            raise ValueError(
                "Invalid config: 'simulation.duration_hours' is required")
        return config
    except FileNotFoundError:
        logging.error(f"Config file {config_file} not found")
        raise
    except yaml.YAMLError as e:
        logging.error(f"Error parsing config file: {e}")
        raise

# Main Logic


def main():
    try:
        config = load_config()
        logger = setup_logger()
        logger.info("Simulation started.")
        grid_load, renewable_generation, battery_soc, ev_energy_delivered = run_simulation(
            config['simulation']['duration_hours'], base_load_amplitude=2.5, peak_load_factor=3.0)
        logger.info("Simulation completed.")
        logger.info(f"Final Grid Load: {grid_load[-1]}")
        logger.info(f"Final Renewable Generation: {renewable_generation[-1]}")
        logger.info(f"Final Battery SOC: {battery_soc[-1]}")
        plot_results(grid_load, renewable_generation,
                     battery_soc, ev_energy_delivered)
    except Exception as e:
        logger.error(f"Main execution failed: {e}")


if __name__ == "__main__":
    main()
