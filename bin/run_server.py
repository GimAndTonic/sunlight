import sys
from pathlib import Path

# Add src/ and lib/ to sys.path
sunlightHome = Path(__file__).resolve().parent.parent
sys.path.append(str(sunlightHome / "src"))
sys.path.append(str(sunlightHome / "lib"))

from sunlight_lib import main

if __name__ == "__main__":
    main.run()