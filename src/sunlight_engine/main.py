import os

from config_interface import ConfigInterface
from logging_setup import Logger

logger          = Logger()
configInterface = None

def get_sunlight_home() :

    sunlight_home = os.getenv("SUNLIGHT_HOME")

    if not sunlight_home:
        raise EnvironmentError("SUNLIGHT_HOME is not set")

    print(f"SUNLIGHT_HOME is: {sunlight_home}")

    return sunlight_home

def cleanup():
    PATH_VAR = os.path.join( get_sunlight_home(), "var")
    try:
        if os.path.exists(PATH_VAR):
            os.remove(PATH_VAR)
            print(f"Removed: {PATH_VAR}")
    except Exception as e:
        logger.warning(f"Failed to remove {PATH_VAR}: {e}")

def run():
    logger.info("App started")

    logger.info("Set runtime variables")
    configInterface = ConfigInterface()
    configInterface.gen_runtime_config()
    logger.info("Set runtime variables: done")
    
    print("foo")

    logger.info("Shuting Down App")
    cleanup()
    logger.info("App stopped")
