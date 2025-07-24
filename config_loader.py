import yaml
import logging


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
