import json
import os
from pathlib import Path

# lib
from logging_setup import Logger

class ConfigInterface :
    ##################
    ## PARAMETER::PATH
    __CONFIG_COORD_DEFAULT    = "etc/default/sim_config.json"
    __CONFIG_COORD_LOCAL      = "etc/local/sim_config.json"
    __CONFIG_COORD_VAR        = "var/sim_config.json"
    ##
    ##################

    ##################
    ## PARAMETER::SYSTEM::set on __init__
    __SUNLIGHT_HOME           = None
    __logger                  = None
    ##
    ##################

    ##################
    ## VAR::CONFIG
    CONFIG_DIR              = dict()
    ##
    ##################

    def __init__(self) :
        self.__logger         = Logger()
        self.__logger.info("New log client in config_interface.py")
        self.__SUNLIGHT_HOME  = os.getenv("SUNLIGHT_HOME")
        self.__logger.info("Config Interface Configured")

        self.__sys_check__()

    def __sys_check__(self) :
        if not self.__SUNLIGHT_HOME:
            self.__logger.warning("SUNLIGHT_HOME is not set")            

    def gen_runtime_config(self) :
        self.__logger.info("Merging default and local configs: coordinates")

        default_path = os.path.join(self.__SUNLIGHT_HOME, self.__CONFIG_COORD_DEFAULT)
        local_path   = os.path.join(self.__SUNLIGHT_HOME, self.__CONFIG_COORD_LOCAL)
        output_path  = os.path.join(self.__SUNLIGHT_HOME, self.__CONFIG_COORD_VAR)

        # Load default config
        with open(default_path, "r") as f:
            coords = json.load(f)

        # Merge with local overrides if available
        if os.path.exists(local_path) :
            with open(local_path, "r") as f:
                local_coords = json.load(f)
            coords.update(local_coords)

        # Write merged config to var/
        if not os.path.exists( os.path.dirname(output_path) ) :
            self.__logger.warning("/var/ does not exists. Creating directory %s" % os.path.dirname(output_path))
            os.mkdir(os.path.dirname(output_path))

        with open( output_path, "w") as f:
            json.dump(coords, f, indent=2)

        self.__logger.info(coords)

        return coords

    def load_runtime_config(self) :
        self.__logger.info("Load runtime variables...")
        self.__sys_check__()

        self.__logger.info("Load coordinates...")
        path_var  = os.path.join(self.__SUNLIGHT_HOME, self.__CONFIG_COORD_VAR)
        with open(path_var, "r") as f:
            coords = json.load(f)
        self.__logger.info("sim_config.json: %s" % coords)

        self.CONFIG_DIR['location'] = coords
