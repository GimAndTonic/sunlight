import sys
import os

# Add src/ and lib/ to sys.path
SUNLIGHT_HOME = os.getenv("SUNLIGHT_HOME")

if not SUNLIGHT_HOME :
    print("ERROR: SUNLIGHT_HOME is not defined")
    print("Start failed - program end.")
    sys.exit()


sys.path.append( os.path.join(SUNLIGHT_HOME, "src") )
sys.path.append( os.path.join(SUNLIGHT_HOME, "src/sunlight_engine") )
sys.path.append( os.path.join(SUNLIGHT_HOME, "src/sunlight_engine/lib") )
#sys.path.append( os.path.join(SUNLIGHT_HOME, "lib") )

from sunlight_engine import main

if __name__ == "__main__":
    main.run()