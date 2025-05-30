import json
import os
from pathlib import Path

from python_helper.logging_setup import logger



class ConfigInterface :
    ##################
    ## PARAMETER::PATH
    CONFIG_COORD_DEFAULT    = "etc/default/coordinates.json"
    CONFIG_COORD_LOCAL      = "etc/local/coordinates.json"
    CONFIG_COORD_VAR        = "var/coordinates.json"
    ##################

    sunlight_home           = None

    def __get_sunlight_home() :
        sunlight_home = os.getenv("SUNLIGHT_HOME")

        if not sunlight_home:
            raise EnvironmentError("SUNLIGHT_HOME is not set")

        print(f"SUNLIGHT_HOME is: {sunlight_home}")

        return sunlight_home

def load_coordinates(sunlightHome) :
    path_var  = os.path.join(sunlightHome, CONFIG_COORD_VAR)
    
    # Load var config
    with open(path_var, "r") as f:
        coords = json.load(f)

    print(coords)

def load_and_merge_coordinates(sunlightHome) :
    default_path = Path("%s/etc/default/coordinates.json" % sunlightHome)
    local_path   = Path("%s/etc/local/coordinates.json" % sunlightHome)
    output_path  = Path("%s/var/coordinates.json" % sunlightHome)

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

    return coords

def gen_config_var() :
    logger.info("Merging default and local configs: coordinates")
    sunlightHome = get_sunlight_home()
    coords = load_and_merge_coordinates(sunlightHome)
    logger.info(f"Latitude: {coords['latitude']}, Longitude: {coords['longitude']}, Elevation: {coords['elevation']}")
    
def load_config_var_coordinates() :
    logger.info("Load coordinates from var...")
    sunlightHome = get_sunlight_home()
    coords = load_coordinates(sunlightHome)
