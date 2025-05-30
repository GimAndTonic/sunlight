import json
import os
from pathlib import Path

# lib
from logging_setup import Logger

class ConfigInterface :
    ##################
    ## PARAMETER::PATH
    CONFIG_COORD_DEFAULT    = "etc/default/coordinates.json"
    CONFIG_COORD_LOCAL      = "etc/local/coordinates.json"
    CONFIG_COORD_VAR        = "var/coordinates.json"
    ##
    ##################

    ##################
    ## PARAMETER::SYSTEM::set on __init__
    SUNLIGHT_HOME           = None
    logger                  = None
    ##
    ##################

    ##################
    ## VAR::CONFIG
    CONFIG_DIR              = None
    ##
    ##################

    def __init__(self) :
        self.logger         = Logger()
        self.logger.info("New log client in config_interface.py")
        self.SUNLIGHT_HOME  = os.getenv("SUNLIGHT_HOME")
        self.logger.info("Config Interface Configured")

        self.__sys_check__()

    def __sys_check__(self) :
        if not self.SUNLIGHT_HOME:
            self.logger.warning("SUNLIGHT_HOME is not set")
            

    def gen_runtime_config(sunlightHome) :
        self.logger.info("Merging default and local configs: coordinates")

        default_path = Path("%s/etc/default/coordinates.json" % SUNLIGHT_HOME)
        local_path   = Path("%s/etc/local/coordinates.json" % SUNLIGHT_HOME)
        output_path  = Path("%s/var/coordinates.json" % SUNLIGHT_HOME)

        # Load default config
        with default_path.open() as f:
            coords = json.load(f)

        # Merge with local overrides if available
        if local_path.exists():
            with local_path.open() as f:
                local_coords = json.load(f)
            coords.update(local_coords)

        # Write merged config to var/
        output_path.parent.mkdir(parents=True, exist_ok=True)  # Ensure var/ exists
        with output_path.open("w") as f:
            json.dump(coords, f, indent=2)

        self.logger.info(f"Latitude: {coords['latitude']}, Longitude: {coords['longitude']}, Elevation: {coords['elevation']}")

        return coords

    def load_runtime_config(self) :
        self.logger.info("Load runtime variables...")
        self.__sys_check__()

        self.logger.info("Load coordinates...")
        path_var  = os.path.join(self.SUNLIGHT_HOME, self.CONFIG_COORD_VAR)
        with open(path_var, "r") as f:
            coords = json.load(f)
        self.logger.info("coordinates.json: %s" % coords)

        self.CONFIG_DIR['gps'] = coords

        return coords