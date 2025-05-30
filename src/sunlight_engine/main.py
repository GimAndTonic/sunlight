import os

import config_interface as config_interface
from logging_setup import logger

def get_sunlight_home() :

    sunlight_home = os.getenv("SUNLIGHT_HOME")

    if not sunlight_home:
        raise EnvironmentError("SUNLIGHT_HOME is not set")

    print(f"SUNLIGHT_HOME is: {sunlight_home}")

def set_var():
    config_interface.gen_config_var()

def run():
    logger.info("App started")

    logger.info("Set runtime variables")
    set_var()
    logger.info("Set runtime variables: done")
    print("foo")

    logger.info("App stopped")
