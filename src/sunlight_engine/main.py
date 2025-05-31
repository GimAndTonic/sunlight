import os

from config_interface import ConfigInterface
from logging_setup import Logger

logger          = Logger()
configInterface = None

def get_sunlight_home() :
    sunlight_home = os.getenv("SUNLIGHT_HOME")
    if not sunlight_home:
        logger.warning("SUNLIGHT_HOME is not set")
    return sunlight_home

def cleanup():
    SUNLIGHT_HOME = get_sunlight_home()
    logger.info("Deleting runtime variables in %s/var" % SUNLIGHT_HOME)
    PATH_VAR = os.path.join( SUNLIGHT_HOME, "var")
    if os.path.exists(PATH_VAR):
        for item in os.listdir(PATH_VAR):
            item_path = os.path.join(PATH_VAR, item)
            try:
                if os.path.isfile(item_path) or os.path.islink(item_path):
                    os.remove(item_path)
                elif os.path.isdir(item_path):
                    logger.warning("Unsupported file format: directory in /var/ can not be deleted: %s" % item_path)        
            except Exception as e:
                logger.warning(f"Failed to remove {PATH_VAR}: {e}")
    logger.info("Deleting runtime variables done.")
    
def run():
    print("Programm start.")
    logger.info("App started")

    logger.info("Set runtime variables")
    configInterface = ConfigInterface()
    configInterface.gen_runtime_config()
    logger.info("Set runtime variables: done")

    print("Programm setup complete.")

    print("foo")

    print("Programm ended shutdown initiated.")
    logger.info("Shuting Down App")
    cleanup()
    logger.info("App stopped")
    print("Programm end.")
