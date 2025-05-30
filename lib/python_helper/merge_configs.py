from python_helper.logging_setup import logger

import json
from pathlib import Path

def get_sunlight_home() :
    sunlightHome = Path().resolve()
    return sunlightHome


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

def run() :
    logger.info("Merging default and local configs: coordinates")
    sunlightHome = get_sunlight_home()
    coords = load_and_merge_coordinates(sunlightHome)
    logger.info(f"Latitude: {coords['latitude']}, Longitude: {coords['longitude']}, Elevation: {coords['elevation']}")
    
