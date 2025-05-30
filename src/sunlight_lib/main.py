from python_helper.logging_setup import logger

import python_helper.merge_configs as merge_configs



def set_var():
    merge_configs.run()

def run():
    logger.info("App started")

    logger.info("Set runtime variables")
    set_var()
    logger.info("Set runtime variables: done")
    print("foo")

    logger.info("App stopped")
