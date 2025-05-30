import python_helper.config_interface as config_interface
from python_helper.logging_setup import logger


def set_var():
    config_interface.gen_config_var()

def run():
    logger.info("App started")

    logger.info("Set runtime variables")
    set_var()
    logger.info("Set runtime variables: done")
    print("foo")

    logger.info("App stopped")
